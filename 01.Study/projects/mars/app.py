from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sunnb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():

    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name' : name_receive,
        'address' : address_receive,
        'size' : size_receive

    }
    db.mars.insert_one(doc)

    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars.find({}, {'_id':False}))
    return jsonify({'orders':order_list})
    # return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

