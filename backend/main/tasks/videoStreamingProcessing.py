import cv2
from flask import Flask, render_template, Response
import os
app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('videos.html')


def gen():
    """Video streaming generator function."""
    print(os.getcwd())
    img = cv2.imread("./backend/main/tasks/supportFiles/lizerd.jpg")
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    frame = cv2.imencode('.jpg', img)[1].tobytes()
    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':

    app.run(debug=True)