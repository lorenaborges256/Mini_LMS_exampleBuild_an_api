from flask import Blueprint
from init import db
from models.student import Student

db_commands = Blueprint('db', __name__)

#commands

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
    
    #create an instance of the Model first
    students = [Student(
        name='Bob',
        email = 'bob@gmail.com',
        address = '123 Baker Street'
        ), Student(
        name='Jack',
        email = 'jack@gmail.com',
        address = '23 B Street'),
    ]

    #adding to the session
    db.session.add_all(students)
    #commit
    db.session.commit()
    print("Tables seeded!!")
