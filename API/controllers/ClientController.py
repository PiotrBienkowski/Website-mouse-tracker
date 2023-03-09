from flask import Flask, jsonify, request, render_template
import models.ClientModel as ClientModel
import lib

def get_all_clients(db, ClientClass):
    clients_json = jsonify(ClientModel.get_all_clients(ClientClass))
    return clients_json

def create_client(proportion, db, ClientClass):
    unique_hash = lib.get_hash()
    return jsonify(ClientModel.create_client(unique_hash, proportion, db, ClientClass))