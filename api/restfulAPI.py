import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.splite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

db.create_all()

######################################
class Prescription(db.Model):
    # manual table name choice!
    __tablename__ = 'Prescriptions'
    id = db.Column(db.Integer, primary_key=True)
    #hospitalName = db.Column(db.Text)
    patientName = db.Column(db.Text)
    #patientAge = db.Column(db.Integer)

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
    def get(self):
        pts = Prescription.query.all()
        return [pt.json() for pt in pts]


api.add_resource(patientNames, '/<string:pName>')
api.add_resource(AllName, '/pts')

if __name__ == '__main__':
    app.run(debug=True)