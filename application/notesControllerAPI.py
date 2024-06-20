from flask import Flask, request
from flask_restful import Resource, Api
from .database import db
from .notesModel import Task

class TaskList(Resource):
    def get(self):
        tasks = Task.query.all()
        return [task.to_dict() for task in tasks], 200

    def post(self):
        data = request.get_json()
        new_task = Task(
            name=data['name'],
            title=data['title'],
            description=data.get('description', '')
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task.to_dict(), 201

# Define the Task Resource for handling a single task
class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return task.to_dict(), 200

    def put(self, task_id):
        data = request.get_json()
        task = Task.query.get_or_404(task_id)
        task.name = data.get('name', task.name)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        db.session.commit()
        return task.to_dict(), 200

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Task deleted'}, 200