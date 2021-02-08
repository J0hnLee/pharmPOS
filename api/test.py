from flask import Flask
import time
import os

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    print(time.time())
    print(time.asctime(time.localtime(time.time())))
    return {'time': time.asctime(time.localtime(time.time()))}


if __name__ == '__main__':
    app.run(debug=True)
