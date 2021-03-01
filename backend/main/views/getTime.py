from flask import Blueprint
import time
import os
whatTime = Blueprint('whatTime', __name__)

@whatTime.route('/time')
def get_current_time():
    print(time.time())
    print(time.asctime(time.localtime(time.time())))
    return {'time': time.asctime(time.localtime(time.time()))}


