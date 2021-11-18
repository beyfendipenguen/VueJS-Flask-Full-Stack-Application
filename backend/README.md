# API Reference 

## Getting Started

Base URL: At present this app con only be run locally and is not as a base URL yet. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
Authentication: this version of the application does not require authentication or API keys.
You can use the VS-code extension Thunder-client or postman to tests the endpoints if you want.


## Error Handling

Errors are returned as JSON objects in the following format:

```
{
  "error": 400,
  "message": "bad request",
  "success": false
}

{
  "error": 404,
  "message": "resource not found"
  "success": False
}

{
  "error": 422,
  "message": "unprocessable"
  "success": False
}
```

## The API will return three error type when request fail:

400: Bad Request
404: Resource Not Found
422: Not Processable


## Endpoints

### GET/tasks

General:

Returns a list of tasks objects values, And total number of tasks.

Simple: curl -X GET http://127.0.0.1:5000/tasks

```
{
  "Status": 200,
  "Success": true,
  "Tasks": [
    {
      "assignee": "Programming",
      "due_date": "2/8/21",
      "id": 31,
      "notes": "Important course",
      "priority": "high",
      "status": true,
      "task": "ES6 javaScript"
    },
    {
      "assignee": "Design",
      "due_date": "1/6/21",
      "id": 30,
      "notes": "This is course will improver my skills.",
      "priority": "high",
      "status": true,
      "task": "Bootstrap 4"
    },
    {
      "assignee": "Design",
      "due_date": "15/11/21",
      "id": 32,
      "notes": "Good course to take.",
      "priority": "high",
      "status": true,
      "task": "Vue.js"
    },
    {
      "assignee": "Project",
      "due_date": "17/11/21",
      "id": 33,
      "notes": "It's very important for me. ",
      "priority": "high",
      "status": true,
      "task": "To-Do-List project"
    },
    {
      "assignee": "Programming",
      "due_date": "1/2/21",
      "id": 34,
      "notes": "I have to take this course. ",
      "priority": "High",
      "status": true,
      "task": "HTML"
    },
    {
      "assignee": "programming",
      "due_date": "2/2/21",
      "id": 35,
      "notes": "Design course",
      "priority": "high",
      "status": true,
      "task": "Css 3"
    },
    {
      "assignee": "Programming",
      "due_date": "3/4/21",
      "id": 36,
      "notes": "This is course will improver my skills.",
      "priority": "high",
      "status": true,
      "task": "Javascript"
    },
    {
      "assignee": "programming",
      "due_date": "2/5/21",
      "id": 37,
      "notes": "It's good course for me. ",
      "priority": "high",
      "status": true,
      "task": "Flask-framework "
    },
    {
      "assignee": "Programming",
      "due_date": "1/1/21",
      "id": 38,
      "notes": "It's very important for me. ",
      "priority": "high",
      "status": true,
      "task": "Python Full Course"
    },
    {
      "assignee": "design",
      "due_date": "23/11/21",
      "id": 27,
      "notes": "It's good to done this course.",
      "priority": "low",
      "status": false,
      "task": "Sass"
    },
    {
      "assignee": "computer science",
      "due_date": "11/12/21",
      "id": 28,
      "notes": "This course will improver my skills.",
      "priority": "high",
      "status": false,
      "task": "CS'50"
    },
    {
      "assignee": "programming",
      "due_date": "20/11/21",
      "id": 29,
      "notes": "This course will improver my skills.",
      "priority": "high",
      "status": true,
      "task": "python OOP"
    }
  ],
  "Total Tasks": 12
}
```

#### POST/task

General:

POST a new task, which will require the task body. 

Simple: curl -X POST http://127.0.0.1:5000/task

Exempla new task body:

```
{
  "task":"Python OOP",
  "status":true,
  "priority":"high",
  "due_date":"6/11/2021",
  "assignee":"Programming",
  "notes":"I did done it."
}
```

The response message after add new task:

```
{
  "Message": "Task added",
  "Status": 200,
  "Success": true
}
```

#### PUT/task

General:

PUT will update the task object, which will require the task update body.

Simple: curl -X PUT http://127.0.0.1:5000/task/5

Exempla update task body:

```
{
  "task":"ES6",
  "status":false,
  "priority":"high",
  "due_date":"10/11/2021",
  "assignee":"Programming",
  "notes":"I did not done yet"
}
```

The response message after update task:

```
{
  "Message": "Task up updated",
  "Status": 200,
  "Success": true
}
```

#### DELETE/task

General:

DELETE task using a task ID.

Simple: curl -X DEL http://127.0.0.1:5000/task/31

The response message after deleted task successfully:

```
{
  "Delete": 31,
  "Message": "One task deleted successfully",
  "Status": 200,
  "Success": true
}
```

I hope this simple API will improve your back-end skills😊.