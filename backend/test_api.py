#----------------------------------------------------------------#
# Imports
#----------------------------------------------------------------#
import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, ToDoList

#----------------------------------------------------------------#
# Unittest Setup
#----------------------------------------------------------------#
class ToDoListTestCase(unittest.TestCase):
    """This class represents the games library test case."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.user_name = 'postgres'
        self.password = 1234
        self.host = 'localhost:5432'
        self.database_name = 'to_do_list'
        self.database_path = "postgres://{}:{}@{}/{}".format(self.user_name, self.password, self.host, self.database_name)
        setup_db(self.app, self.database_path )

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

#----------------------------------------------------------------#
# Test Cases
#----------------------------------------------------------------#

    def test_get_all_tasks(self):
        req = self.client().get('/tasks')
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)
        self.assertEqual(data['total Tasks'], 5)

    def test_add_new_task(self):
        body = {
            "task":"ToDo project",
            "status":True,
            "priority":"high",
            "due_date":"13/11/2021",
            "assignee":"Projects",
            "notes":"I did done yet"
        }
        req = self.client().post('/task', json=body)
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)
        self.assertEqual(data['Message'], 'Task added')

    def test_update_one_task(self):
        body = {
            "task":"ToDo",
            "status":False,
            "priority":"high",
            "due_date":"13/11/2021",
            "assignee":"Projects",
            "notes":"I did done yet"
        }
        req = self.client().put('/task/10', json=body)
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)
        self.assertEqual(data['Message'], 'Task updated')

    def test_delete_one_task(self):
        req = self.client().delete('/task/10')
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)
        self.assertEqual(data['Message'], 'One task deleted successfully')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()