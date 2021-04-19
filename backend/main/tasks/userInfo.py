import time
from flask import Blueprint
from flask_restful_swagger_2 import Api, swagger, Resource
from ..views import model


class timeResource(Resource):
    @swagger.doc({'tags': ['users'], 'description': 'Adds a user', 'parameters': [
        {'name': 'body', 'description': 'Request body', 'in': 'body', 'schema': model.UserModel, 'required': True, }],
                  'responses': {'201': {'description': 'Created user', 'schema': model.UserModel, 'headers': {
                      'Location': {'type': 'string', 'description': 'Location of the new item'}},
                                        'examples': {'application/json': {'id': 1}}}}})
    def get(self):
        print(time.time())
        a = time.asctime(time.localtime(time.time()))
        print(type(a))
        print(time.asctime(time.localtime(time.time())))
        return {'time': time.asctime(time.localtime(time.time()))}

    def post(self):
        pass

def get_time_resources():
    """
    Returns user resources.
    :param app: The Flask instance
    :return: User resources
    """
    blueprint = Blueprint('whatTime', __name__, template_folder='/templates')
    api = Api(blueprint, add_api_spec_resource=False)
    api.add_resource(timeResource, '/api/users')

    return api
