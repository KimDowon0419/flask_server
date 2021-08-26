import json
import requests
import os
import cv2
import base64
import numpy as np
import glob
from PIL import Image


dir = "C:/Users/user/PycharmProjects/flask_server/"
image_dir= os.path.join(dir,"static/image/")
dir_path = glob.glob(image_dir+'*.*[gG]')


for path_img in dir_path:
    image = cv2.imread(path_img)
    img_str = base64.b64encode(cv2.imencode('.jpg', image)[1]).decode('utf-8')
    img_dict = {'img':img_str}
    img_dict = json.dumps(img_dict)
    headers = {'Content-Type': "application/json"}
    address = "http://127.0.0.1:2432/inference"
    toserver = requests.post(address, data=img_dict, headers=headers)
    img = toserver.json()
    a = img['info']
    b = np.array(a)
    resize_image = cv2.cvtColor(np.uint8(b), cv2.COLOR_BGR2RGB)
    Image.fromarray(resize_image).save(
        "C:/Users/user/PycharmProjects/flask_server/static/resize/" +os.path.basename(path_img) + '.jpg')




