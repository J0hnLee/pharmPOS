import sys
import os
#print(sys.path)
from backend.main.databaseModel.patientModel import Prescription
from backend.main import create_app,db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
prescription = Prescription('kerker1')
db.session.add(prescription)
db.session.commit()
sample1 = Prescription('kerker4')
sample2 = Prescription('kerker3')

print(sample1.id)
print(sample2.id)

db.session.add_all([sample1, sample2])
####
## db.section.add(sample1) ##
## db.section.add(sample2) ##

db.session.commit()

print(sample1.id)
print(sample2.id)

print(db)