from flask import Flask
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS
import flask_monitoringdashboard as dashboard
from .main.tasks.views import tasks_blueprints
from .main.tasks.userInfo import get_time_resources
from flask_restful_swagger_2 import swagger, get_swagger_blueprint


app = Flask(__name__, template_folder='../templates')
CORS(app)
dashboard.bind(app)
app.config['DEBUG'] = True  # open debug mode

def auth(api_key, endpoint, method):
    # Space for your fancy authentication. Return True if access is granted, otherwise False
    return True
swagger.auth = auth

docs=[]
# Get time resources
user_resources = get_time_resources()
# Retrieve and save the swagger document object (do this for each set of resources).
docs.append(user_resources.get_swagger_doc())

# Register the blueprint for user resources
app.register_blueprint(user_resources.blueprint,url_prefix='/pages')

# Prepare a blueprint to server the combined list of swagger document objects and register it
app.register_blueprint(get_swagger_blueprint(docs, '/api/swagger', title='Example', api_version='1'))

# using blueprint to add different page
app.register_blueprint(tasks_blueprints, url_prefix='/tasks')
#app.register_blueprint(whatTime,url_prefix='/pages')
mongo = PyMongo(app, uri="mongodb://localhost:27017/pharmPOS")  # open database instance


# @app.route('/user/<string:age>', methods=['GET'])
# def home_page(age):
#     age = str(30)
#     if age:
#         users = mongo.db.pP.find({"age": age})
#         print(age)
#         print(type(users))
#         for name in users:
#             last = json_util.dumps(name)
#         print(last)
#
#         return last
#
#     else:
#         return 'No user found!'

@app.route('/')
def new_page():
    return """<head>
    <meta http-equiv="refresh" content="0; url=http://petstore.swagger.io/?url=http://localhost:5000/api/swagger.json" />
    </head>"""



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
