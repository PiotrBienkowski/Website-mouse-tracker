import lib

def get_all_clients(ClientClass):
    clients = ClientClass.query.all()
    tab = []
    for client in clients:
        tmp = {
            "client_id": client.id,
            "unique_hash": client.unique_hash,
            "proportion": client.proportion,
            "timestamp": lib.get_timestamp()
        }
        tab.append(tmp)
    return tab

def create_client(unique_hash, proportion, db, ClientClass):
    new_client = ClientClass(
        unique_hash = unique_hash,
        proportion = proportion,
    )

    try:
        db.session.add(new_client)
        db.session.commit()
        return {
            "status": True, 
            "info": "User created.",
            "hash": unique_hash,
            "timestamp": lib.get_timestamp()
        }
    except Exception as e:
        db.session.rollback()
        return {
            "status": False,
            "error":  str(e)
        }


