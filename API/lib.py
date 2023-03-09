import time
import secrets
from flask import jsonify

def get_hash():
    random_hash = secrets.token_hex(16)
    return random_hash

def create_database(db):
    db.create_all()

def get_timestamp():
    return int(time.time())

def access_denied():
    return jsonify("Access denied.")