from fastai import *
from fastai.vision import *
import fastai

from io import BytesIO
from typing import List,Dict, Union, ByteString

import flask
from flask import Flask
import requests
import torch

#fastai.defaults.device = torch.device('cpu')

app = Flask(__name__)


def load_model(classes:List[str] , path="data" ,model_name="final"
               , architecture= models.resnet34
               , image_size=224)->ClassificationLearner:

    data = ImageDataBunch.single_from_classes(path, classes
                                           , tfms=get_transforms()
                                           ,size=image_size).normalize(imagenet_stats)
    learn = create_cnn(data, architecture)
    learn.load(model_name)
    return learn

def load_image_url(url:str)->Image:
    response = requests.get(url)
    img = open_image(BytesIO(response.content))
    return img


def load_image_bytes(raw_bytes:ByteString)->Image:
    img = open_image(BytesIO(raw_bytes))
    return img



def predict(img)->List[Dict]:
    pred_class,pred_idx,losses = model.predict(img)
    payload = []
    for image_class, loss in zip (model.data.classes, losses.tolist()):
        payload.append(
            {"class":image_class, "loss":loss}
        )
    
    return payload

@app.route('/classify', methods=['POST','GET'])
def upload_file():
    if flask.request.method == 'GET':
        url = flask.request.args.get("url")
        img = load_image_url(url)
    else:
        bytes = flask.request.files['image'].read()
        img = load_image_bytes(bytes)
    predictions = predict(img)
    return flask.jsonify(predictions=predictions)    

@app.route('/')
def index():
    return flask.render_template('pretty.html')


CLASSES = sorted(["grizzly bear", "teddy bear", "black bear"])
model = load_model(CLASSES)


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
    
    
    