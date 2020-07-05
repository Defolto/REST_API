from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pymongo import MongoClient
import json
import webbrowser

client = MongoClient("mongodb+srv://test:952863mak@cluster0-ainc3.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.get_database("student_db")
records = db.student_records

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
def main_page():
    list1 = list(records.find({}, {"_id": 0}))
    return jsonify(list1)

@app.route("/login", methods=['POST'])
def login():
    # user = {
    #     "name": request.form['user_name'],
    #     "password": request.form['user_password']
    # }
    # records.insert_one(user)
    newData = request.json
    # print (newData.get("user_name"))
    akk = records.find_one({"name": newData.get("user_name"), "password": newData.get("user_password")}, {"_id": 0, "info": 1})
    if akk:
       pass
    else:
        akk = "Пользователь не найден"
    return jsonify(akk)

