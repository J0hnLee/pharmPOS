from main import create_app, db
from flask_restful_swagger_2 import Api, swagger, get_swagger_blueprint, swagger, Resource
from main.views.model import UserModel
from main.databaseModel.patientModel import Prescription
from main.databaseModel.userModel import user
from main.tasks.userInfo import get_time_resources
from main.tasks.views import tasks_blueprints
import flask_monitoringdashboard as dashboard
from bson import json_util
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import unittest
import os
import sys
from flask_jwt import JWT, jwt_required
from main.tasks.authentication.security import authenticate, identiy

# import table of database

# import manipulation function

# import self-api function
from main.tasks.pharmInfo import get_user_resources

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
CORS(app)
dashboard.bind(app)
app.config['DEBUG'] = True  # open debug mode
app.secret = 'god'
jwt = JWT(app, authenticate, identiy)  # /auth


def auth(api_key, endpoint, method):
    # Space for your fancy authentication. Return True if access is granted, otherwise False
    # api_key is extracted from the url parameters (?api_key=foo)
    # endpoint is the full swagger url (e.g. /some/{value}/endpoint)
    # method is the HTTP method
    return True


# project seperate to 3 parts
swagger.auth = auth
docs = []
# Get time resources
user_resources = get_time_resources()
user_resources_2 = get_user_resources()
# Retrieve and save the swagger document object (do this for each set of resources).
docs.append(user_resources.get_swagger_doc())
docs.append(user_resources_2.get_swagger_doc())

'''
How to use blueprint with swagger
'''
# Register the blueprint for user resources
app.register_blueprint(user_resources.blueprint, url_prefix='/pages')
app.register_blueprint(user_resources_2.blueprint, url_prefix='/pages')

# Prepare a blueprint to server the combined list of swagger document objects and register it
app.register_blueprint(get_swagger_blueprint(docs, '/api/swagger', title='Example', api_version='1'))

# using blueprint to add different page
app.register_blueprint(tasks_blueprints, url_prefix='/tasks')

# app.register_blueprint(whatTime,url_prefix='/pages')
# open database instance
mongo = PyMongo(app, uri="mongodb://localhost:27017/pharmPOS")

"""setting database that can use command"""
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('./test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


# class AllName(Resource):
#     @swagger.doc({'tags': ['users'], 'description': 'Adds a user', 'parameters': [
#         {'name': 'body', 'description': 'Request body', 'in': 'body', 'schema': UserModel, 'required': True, }],
#         'responses': {'201': {'description': 'Created user', 'schema': UserModel,
#             'headers': {'Location': {'type': 'string', 'description': 'Location of the new item'}},
#             'examples': {'application/json': {'id': 1}}}}})
#
#     def get(self):
#         pts = Prescription.query.all()
#         return [pt.json() for pt in pts]

# redirect to swagger page

@app.route('/user/<string:age>', methods=['GET'])
def home_page(age):
    age = str(30)
    if age:
        users = mongo.db.pP.find({"age": age})
        print(age)
        print(type(users))
        for name in users:
            last = json_util.dumps(name)
        print(last)

        return last

    else:
        return 'No user found!'


@app.route('/')
def new_page():
    return """<head>
    <meta http-equiv="refresh" content="0; url=http://petstore.swagger.io/?url=http://localhost:5000/api/swagger.json" />
    </head>"""


# api.add_resource(patientNames, '/<string:pName>')
# api.add_resource(AllName, '/pts')


if __name__ == '__main__':
    manager.run()
