import time
from flask import Blueprint, request
from flask_restful_swagger_2 import Api, swagger, Resource
from ..views import model
from flask_jwt import jwt_required
nameList = []


class userInfo(Resource):
    @swagger.doc({'tags': ['users'], 'description': 'Adds a user', 'parameters': [
        {'name': 'body', 'description': 'Request body', 'in': 'body', 'schema': model.UserModel, 'required': True, }],
                  'responses': {'201': {'description': 'Created user', 'schema': model.UserModel, 'headers': {
                      'Location': {'type': 'string', 'description': 'Location of the new item'}},
                                        'examples': {'application/json': {'id': 1}}}}})
    @jwt_required()
    def get(self, name):
        oneName = next(filter(lambda x: x['name'] == name, nameList), None)
        return {"name": oneName}, 200 if oneName else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, nameList), None):
            return {'message': "An item with name '{}' already.".format(name)}, 400
        # data = request.get_json()
        # item = {'name': name, 'price': data['price']}
        item = {'name': name}
        nameList.append(item)
        return item, 201

    def delete(self, name):
        nameList.pop(0)
        return nameList


def get_user_resources():
    """
    Returns user resources.
    :param app: The Flask instance
    :return: User resources
    """
    blueprint = Blueprint('userInfo', __name__, template_folder='/templates')
    api = Api(blueprint, add_api_spec_resource=False)
    api.add_resource(userInfo, '/api/users/<string:name>')

    return api
