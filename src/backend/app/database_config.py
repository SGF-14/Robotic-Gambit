# database_config.py
import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase_app():
    # Load your Firebase credentials and initialize the app
    cred = credentials.Certificate('app/robotic-gambit-firebase-adminsdk-qoeq8-0e937ad0f9.json')
    firebase_app = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://robotic-gambit-default-rtdb.europe-west1.firebasedatabase.app/'
    })
    return firebase_app

firebase_app = initialize_firebase_app()
