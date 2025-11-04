# Mini_LMS_exampleBuild_an_api
MINI Learning Management System - Build together in class, as example for our next assessment DEV1002_ Assignment 3: Web API Server

To create a new app
1. create a virtual enviroment active it
```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Git repo and .gitignore file

3. Installation of the necessary packages. We will need all the packages from the previous app. Feel free to reuse requirements.txt and run 
```bash 
pip install -r requirements.txt 
```
or you can run this: 
```bash 
pip install flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy psycopg2-binary
pip freeze > requirements.txt
```
4. create .env file and add inside it:
```
# DATABASE_URI=database+driver://username:password@server:port/databasename

DATABASE_URI=postgresql+psycopg2://username:password@localhost:5432/databasename
```

5. create a database
- Connect to postgres
```bash
sudo -u postgres psql
```
- create a database
```
CREATE DATABASE jan_lms_db;
```
- see all database in the system -> \l
- see all users int he system -> \du

- create user
```
CREATE USER jan_lms_dev PASSWORD '123456';
```
- grant privileges to database
```
GRANT ALL PRIVILEGES ON DATABASE jan_lms_dev TO jan_lms_dev;
```
- grant privileges to schema, (to find schemas name \dn)
```
GRANT ALL PRIVILEGES ON SCHEMA public TO jan_lms_dev;
```
- connect to database \c databasename

6. create folders, instructures before start flask
````python
#init.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
````
````python
#main.py
from flask import Flask

from init import db

app = Flask(__name__)
print("Flask Server Started.")
app.config['SQLALCHEMY_DATABASE_URI'] = fabcd
db.init_app(app)

````

7. Using flask blueprints from its website

8. create .flaskenv file
```
FLASK_APP = main
FLASK_DEBUG = 1
FLASK_RUN_PORT = 8080
```

