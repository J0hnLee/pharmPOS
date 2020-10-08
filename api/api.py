from flask import Flask
import time
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.splite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)

########################
class Prescription(db.Model):
    # manual table name choice!
    __tablename__='Prescriptions'

    id = db.Column(db.Integer,primary_key=True)
    hospitalName = db.Column(db.Text)
    patientName = db.Column(db.Text)
    patientAge=db.Column(db.Integer)

    def __init__(self,hospitalName, patientName,patientAge):
        self.hospitalName=hospitalName
        self.patientName=patientName
        self.patientAge=patientAge


    def __repr__(self):
        return f"patient {self.patientName} is {self.patientAge} year/s old"




@app.route('/time')
def get_current_time():
    print(time.time())
    print(time.asctime(time.localtime(time.time())))
    return {'time': time.asctime(time.localtime(time.time()))}


if __name__ == '__main__':
    app.run(debug=True)
