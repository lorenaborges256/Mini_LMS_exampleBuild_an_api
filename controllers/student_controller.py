from flask import Blueprint, jsonify, request
from init import db
from models.student import Student, student_schema, students_schema


students_bp = Blueprint('students', __name__, url_prefix='/students')

# Our routes to be defined ....

# GET/students
@students_bp.route('/')
def get_students():
    #first define a statement: Select * from students;
    stmt = db.select(Student)
    #execute it
    students_list = db.session.scalars(stmt)
    #serialise it
    data = students_schema.dump(students_list)
    #return it as json, the jsonify(list)
    if data:
        return jsonify(data)
    else:
        return {"message": "No record found. Add a student to get started with system..."}

# GET /students/id
@students_bp.route("/<int:student_id>")
def get_students_byid(student_id):
    #define the statement: select * from students where id=student_id;
    stmt = db.select(Student).where(Student.student_id == student_id)
    #execute it
    student = db.session.scalar(stmt)
    #serialise it
    data = student_schema.dump(student)
    #return it 

    if data:         
        return jsonify(data)
    else:
        return {"message": f"Student with id: {student_id} does not exist!"}
    

# POST /students
@students_bp.route("/", methods=["POST"])
def create_students():
    #get details from request body
    body_data = request.get_json()
    #create student object with the request body data
    email = body_data.get("email")
    stmt = db.select(Student).where(Student.email == email)
    #adding to the session
    student = db.session.scalar(stmt)
    #checking the system with an email add 
    data = student_schema.dump(student)

    #display message with the same email issue
    if data: 
        return {"message": f"The Student with email:{email} already exists."}

    new_student = Student(
        name = body_data.get("name"),
        email = body_data.get("email"),
        address = body_data.get("address")
    )
    #add to the section
    db.session.add(new_student)
    #commit the session
    db.session.commit()
    #send Ack
    #creating a new variable to hold the serialised data
    data = student_schema.dump(new_student)
    #calling data to convert with jsonify
    return jsonify(data) , 201
# # Types of error
# fields can not be empty
# email must be unique
# defaults errors - unexpected errors occured
# 404 - not found


# DELETE /students/id
@students_bp.route("/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    #find the student by id: select * from students where student_id=student_id;
    stmt = db.select(Student).where(Student.student_id == student_id)
    student = db.session.scalar(stmt)

    #if student exists:
    if student:
        #delete
        name = student.name
        db.session.delete(student)
        #commit
        db.session.commit()
        #return ack
        return {"message": f"Student with name {student.name} has been deleted successfully."},200

    else: 
        #return ack no record found
        return {"message": f"Student with id {student_id} does not exist."}, 404
     

# PUT/PATCH /students/id (EDIT the student details)
@students_bp.route("/<int:student_id>", methods=["PUT", "PATCH"])
def edit_student(student_id):
    # Get the student from db first
    stmt = db.select(Student).where(Student.student_id == student_id)
    student = db.session.scalar(stmt)

    # if the student does not exist, return 404
    if not student:
        return {"message": f"Student with id {student_id} does not exist."}, 404

    # fetch the info from the request body
    body_data = request.get_json()
    name = body_data.get("name")
    email = body_data.get("email")
    address = body_data.get("address")

    # if email is being changed, ensure it's unique
    if email and email != student.email:
        stmt = db.select(Student).where(Student.email == email)
        existing = db.session.scalar(stmt)
        if existing:
            return {"message": f"The Student with email:{email} already exists."}, 400
        student.email = email

    # update other fields if provided
    if name is not None:
        student.name = name
    if address is not None:
        student.address = address

    # persist changes
    db.session.add(student)
    db.session.commit()

    # return the updated student
    data = student_schema.dump(student)
    return jsonify(data), 200