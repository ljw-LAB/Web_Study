from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sunnb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    # return jsonify({'msg': 'POST 연결 완료!'})

    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name' :name_receive,
        'comment': comment_receive
    }
    db.homework.insert_one(doc)

    return jsonify({'msg': 'POST 연결 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    homework_list = list(db.homework.find({}, {'_id':False}))
    return jsonify({'homeworks':homework_list})
    # return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
