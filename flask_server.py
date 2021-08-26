import numpy as np
import test0713
import cv2
import base64
import os
from flask import Flask, request,render_template,jsonify


UPLOAD_FOLDER = 'C:/Users/user/PycharmProjects/flask_sever'

app = Flask(__name__)
app.secret_key = "secret key"


@app.route('/inference', methods=['POST'])
def inference():
    data = request.json
    data = data['img']
    data = base64.b64decode(data)
    jpg_arr = np.frombuffer(data, dtype=np.uint8)
    img = cv2.imdecode(jpg_arr, cv2.IMREAD_COLOR)
    result = test0713.input(img)
    result2 = result.tolist()
    result3 = {'info': result2}
    return jsonify(result3)



@app.route("/")
def upload_form():
    views = os.listdir('static/resize/')
    views = ['resize/' + file for file in views]
    return render_template("test.html", views= views)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=2432, threaded=False)
