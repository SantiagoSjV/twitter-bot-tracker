import pyrebase

config = {
    "projectId": "twitter-media-tracker",
    "appId": "1:254806048411:web:fe6750e8ed5bfdeb07903e",
    "databaseURL": "https://twitter-media-tracker-default-rtdb.firebaseio.com",
    "storageBucket": "twitter-media-tracker.appspot.com",
    "apiKey": "AIzaSyCoK5AVMvTiGc9Aae3LLxlHYmUh1pxRmMw",
    "authDomain": "twitter-media-tracker.firebaseapp.com",
    "messagingSenderId": "254806048411",
    "serviceAccount": "./serviceAccount.json",
    "databaseURL": "https://twitter-media-tracker-default-rtdb.firebaseio.com/"
  }

app = pyrebase.initialize_app(config)
db = app.database()