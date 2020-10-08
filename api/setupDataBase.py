from api import db, Prescription


# CREATES ALL THE TABLES Model--> Db table
db.create_all()

sample1=Prescription('亞東','kerker1','25')
sample2=Prescription('亞東','kerker3','52')

print(sample1.id)
print(sample2.id)

db.session.add_all([sample1,sample2])
####
## db.section.add(sample1) ##
## db.section.add(sample2) ##

db.session.commit()

print(sample1.id)
print(sample2.id)