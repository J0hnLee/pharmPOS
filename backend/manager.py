import os
import sys
print(sys.path)
import unittest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_restful_swagger_2 import Api,swagger, Resource
from flask_cors import CORS

# import table of database
from main import create_app,db
from main.databaseModel.userModel import user
from main.databaseModel.patientModel import Prescription

# import manipulation function

## import self-api function
from main.views.getTime import whatTime
from main.views.model import UserModel

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
CORS(app)
api = Api(app,
    host="localhost:5000",
    #schemes=['http'],
    schemes=['https'],
    #base_path='/dev',
    security_definitions='security',
    security=[{'appKey': []}],
    api_version='0.01',
    api_spec_url='/api/swagger')



def auth(api_key, endpoint, method):
    # Space for your fancy authentication. Return True if access is granted, otherwise False
    # api_key is extracted from the url parameters (?api_key=foo)
    # endpoint is the full swagger url (e.g. /some/{value}/endpoint)
    # method is the HTTP method
    return True

swagger.auth = auth


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

class AllName(Resource):
    @swagger.doc({'tags': ['users'], 'description': 'Adds a user', 'parameters': [
        {'name': 'body', 'description': 'Request body', 'in': 'body', 'schema': UserModel, 'required': True, }],
        'responses': {'201': {'description': 'Created user', 'schema': UserModel,
            'headers': {'Location': {'type': 'string', 'description': 'Location of the new item'}},
            'examples': {'application/json': {'id': 1}}}}})

    def get(self):
        pts = Prescription.query.all()
        return [pt.json() for pt in pts]

# redirect to swagger page
@app.route('/')
def index():
    return """<head>
    <meta http-equiv="refresh" content="0; url=http://petstore.swagger.io/?url=http://localhost:5000/api/swagger.json" />
    </head>"""

#api.add_resource(patientNames, '/<string:pName>')
api.add_resource(AllName, '/pts')


if __name__ == '__main__':
    manager.run()