Job Application Tracker

A Python backend project built using Flask and MySQL to manage job applications securely through REST APIs.

Features

. User registration and login

. Password hashing for secure password storage

. JWT-based authentication

. Protected API endpoints

. Add new job applications

. View job applications

. Update application status

. Delete job applications

. User-specific application management

. Input validation and error handling

. MySQL database integration


Technologies Used

.Python
.Flask
.MySQL
.MySQL Connector
.PyJWT
.Werkzeug
.Python-dotenv
.Postman for API testing

Project Structure

job-application-tracker/
│
├── app.py
├── db.py
├── requirements.txt
├── README.md
├── .gitignore
└── test_api.py

Installation and Setup

1.Clone the repository:

git clone https://github.com/mahwish-110/job-application-tracker.git

2.Navigate to the project folder:

cd job-application-tracker

3.Create a virtual environment:

python -m venv .venv

4.Activate the virtual environment (Windows):

.\.venv\Scripts\Activate.ps1

5.Install dependencies:

pip install -r requirements.txt

6.Create a MySQL database named job_tracker.

7.Create a .env file in the project root and add your own configuration:

DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=job_tracker
SECRET_KEY=your_secret_key

Important: Never upload your actual .env file or secret keys to GitHub.

8.Run the Flask application:

python -m flask --app app run --debug

API Endpoints


| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Check API status |
| GET | `/api/test-db` | Test database connection |
| POST | `/api/register` | Register a new user |
| POST | `/api/login` | Authenticate user |
| GET | `/api/profile` | Get logged-in user profile |
| GET | `/api/applications` | View applications |
| POST | `/api/applications` | Add an application |
| PUT | `/api/applications/<id>` | Update an application |
| DELETE | `/api/applications/<id>` | Delete an application |


Testing

API endpoints are tested using Postman by sending HTTP requests with JSON data.

Database

The project uses MySQL with two main tables:

. users – Stores user account information and hashed passwords.

. applications – Stores job application details associated with users.

Security

. Passwords are stored using password hashing.

. JWT tokens are used for authentication.

. Secret keys and database credentials are stored in environment variables.

. Protected routes require authentication.

Author

B.Tech in Computer Science and Engineering (AI & ML), 2026 Graduate.