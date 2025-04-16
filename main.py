import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import *
from google.cloud.firestore_v1.base_query import FieldFilter
from flask import *
from flask_cors import CORS

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
    return True
print(getUsername(1))