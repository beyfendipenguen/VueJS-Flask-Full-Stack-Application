#-------------------------------------------------------------#
# Imports
#-------------------------------------------------------------#
from sqlalchemy import (Column, String, Boolean, Integer, create_engine)
from flask_sqlalchemy import SQLAlchemy


#-------------------------------------------------------------#
# Database config
#-------------------------------------------------------------#
user_name = 'postgres'
password = '1234'
host = 'localhost:5432'
database_name = 'to_do_list'
database_path = "postgres://{}:{}@{}/{}".format(user_name, password, host, database_name)

db = SQLAlchemy()

#---------------------------------------------------------------#
# setup_db(app) 
# Binds a flask application and a SQLAlchemy service
#---------------------------------------------------------------#
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#---------------------------------------------------------------#
# Models
#---------------------------------------------------------------#

class ToDoList(db.Model): 
    __tablename__ = "ToDoList"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean)
    priority = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.String(255), nullable=False)
    assignee = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.String(255), nullable=True)


    def __init__(self, task: str, status: bool, priority: str, due_date: str, assignee: str, notes: str):
        self.task = task
        self.status = status
        self.priority = priority
        self.due_date = due_date
        self.assignee = assignee
        self.notes = notes

    def __repr__(self):
        return f"Task('{self.task}', '{self.status}', '{self.priority}', '{self.due_date}', '{self.assignee}', '{self.notes}')"

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'task': self.task,
            'status': self.status,
            'priority': self.priority,
            'due_date': self.due_date,
            'assignee': self.assignee,
            'notes': self.notes
        }
