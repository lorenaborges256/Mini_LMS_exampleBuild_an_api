from flask import Blueprint, jsonify, request
from init import db

from sqlalchemy.exc import IntegrityError
from models.course import Course, course_schema, courses_schema 

courses_bp = Blueprint('courses', __name__, url_prefix='/courses')

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
    
# READ a course - GET /course_id
@courses_bp.route("/<int:course_id>")
def get_a_course(course_id):
    # Define the statement
    # SQL: SELECT * FROM courses WHERE course_id = course_id;
    stmt = db.select(Course).where(Course.course_id == course_id)
    # excute it
    course = db.session.scalar(stmt)
    # serialise it
    data = course_schema.dump(course)

    # if the course exists
    if data:
        # return it
        return jsonify(data)
    # else
    else:
        # ack
        return {"message": f"Course with id: {course_id} does not exist"}, 404

# CREATE - POST /courses
@courses_bp.route("/", methods=["POST"])
def create_course():
    #get details from request body
    body_data = request.get_json()
    # Validate and create a course
    new_course = course_schema.load(body_data, session=db.session)
    # Add to the session
    db.session.add(new_course)
    # Commit it 
    db.session.commit()
    # Return the newly created course
    return course_schema.dump(new_course), 201

# UPDATE - PUT/PATCH /courses/id

# DELETE - DELETE /courses/id

#define a statement:
#execute it
#selialse it
#if it exists:
    #do something
#else
    #do something else