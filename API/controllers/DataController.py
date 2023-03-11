from flask import jsonify
import models.DataModel as DataModel
import lib

def get_all_datas(db, DataClass):
    users_json = jsonify(DataModel.get_all_datas(DataClass))
    return users_json

def add_datas(data, db, DataClass):
    token = data.get("token", "-")
    data_list = data.get("list")
    success = 0
    for item in data_list:
        tmp = DataModel.add_data(token, float(item.get("x")), float(item.get("y")), db, DataClass)
        if tmp.get("status"):
            success += 1
    return {
        "success": success,
        "failure": len(data_list) - success,
        "timestamp": lib.get_timestamp()
    }