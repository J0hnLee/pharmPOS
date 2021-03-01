from flask_restful_swagger_2 import Schema
## add parameters to specify all fields in spec document
class UserModel(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'integer',
            'format': 'int64',
        },
        'name': {
            'type': 'string'
        },

    }
    required = ['name']