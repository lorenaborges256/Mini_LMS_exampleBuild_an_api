from flask import Blueprint
from init import db
from models.student import Student
from models.teacher import Teacher
from models.course import Course

db_commands = Blueprint('db', __name__)

#CLI commands
#create
@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created!!")

#drop
@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped!!")

#seed
@db_commands.cli.command('seed')
def seed_tables():
    
    #STUDENTS create an instance of the Model first
    students = [Student(
        name='Bob',
        email = 'bob@gmail.com',
        address = '123 Baker Street'
        ), Student(
        name='Jack',
        email = 'jack@gmail.com',
        address = '23 B Street'),
    ]

    #adding students to the session
    db.session.add_all(students)
    
    #TEACHERS create an instance of the Model first
    teachers = [
        Teacher(
        name='Teacher 1',
        department = 'Math',
        address = '123 teacher Street'), 
        Teacher(
        name='Teacher 2',
        department = 'IT',
        address = '456 teacher Street'),
        Teacher(
        name='Teacher Jack',
        department = 'Science',
        address = 'Teacher 23 B Street'),
    ]

    #adding teachers to the session
    db.session.add_all(teachers)
    db.session.commit()
    #COURSE create an instance of the Model first
    courses = [
        Course(
            name="Physics",
            duration=3,
            teacher_id=teachers[0].teacher_id
        ),
                Course(
            name="Chemistry",
            duration=3,
            teacher_id=teachers[0].teacher_id
        ),        Course(
            name="Biology",
            duration=3,
            teacher_id=teachers[0].teacher_id
        ),        Course(
            name="Mathematics",
            duration=3,
            teacher_id=teachers[1].teacher_id
        ),        Course(
            name="Accounting",
            duration=3,
            teacher_id=teachers[1].teacher_id
        )
    ]

    #adding courses to the session
    db.session.add_all(courses)
    
    
    #commit
    db.session.commit()
    print("Tables seeded!!")