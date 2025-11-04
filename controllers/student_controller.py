from flask import Blueprint, jsonify
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
    stmt = db.select(Student).where(Student.id == student_id)
    #execute it
    student = db.session.scalar(stmt)
    #serialise it
    data = student_schema.dump(student)
    #return it 
    if data:         
        return jsonify(data)
    else:
        return {"message": f"Student with id: {student_id} does not exist!"}
    

# # POST /students
# @students_bp.route("/", methods=["POST"])
# def create_students():
#     #create detail from request body
#     body_data = request.get_json()
#     #create student object with the requested body data
#     new_student = Student(
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

#     #display message with same emailo add issues...
#     if data: 
#         return {"message": f"The Student email: {email} already exists. Please use a different email address."}, 409
#     new_student = Student(
#         name = body_data.get("name"),
#         email = body_data.get("email"),
#         address = body_data.get("address")
#     )
#     #calling data to convert with jsonify
#     return jsonify(data)



# # PUT/PATCH /students/id
# # DELETE /students/id
# @students_bp.route("/<int:student_id>", methods=["DELETE"])
# def delete_student(student_id):
#     #find the student by id
#     stmt = db.select(Student).where(Student.id == student_id)
#     student = db.session.scalar(stmt)

#     #if student exists:

#     if student:
#     #delete
#     name = student.name
#     db.session.delete(student)
#     #commit
#     db.session.commit()
#     #return ack
#     return {"message": f"Student {student.name} has been deleted successfully."},200

#     #else
#      #return ack no record found