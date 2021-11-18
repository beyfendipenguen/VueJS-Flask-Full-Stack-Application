from flask import (Flask, jsonify, request, abort)
from flask_cors import CORS

from models import setup_db, ToDoList

#----------------------------------------------------------------#
# Create app configure
#----------------------------------------------------------------#
def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins.
    CORS(app, resources={r"/*": {"origins": "*"}})

#----------------------------------------------------------------#
# API
#----------------------------------------------------------------#
    # The Get route handler
    @app.route('/tasks', methods=['GET'])
    def get_all_tasks():
        try:
            get_all_tasks = ToDoList.query.all()
            format_tasks = [task.format() for task in get_all_tasks]
            totale_tasks = len(format_tasks)

            if totale_tasks == 0:
                abort(404)
            else:
                return jsonify({
                "Success": True,
                "Status": 200, 
                "Tasks": format_tasks,
                "Total Tasks": totale_tasks
                }), 200
        except Exception:
            abort(500)

    # The Post route handler
    @app.route('/task', methods=["POST"])
    def add_task():
        try:
            add_task = request.get_json()

            if add_task == 0:
                abort(500)
            else:
                ToDoList(
                    task = add_task['task'],
                    status = add_task['status'],
                    priority = add_task['priority'],
                    due_date = add_task['due_date'],
                    assignee = add_task['assignee'],
                    notes = add_task['notes']
                ).insert()

            return jsonify({
                "Success": True,
                "Status": 200,
                "Message": "Task added"
            }), 200
        except Exception:
            abort(422)

    # The Put route handler
    @app.route('/task/<int:task_id>', methods=["PUT"])
    def update_task(task_id):
        try:
            up_task = ToDoList.query.filter_by(id=task_id).first()
            req = request.get_json()

            if up_task is None and req is None:
                abort(422)
            else:
                task     = up_task.task     = req['task']
                status   = up_task.status   = req['status']
                priority = up_task.priority = req['priority']
                due_date = up_task.due_date = req['due_date']
                assignee = up_task.assignee = req['assignee']
                notes    = up_task.notes    = req['notes']

                ToDoList(
                    task = task,
                    status = status,
                    priority = priority,
                    due_date = due_date,
                    assignee = assignee,
                    notes = notes,
                ).update()
            
            return jsonify({
                "Success": True,
                "Status": 200,
                "Message": "Task updated" 
            }), 200
        except Exception:
            abort(500)

    # The delete route handler
    @app.route('/task/<int:task_id>', methods=['DELETE'])
    def delete_one_task(task_id):
        try:
            del_one_task = ToDoList.query.filter_by(id=task_id).first()

            if del_one_task is None:
                abort(404)
            else:
                del_one_task.delete()
                return jsonify({
                    "Success": True,
                    "Status": 200,
                    "Delete": task_id,
                    "Message": "One task deleted successfully"
                }), 200
        except Exception:
            abort(500)


    return app
