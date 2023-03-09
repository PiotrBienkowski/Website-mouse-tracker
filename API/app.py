# to run
# export FLASK_APP=app.py
# flask run

import lib
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

import controllers.ClientController as ClientController
import controllers.DataController as DataController

app = Flask(__name__)
CORS(app)
api = Api(app)

DEBUG = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_hash = db.Column(db.String(100), nullable=False)
    proportion = db.Column(db.Float, nullable=False)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100), nullable=False)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)

@app.route('/create-db', methods=['GET'])
def create_db():
    lib.create_database(db)
    return "ok"

# ----CLIENT----
@app.route('/all-clients', methods=['GET'])
def all_clients():
    if DEBUG:
        return ClientController.get_all_clients(db, Client)
    else:
        return lib.access_denied;

@app.route('/create-client', methods=['GET'])
def create_client():
    proportion = 2
    return ClientController.create_client(proportion, db, Client)
    
# ----DATA----
@app.route('/all-datas', methods=['GET'])
def all_datas():
    if DEBUG:
        return DataController.get_all_datas(db, Data)
    else:
        return lib.access_denied;

@app.route('/add-data', methods=['POST'])
def add_data():
    data = request.get_json()
    return DataController.add_datas(data, db, Data)