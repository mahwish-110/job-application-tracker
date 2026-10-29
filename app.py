from flask import Flask 
from db import get_connected 
from flask import request


app=Flask(__name__)

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
def get_applications():
    connection=get_connected()
    cursor=connection.cursor(dictionary=True)

    cursor.execute("SELECT*FROM applications")
    applications=cursor.fetchall()

    cursor.close()
    connection.close()

    return applications

@app.route("/api/applications", methods=["POST"])
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
        (company_name,job_role,status,applied_date)
        VALUES(%s,%s,%s,%s)
    """

    values=(
        data["company_name"],
        data["job_role"],
        data.get("status","Applied"),
        data.get("applied_date")
    )

    cursor.execute(query,values)
    connection.commit()

    cursor.close()
    connection.close()
    return {"message":"Application added successfully!"},201


@app.route("/api/applications/<int:application_id>",methods=["PUT"])
def update_application(application_id):
    data=request.get_json()

    connection=get_connected()
    cursor=connection.cursor()

    query="UPDATE applications SET status=%s WHERE id=%s"
    values=(data["status"],application_id)

    cursor.execute(query,values)
    connection.commit()

    cursor.close()
    connection.close()

    return {"message":"Application status updated successfully!"}

@app.route("/api/applications/<int:application_id>",methods=["DELETE"])
def delete_application(application_id):
    connection=get_connected()
    cursor=connection.cursor()

    query="DELETE FROM applications WHERE id =%s"
    cursor.execute(query,(application_id,))

    if cursor.rowcount==0:
        cursor.close()
        connection.close()
        return {"error": "Application not found"},404

    connection.commit()
    cursor.close()
    connection.close()

    return{"message": "Applocation deleted successfully!"}