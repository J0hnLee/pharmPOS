from api import db, Prescription
#can be delete
##CREATE##
prescription = Prescription('亞東','kerker1','25')
db.session.add(prescription)
db.session.commit()

##READ##
all_prescription=Prescription.query.all() # list of prescriptions objects in the talbe.
print(all_prescription)

##SELECT BY ID##
prescriptionOne=Prescription.query.get(1)
print(prescriptionOne.patientName)

#FILTERS
#PRODUCE SOME SQL CODE
sampleOne=Prescription.query.filter_by(patientAge=25)
print(sampleOne.all())


####UPDATE
firstSample= Prescription.query.get(1)
firstSample.age=10
db.session.add(firstSample)
db.session.commit()


###DELETE
secondSample=Prescription.query.get(2)
db.session.delete(secondSample)
db.session.commit()