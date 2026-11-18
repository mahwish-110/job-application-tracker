Job Application Tracker

A full-stack Job Application Tracker built using Python, Flask, MySQL, and Streamlit. The application allows users to securely manage and track their job applications through a web-based dashboard and REST APIs.

Features

User registration and login

Secure password hashing

JWT-based authentication

Protected API endpoints

Add new job applications

View all job applications

Update application status

Delete job applications

User-specific application management

Dashboard with application summary

Interactive application tables

Input validation and error handling

MySQL database integration

Technologies Used

Python

Flask

MySQL

MySQL Connector

Streamlit

Requests

PyJWT

Werkzeug

Python-dotenv

Postman for API testing

Project Structure

job-application-tracker/
│
├── app.py
├── db.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── test_api.py

Installation and Setup

1. Clone the repository

git clone https://github.com/mahwish-110/job-application-tracker.git

2. Navigate to the project folder

cd job-application-tracker

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment (Windows)

.\.venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt

6. Configure MySQL

Create a MySQL database named job_tracker.

7. Configure environment variables

Create a .env file in the project root and add your own configuration:

DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=job_tracker
SECRET_KEY=your_secret_key

Important: Never upload your actual .env file or secret keys to GitHub.

8. Run the Flask backend

Open a terminal and run:

python -m flask --app app run --debug

The Flask backend will run at:

http://127.0.0.1:5000

9. Run the Streamlit frontend

Open a second terminal, activate the same virtual environment, and run:

streamlit run streamlit_app.py

The Streamlit frontend will open in your browser, usually at:

http://localhost:8501

Keep both backend and frontend terminals running while using the application.

API Endpoints

Method	Endpoint	Description


GET	/api/health	Check API status
GET	/api/test-db	Test database connection
POST	/api/register	Register a new user
POST	/api/login	Authenticate user
GET	/api/profile	Get logged-in user profile
GET	/api/applications	View applications
POST	/api/applications	Add an application
PUT	/api/applications/<id>	Update an application
DELETE	/api/applications/<id>	Delete an application

Database

The project uses MySQL with two main tables:

users: Stores user account information and hashed passwords.

applications: Stores job application details associated with individual users.

Testing

API endpoints are tested using Postman by sending HTTP requests with JSON data.

The Streamlit frontend is used to test login, application management, and dashboard functionality.

Security

Passwords are stored using secure password hashing.

JWT tokens are used for authentication.

Database credentials and secret keys are stored in environment variables.

Protected routes require authentication.

Application records are associated with individual users.

Author

B.Tech in Computer Science and Engineering (AI & ML), 2026 Graduate.