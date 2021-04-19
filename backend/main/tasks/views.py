from flask import Blueprint
from PIL import Image
import base64
import io
from flask import render_template

tasks_blueprints = Blueprint( 'tasks', __name__, template_folder= '/templates' )

with open('/Users/johnlee/Desktop/pharmPOS/backend/main/tasks/imgInbase64.txt','r') as file:
    img_data=file.read()
@tasks_blueprints.route('/imgDecoder', methods=['POST'])
def imgDecoder():
    image = base64.b64decode(str(img_data))
    fileName = 'test.jpeg'
    imagePath = ('./test.jpeg')
    img = Image.open(io.BytesIO(image))
    img.save(imagePath, 'jpeg')
    print('success')
    return render_template('imgDecoder.html')