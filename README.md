Job Application Tracker

A Python backend project to manage job applications using Flask and MySQL.

Features 

. Add a new job application
. View all job applications
. Update application status
. Delete a job application
. Validate required fields and application status
. Store application data in MYSQL

Technologies Used

. Python
. Flask
. MySQl
. MySql Connector
. Python-dotenv
. Requests for API testing

Installation

1. clone or download the project.

2. Create and activate a virtual environment.

3. Install the required packages:
   pip install -r requirements.txt

4. Create a .env file in the project root
   and add your own database credentials.

5.Run the Flask application:

6.python -m flask --app app run --debug


API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/applications` | View applications |
| POST | `/api/applications` | Add an application |
| PUT | `/api/applications/<id>` | Update application status |
| DELETE | `/api/applications/<id>` | Delete an application |


Note

Do not upload your `.env` file or database password to GitHub.


