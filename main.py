import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("geeslesearch-firebase-adminsdk-fbsvc-786f71926e.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

user_ref = db.collection("users")
user_ref.document("StarKeeper").set({"id": 0, "linkid": 0, "karma": 100})

search_ref = db.collection("searches")
search_ref.document("minecraft").set({"url": "https://www.minecraft.net/", "visits": 0, "author": "StarKeeper"})