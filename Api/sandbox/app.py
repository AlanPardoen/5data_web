from flask import Flask
from flask import request
from flask_cors import CORS
import pymongo
import json
from bson import json_util

app = Flask(__name__)
CORS(app)
db_uri = "mongodb+srv://admin:admin@cluster0.8mcxx.mongodb.net/SUPINFO?retryWrites=true&w=majority"
client = pymongo.MongoClient(db_uri)
database = client.SUPINFO
collection = client.SUPINFO.Student


def parse_json(data):
  return json_util.dumps(data, ensure_ascii=False).encode('utf8')

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/data' , methods=['GET'])
def get_data():
  tablename = request.args.get('table', type = str)
  print(tablename)
  return  parse_json(client.SUPINFO[tablename].find())

@app.route('/tables' , methods=['GET'])
def get_tables_name():
  return  json_util.dumps(database.list_collection_names())

@app.route('/campusdata', methods=['GET'])
def get_campus_data():
  campusName = request.args.get('campusname', type=str)
  activestudent = client.SUPINFO.Student.find(
    {"ÉTABLISSEMENT ACTUEL".lower(): "campus de "+campusName.lower(), "SITUATION ACTUELLE".lower(): "continue"})
  activestudent = list(activestudent)
  dilpomstudent = client.SUPINFO.Student.find(
    {"ÉTABLISSEMENT ACTUEL".lower(): "campus de "+campusName.lower(), "SITUATION ACTUELLE".lower(): "fin de scolarité"})
  dilpomstudent = list(dilpomstudent)
  result = "Eleves actifs: {} / Eleves diplomés {} ".format(len(activestudent),len(dilpomstudent))
  return result


@app.route('/growrate', methods=['GET'])
def get_grow_rate():
  campusName = request.args.get('campusname', type=str)
  oldyears = client.SUPINFO.Student.find(
    {"ÉTABLISSEMENT ACTUEL".lower(): "campus de " + campusName.lower(), "ANNÉE D'ADMISSION".lower(): "2010"})
  oldyears = list(oldyears)
  now = client.SUPINFO.Student.find(
    {"ÉTABLISSEMENT ACTUEL".lower(): "campus de " + campusName.lower(), "ANNÉE D'ADMISSION".lower(): "2021"})
  now = list(now)
  thirdyears = client.SUPINFO.Student.find(
    {"ÉTABLISSEMENT ACTUEL".lower(): "campus de " + campusName.lower(), "ANNÉE D'ADMISSION".lower(): "2019"})
  thirdyears = list(thirdyears)
  oldgrowrate = round(((len(now) - len(oldyears)) / len(oldyears)) * 100)
  thirdgrowrate = round(((len(now) - len(thirdyears)) / len(thirdyears)) * 100)
  result = "Croissance sur 10 ans: {}% / Croissance estimé {}% ".format(oldgrowrate, thirdgrowrate)
  return result
