from .test2 import app
from flask_pymongo import PyMongo
from bson import json_util

mongo = PyMongo(app, uri="mongodb://localhost:27017/pharmPOS")  # open database instance

@app.route('/user/<string:age>', methods=['GET'])
def home_page(age):
    age = str(30)
    if age:
        users = mongo.db.pP.find({"age": age})
        print(age)
        print(type(users))
        for name in users:
            last = json_util.dumps(name)
        print(last)

        return last

    else:
        return 'No user found!'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

