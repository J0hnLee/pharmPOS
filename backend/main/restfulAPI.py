import os
from flask import Flask,Blueprint
from flask_restful_swagger_2 import Api
from flask_sqlalchemy import SQLAlchemy
from flask_restful_swagger_2 import swagger, Resource
from flask_cors import CORS


## import self-api function
from .views.databaseInit import Prescription
from .views.getTime import whatTime
from .views.model import UserModel
#from .views.groupResource import  GroupResource

import flask_bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

def auth(api_key, endpoint, method):
    # Space for your fancy authentication. Return True if access is granted, otherwise False
    return True
swagger.auth = auth

app.register_blueprint(whatTime,url_prefix='/pages')
api = Api(app,
    host="localhost:5000",
    schemes=['http'],
   # schemes=['https'],
   # base_path='/dev',
    security_definitions='security',
    security=[{'appKey': []}],
    api_version='0.01',
    api_spec_url='/api/swagger')

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.splite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
db.create_all()



######################################
class Prescription(db.Model):
    # define the database model
    __tablename__ = 'Prescriptions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # email = db.Column(db.String(255), unique=True, nullable=False)
    # registered_on = db.Column(db.DateTime, nullable=False)
    # admin = db.Column(db.Boolean, nullable=False, default=False)
    # public_id = db.Column(db.String(100), unique=True)
    patientName = db.Column(db.Text, unique=True)
    #password_hash = db.Column(db.String(100))
    # hospitalName = db.Column(db.Text)
    # patientAge = db.Column(db.Integer)

    # @property
    # def password(self):
    #     raise AttributeError('password: write-only field')
    #
    # @password.setter
    # def password(self, password):
    #     self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    #
    # def check_password(self, password):
    #     return flask_bcrypt.check_password_hash(self.password_hash, password)
    #
    # def __repr__(self):
    #     return "<User '{}'>".format(self.patientName)



    def __init__(self, patientName):
        #self.hospitalName = hospitalName
        self.patientName = patientName
        #self.patientAge = patientAge

    # def __init__(self, hospitalName, patientName, patientAge):
    #     self.hospitalName = hospitalName
    #     self.patientName = patientName
    #     self.patientAge = patientAge

    # def json(self):
    #     return {'Hospital': self.hospitalName, 'PatientName': self.patientName, 'Age': self.patientAge}
    #
    def json(self):
        return {'PatientName': self.patientName}


    # def __repr__(self):
    #     return f"patient {self.patientName} is {self.patientAge} year/s old"


#####################################

class patientNames(Resource):
    def get(self,pName):
        pt = Prescription.query.filter_by(patientName=pName).first()
        if pt:
            return pt.json()
        else:
            return {'name': None}, 404

    def post(self,pName):
        prescription = Prescription(pName)
        db.session.add(prescription)
        db.session.commit()
        return prescription.json()

    def delete(self,pName):
        secondSample = Prescription.query.filter_by(patientName=pName).first()
        db.session.delete(secondSample)
        db.session.commit()
        return {'note': 'delete success'}






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

api.add_resource(patientNames, '/<string:pName>')
api.add_resource(AllName, '/pts')

if __name__ == '__main__':

    app.run(debug=True)