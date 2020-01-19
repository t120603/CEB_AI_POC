import flask
from flask import request, jsonify
from PIL import Image
import io
import requests
import os
import numpy as np

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Is this baby sleeping safely?</h1>
<p>navigate to /api/v1/is_baby_safe_yolo to test</p>
<p>Back example: https://www.todaysparent.com/wp-content/uploads/2017/01/tips-for-getting-baby-to-sleep-in-crib-during-naptime.jpg</p>
<p>Stomach example: https://imgix.bustle.com/uploads/image/2018/4/19/0db9d02e-8e7c-4248-8018-ea9df95ea74a-fotolia_189864845_subscription_monthly_m.jpg?w=960&h=540&fit=crop&crop=faces&auto=format&q=70</p>'''


@app.route('/api/v1/is_baby_safe', methods=['GET'])
def api_id():
    # Check if baby_url is present on request arguments
    if 'baby_url' in request.args:
        results = classify_baby(request.args['baby_url'])
    else:
        return "Error: No baby image url provided. Please provide it with '?baby_url=<url>'"

    return jsonify(results)


@app.route('/api/v1/is_baby_safe_yolo', methods=['GET'])
def api_baby_safe_yolo():
    # Check if baby_url is present on request arguments
    if 'baby_url' in request.args:
        results = classify_baby_yolo(request.args['baby_url'])
    else:
        return "Error: No baby image url provided. Please provide it with '?baby_url=<url>'"

    return jsonify(results)

def classify_baby_yolo(baby_url):
    
    img_data = requests.get(baby_url).content
    image = Image.open(io.BytesIO(img_data))
    print('image loaded!', image.size)
    
    from keras_yolo3.yolo import YOLO
    yolo_obj = YOLO()
    print('YOLO loaded!')
    image_post_yolo, result = yolo_obj.detect_image(image)
    print('YOLO applied!', result)
    print(result[0])
    #result[0].show()

    '''imgs = []
    for obj in result[1]:
        if obj['predicted_class'] == 'person' and obj['score']>0.33:
            border = tuple(obj['box']) # left, up, right, bottom
            img_cropped = image.crop(border)
            imgs.append(img_cropped)
    print('Babies found: ',len(imgs))'''
    import keras
    keras.backend.clear_session()
    return result

app.run()