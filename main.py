import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import *
from google.cloud.firestore_v1.base_query import FieldFilter
from flask import *
from flask_cors import CORS
import json

# Use a service account.
cred = credentials.Certificate('service-account.json')

fireapp = firebase_admin.initialize_app(cred)

db = firestore.client()

flaskapp = Flask(__name__)
CORS(flaskapp)

user_ref = db.collection('users')

def doesUserExist(username):
    query = user_ref.where(filter=FieldFilter('username', '==', username)).stream()
    for doc in query:
        return True
    return False

def getUsername(id):
    query = user_ref.document(str(id))
    if query.get().exists:
        return query.get().to_dict()['username']
    else:
        return None

@flaskapp.route("/getusername", methods=["POST"])
def getUsernameRoute():
    print("running getUsernameRoute")
    data = request.json
    print("data get")
    if not data or 'id' not in data:
        print("error w/ data")
        return jsonify({"status": "error", "username": "..."})

    id = str(data['id'])
    print(id)

    query = getUsername(id)
    print(query)

    if query:
        return jsonify({"status": "success", "username": str(query)})
    else:
        return jsonify({"status": "error", "username": "..."})

if __name__ == "__main__":
    flaskapp.run(port="4321")
    print("running")