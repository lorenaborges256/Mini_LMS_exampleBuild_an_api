from flask import Blueprint, jsonify, request
from init import db

from sqlalchemy.exc import IntegrityError
from models.course import Course, course_schema, courses_schema 

courses_bp = Blueprint('courses', __name__, url_prefix='/courses')

# CREATE - POST /courses



# READ - GET/courses and GET /courses/id

@courses_bp.route('/')
def get_courses():
    #define a statement:
    stmt = db.select(Course)
    #execute it
    courses_list = db.session.scalars(stmt)
    #selialse it
    data = courses_schema.dump(courses_list)
    #if it exists:
    if data:
        #do something
        return jsonify(data)
    else:
        #do something else
        return {"message": "No course found."}, 404

# UPDATE - PUT/PATCH /courses/id

# DELETE - DELETE /courses/id

#define a statement:
#execute it
#selialse it
#if it exists:
    #do something
#else
    #do something else