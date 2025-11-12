from flask import Blueprint, jsonify, request
from init import db
from models.student import Student, student_schema, students_schema
from models.teacher import Teacher, teacher_schema, teachers_schema


teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

# Our routes to be defined ....

# GET/teachers
@teachers_bp.route('/')
def get_teachers():
    #Get the department name from URL
    department = request.args.get('department')
    if department:
        #define a statement: Select * from teachers where department='something/science/math';
        stmt = db.select(Teacher).where(Teacher.department == department)
    else:
        stmt = db.select(Teacher)

    #first define a statement: Select * from teachers;
    # stmt = db.select(Teacher)
    #execute it
    teachers_list = db.session.scalars(stmt)
    #serialise it
    data = teachers_schema.dump(teachers_list)
    #return it as json, the jsonify(list)
    if data:
        return jsonify(data)
    else:
        return {"message": "No record found. Add a teachers to get started with system..."}

# READ - GET /teacher and GET /teachers/id
@teachers_bp.route("/<int:teacher_id>")
def get_teachers_byid(teacher_id):
    #define the statement: select * from teachers where id=student_id;
    stmt = db.select(Teacher).where(Teacher.teacher_id == teacher_id)
    #execute it
    teacher = db.session.scalar(stmt)
    #serialise it
    data = student_schema.dump(teacher)
    #return it 

    if data:         
        return jsonify(data)
    else:
        return {"message": f"Teacher with id: {teacher_id} does not exist!"}
    

# POST /teachers
@teachers_bp.route("/", methods=["POST"])
def create_teachers():
    #get details from request body
    body_data = request.get_json()
    #create teacher object with the request body data
    # email = body_data.get("email")
    stmt = db.select(Teacher)
    #adding to the session
    teacher = db.session.scalar(stmt)
    #checking the system with an email add 
    data = teacher_schema.dump(teacher)

    #display message with the same email issue
    # if data: 
    #     return {"message": f"The Teacher with email:{email} already exists."}

    new_teacher = Teacher(
        name = body_data.get("name"),
        department = body_data.get("department"),
        address = body_data.get("address")
    )
    #add to the section
    db.session.add(new_teacher)
    #commit the session
    db.session.commit()
    #send Ack
    #creating a new variable to hold the serialised data
    data = teacher_schema.dump(new_teacher)
    #calling data to convert with jsonify
    return jsonify(data) , 201
# # Types of error
# fields can not be empty
# email must be unique
# defaults errors - unexpected errors occured
# 404 - not found


# DELETE /teacher/id
@teachers_bp.route("/<int:teacher_id>", methods=["DELETE"])
def delete_teacher(teacher_id):
    #find the teacher by id: select * from teacher where teacher_id=teacher_id;
    stmt = db.select(Teacher).where(Teacher.teacher_id == teacher_id)
    teacher = db.session.scalar(stmt)

    #if teacher exists:
    if teacher:
        #delete
        name = teacher.name
        db.session.delete(teacher)
        #commit
        db.session.commit()
        #return ack
        return {"message": f"Teacher with name {teacher.name} has been deleted successfully."},200

    else: 
        #return ack no record found
        return {"message": f"Teacher with id {teacher_id} does not exist."}, 404
     

# PUT/PATCH /teachers/id (EDIT the teacher details)
@teachers_bp.route("/<int:teacher_id>", methods=["PUT", "PATCH"])
def edit_teacher(teacher_id):
    # try:
        # Get the student from db first
        stmt = db.select(Teacher).where(Teacher.teacher_id == teacher_id)
        #exc the stmt
        teacher = db.session.scalar(stmt)
        
        #if the std exists
        if teacher:
            #fetch the info from the request body
            body_data = request.get_json()
            
            # make the changes (using a short circuit method) using both put and patch
            # where put updates everything 
            # patch updates specific key values
            teacher.name = body_data.get("name", teacher.name)
            teacher.department = body_data.get("department", teacher.department)
            teacher.address = body_data.get("address", teacher.address)
            
            #commit to the db
            db.session.commit()
            # ack
            return jsonify(teacher_schema.dump(teacher))
        #else
        else:
            return {"message": f"Teacher with id: {teacher_id} does not exist"}, 404
            # ack 
    # except IntegrityError as err:
    #     return {"Email address is already in Use "}, 409