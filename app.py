from flask import Flask 
from db import get_connected 
from flask import request
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
import os

app=Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return {"error": "Token is missing"}, 401
        
        if not token.startswith("Bearer "):
            return {"error": "Invalid token format"}, 401

        token = token.split(" ", 1)[1]

        try:
            data = jwt.decode(
                token,
                app.config["SECRET_KEY"],
                algorithms=["HS256"]
    )

        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}, 401

        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}, 401
        request.user_id = data["sub"]

        return f(*args, **kwargs)

    return decorated

@app.route("/")
def home():
    return "job application tracker API is running!"

@app.route("/api/health")
def health():
    return{
        "status":"success",
        "message":"API is working"
    }

@app.route("/api/test-db")
def test_db():
    connection=get_connected()
    connection.close()

    return{"message":"Database connected successfully"}

@app.route("/api/applications")
@token_required
def get_applications():
    connection=get_connected()
    cursor=connection.cursor(dictionary=True)

    #cursor.execute("SELECT*FROM applications")

    cursor.execute(
        "SELECT*FROM applications WHERE user_id=%s",
        (request.user_id,)
    )
    applications=cursor.fetchall()

    cursor.close()
    connection.close()

    return applications,200


        
@app.route("/api/applications", methods=["POST"])
@token_required
def add_application():
    data=request.get_json()

    if not data.get("company_name") or not data.get("job_role"):
        return {
            "error": "Company name and job role are required"
        },400

    allowed_statuses=["Applied","Interview","Rejected","Selected"]

    status=data.get("status","Applied")

    if status not in allowed_statuses:
        return{
            "error":"Invalid status"
        },400

    connection=get_connected()
    cursor=connection.cursor()

    query="""
        INSERT INTO applications
        (company_name,job_role,status,applied_date,user_id)
        VALUES(%s,%s,%s,%s,%s)
    """

    values=(
        data["company_name"],
        data["job_role"],
        status,
        data.get("applied_date"),
        request.user_id
    )
    cursor.execute(query,values)
    connection.commit()
    cursor.close()
    connection.close()
    return {"message":"Application added successfully!"},201


@app.route("/api/applications/<int:application_id>",methods=["PUT"])
@token_required
def update_application(application_id):
    data=request.get_json()

    connection=get_connected()
    cursor=connection.cursor()

    #query="UPDATE applications SET status=%s WHERE id=%s"
    #values=(data["status"],application_id)
    query = """
    UPDATE applications
    SET status = %s
    WHERE id = %s AND user_id = %s
"""

    values = (
    data["status"],
    application_id,
    request.user_id
)
    cursor.execute(query,values)
    if cursor.rowcount == 0:
        cursor.close()
        connection.close()
        return {"error": "Application not found"}, 404
    connection.commit()

    cursor.close()
    connection.close()

    return {"message":"Application status updated successfully!"}

@app.route("/api/applications/<int:application_id>",methods=["DELETE"])
@token_required
def delete_application(application_id):
    connection=get_connected()
    cursor=connection.cursor()

    #query="DELETE FROM applications WHERE id =%s"

    query="""
        DELETE FROM applications
        WHERE id=%s AND user_id=%s
        """
    
    cursor.execute(query,(application_id,request.user_id))

    if cursor.rowcount==0:
        cursor.close()
        connection.close()
        return {"error": "Application not found"},404

    connection.commit()
    cursor.close()
    connection.close()

    return{"message": "Applocation deleted successfully!"}

@app.route("/api/register",methods=["POST"])
def register():
    data=request.get_json(silent=True)

    name=data.get("name")
    email=data.get("email")
    password=data.get("password")

    if not name or not email or not password:
        return{"error":"All fields are required"},400

    connection=get_connected()
    cursor=connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT*FROM users WHERE email=%s",
        (email,)
    )
    existing_user=cursor.fetchone()

    if existing_user:
        cursor.close()
        connection.close()
        return {"error":"Email already registered"},409

    hashed_password=generate_password_hash(password)

    cursor.execute(
        "INSERT INTO users (name,email,password_hash)VALUES(%s,%s,%s)",
        (name,email,hashed_password)
    )
    connection.commit()

    cursor.close()
    connection.close()
    return{"message":"User registered successfully!"},201


@app.route("/api/login",methods=["POST"])
def login():
    data=request.get_json(silent=True)

    if not data:
        return{"error":"Invalid JSON data"},400
    
    email=data.get("email")
    password=data.get("password")

    if not email or not password:
        return{"error":"Email and password are required"},400

    connection=get_connected()
    cursor=connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT*FROM users WHERE email=%s",(email,)
    )
    user=cursor.fetchone()

    if not user:
        cursor.close()
        connection.close()
        return{"error":"invalid email or password"},401

    is_password_correct=check_password_hash(
        user["password_hash"],
        password
    )

    if not is_password_correct:
        cursor.close()
        connection.close()
        return{"error":"Invalid email or password"},401
    
    payload = {
    "sub": str(user["id"]),
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

    cursor.close()

    connection.close()
    return {
    "message": "Login Successful",
    "token": token
}, 200
    
@app.route("/api/profile",methods=["GET"])
@token_required
def profile():

    connection=get_connected()
    cursor=connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT id,name,email FROM users WHERE id =%s",
        (request.user_id,)
    )

    user=cursor.fetchone()

    cursor.close()
    connection.close()

    if not user:
        return{
            "error":"User not found"
        },404

    return{
        "message":"profile fetched successfully!",
        "user":user
    },200