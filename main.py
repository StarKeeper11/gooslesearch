import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import *
from google.cloud.firestore_v1.base_query import FieldFilter

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

