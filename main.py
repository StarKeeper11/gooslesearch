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

app = firebase_admin.initialize_app(cred)

db = firestore.client()

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

app = Flask(__name__)

@app.route("/getusername", methods=["POST"])
def getUsernameRoute():
    print("running getUsernameRoute")
    data = request.json
    print("data get")
    if not data or 'id' not in data:
        print("error w/ data")
        return jsonify({"status": "error", "username": "..."})

    username = str(data['id'])

    query = getUsername(id)

    if query:
        return jsonify({"status": "success", "username": str(query)})
    else:
        return jsonify({"status": "error", "username": "..."})

    return True

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)