Postman Routes --->

register url--> POST accounts/api/register
{
    "email": "user1@user.com",
    "name": "user's naame1",
    "password": "user@123"
}

Login url --> POST accounts/api/login/
{
    "email": "user1@user.com",
    "password": "user@123"
}

PROJECTS --------------->

Fetch all the Projets --> GET /project/projects

Create a Project --> POST project/projects/
{
    "name": "Project1",
    "description": "This is awesome."
}

TASKS------------------>

Fetch all the Tasks --> GET /project/tasks

Create a Task --> POST project/tasks/
{
    "title": "tasks1",
    "description": "This is p1 tasks",
    "deadline":"2025-05-08",
    "project":"1", PK
    "assigned_to": "4" PK
}


Updating a Task --> PATCH project/tasks/{task_id}/
{
    "title": "updatedtasks2",
    "description": "This is p1's updated tasks",
    "deadline":"2025-05-08",
    "project":"1",
    "assigned_to": "4",
    "status":"pending"
}

Deleting a Task --> DEL project/tasks/{task_id}/

Task filtering ---> GET project/tasks/?status=ongoing&project=1&deadline=2025-05-08