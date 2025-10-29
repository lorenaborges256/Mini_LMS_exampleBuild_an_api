from flask import Blueprint
from init import db
from models.student import Student

students_bp = Blueprint('students', __name__, url_prefix='/students')

# Our routes to be defined ....

# GET/students
# GET/students/id
# POST/students
# PUT/PATCH /students/id
# DELETE /students/id

@app.route('/')
def a_fun():
    return "Welcome to the Student Management System"