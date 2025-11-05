from flask import Blueprint, jsonify, request
from init import db
from models.student import Student, student_schema, students_schema
from models.teacher import Teacher, teacher_schema, teachers_schema


teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

# Our routes to be defined ....

# GET/teachers
@teachers_bp.route('/')
def get_teachers():
    #first define a statement: Select * from students;
    stmt = db.select(Teacher)
    #execute it
    teachers_list = db.session.scalars(stmt)
    #serialise it
    data = teachers_schema.dump(teachers_list)
    #return it as json, the jsonify(list)
    if data:
        return jsonify(data)
    else:
        return {"message": "No record found. Add a teachers to get started with system..."}

# # GET /teachers/id
# @teachers_bp.route("/<int:teacher_id>")
# def get_teachers_byid(student_id):
#     #define the statement: select * from students where id=student_id;
#     stmt = db.select(Teacher).where(Teacher.student_id == student_id)
#     #execute it
#     student = db.session.scalar(stmt)
#     #serialise it
#     data = student_schema.dump(student)
#     #return it 

#     if data:         
#         return jsonify(data)
#     else:
#         return {"message": f"Teacher with id: {student_id} does not exist!"}
    

# # POST /students
# @teachers_bp.route("/", methods=["POST"])
# def create_students():
#     #get details from request body
#     body_data = request.get_json()
#     #create student object with the request body data
#     email = body_data.get("email")
#     stmt = db.select(Teacher).where(Teacher.email == email)
#     #adding to the session
#     student = db.session.scalar(stmt)
#     #checking the system with an email add 
#     data = student_schema.dump(student)

#     #display message with the same email issue
#     if data: 
#         return {"message": f"The Teacher with email:{email} already exists."}

#     new_student = Teacher(
#         name = body_data.get("name"),
#         email = body_data.get("email"),
#         address = body_data.get("address")
#     )
#     #add to the section
#     db.session.add(new_student)
#     #commit the session
#     db.session.commit()
#     #send Ack
#     #creating a new variable to hold the serialised data
#     data = student_schema.dump(new_student)
#     #calling data to convert with jsonify
#     return jsonify(data) , 201
# # # Types of error
# # fields can not be empty
# # email must be unique
# # defaults errors - unexpected errors occured
# # 404 - not found


# # DELETE /students/id
# @teachers_bp.route("/<int:student_id>", methods=["DELETE"])
# def delete_student(student_id):
#     #find the student by id: select * from students where student_id=student_id;
#     stmt = db.select(Teacher).where(Teacher.student_id == student_id)
#     student = db.session.scalar(stmt)

#     #if student exists:
#     if student:
#         #delete
#         name = student.name
#         db.session.delete(student)
#         #commit
#         db.session.commit()
#         #return ack
#         return {"message": f"Teacher with name {student.name} has been deleted successfully."},200

#     else: 
#         #return ack no record found
#         return {"message": f"Teacher with id {student_id} does not exist."}, 404
     

# # PUT/PATCH /students/id (EDIT the student details)
# @teachers_bp.route("/<int:student_id>", methods=["PUT", "PATCH"])
# def edit_student(student_id):
#     #Get the std from db first
#     #define statemnet
#     #exc the stmt
    
#     #if the std exists
#         #fetch the info from the request body
#         # make the changes
#         #commit to the db
#         # ack
#     #else
#         #