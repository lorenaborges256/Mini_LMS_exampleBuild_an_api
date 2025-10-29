from flask import Flask

from init import db
import os
# from dotenv import load_dotenv # to initialize app.config['SQLALCHEMY_DATABASE_URI'] = fabcd

# load_dotenv()

#run development phase
from controllers.cli_controllers import db_commands

def create_app():
    app = Flask(__name__)
    print("Flask Server Started.")
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    #or

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

    db.init_app(app)
    app.register_blueprint(db_commands)
    return app



#testing phase


#deployment phase