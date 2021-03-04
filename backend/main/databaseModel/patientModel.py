from .. import db

######################################
class Prescription(db.Model):
    # define the database model
    __tablename__ = 'Prescriptions'
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(255), unique=True, nullable=False)
    # registered_on = db.Column(db.DateTime, nullable=False)
    # admin = db.Column(db.Boolean, nullable=False, default=False)
    # public_id = db.Column(db.String(100), unique=True)
    patientName = db.Column(db.Text)
    #password_hash = db.Column(db.String(100))
    #hospitalName = db.Column(db.Text)
    #patientAge = db.Column(db.Integer)

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



    def __init__(self,ID,patientName):
        #self.hospitalName = hospitalName
        #
        self.patientName = patientName
        self.id=ID
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