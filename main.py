import os 
from flask import Flask
from application.config import LocalDevelopmentConfig 
from application.database import db
from flask_restful import Api

app = None
api=None

def createApp():
    app=Flask(__name__,template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    api=Api(app)
    print(app)
    return app,api

app , api =createApp()

from application.notesControllerAPI import *
from application.notesController import *

api.add_resource(TaskList, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port='5000')
    app.run(host='0.0.0.0',debug=True)
