# from flask_restful_swagger_2 import swagger, Resource
# #from ..  import Prescription
#
# class groupRouce(Resource):
#     @swagger.doc({'tags': ['users'],
#                   'description': 'Adds a user',
#                   'parameters': [
#         {
#             'name': 'body',
#             'description': 'Request body',
#             'in': 'body', 'schema': 'UserModel',
#             'required': True,
#         }
#                   ],
#         'responses': {
#                           '201': {'description': 'Created user', 'schema': 'UserModel',
#             'headers': {'Location': {'type': 'string', 'description': 'Location of the new item'}},
#             'examples': {'application/json': {'id': 1}}}}})
#
#     def get(self):
#         pts = Prescription.query.all()
#         return [pt.json() for pt in pts]
