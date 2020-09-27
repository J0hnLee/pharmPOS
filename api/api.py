from flask import Flask
import time

app = Flask(__name__)


@app.route('/time')
def get_current_time():
    print(time.time())
    return {'time': time.time()}

if __name__ == '__main__':
    app.run(debug=True)