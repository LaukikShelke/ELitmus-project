from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import Binary
from bson.json_util import dumps
from base64 import encodebytes
from flask_cors import CORS
CLIENT = MongoClient("mongodb://localhost:27017/")
db = CLIENT["Invigilation"]
user_coll = db["Users"]
image_coll = db["Images"]


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({'msg': "Server conencted!"})
@app.route("/captures", methods=["POST"])
def captures():
    
    image_coll.insert_one(request.json)
    return jsonify({"msg": "Succeeded"})

@app.route("/images/<userid>", methods=["GET"])
def send_images(userid):
    images = image_coll.find({})
    imgs = []
    for image in images:
        imgs.append(image)
    print(imgs)
    return jsonify({"msg": imgs})
    

if __name__ == "__main__":
    app.run(debug=True)