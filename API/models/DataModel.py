import lib

def get_all_datas(DataClass):
    datas = DataClass.query.all()
    tab = []
    for data in datas:
        tmp = {
            "data_id": data.id,
            "x": data.x,
            "y": data.y,
            "token": data.token,
            "timestamp": lib.get_timestamp()
        }
        tab.append(tmp)
    return tab

def add_data(token, x, y, db, DataClass):
    new_data = DataClass(
        token = token,
        x = x,
        y = y
    )

    try:
        db.session.add(new_data)
        db.session.commit()
        return {
            "status": True, 
            "info": "Data added.",
            "timestamp": lib.get_timestamp()
        }
    except Exception as e:
        db.session.rollback()
        return {
            "status": False,
            "error":  str(e),
            "timestamp": lib.get_timestamp()
        }

def get_data(token, db, DataClass):
    data = DataClass.query.filter_by(token=token).all()
    return data