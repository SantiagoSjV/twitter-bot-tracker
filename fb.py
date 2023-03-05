import pyrebase

config = {
    "projectId": "twitter-scrt-tracker",
    "appId": "1:494820846559:web:1ea1b3f041c088eae8b26a",
    "storageBucket": "twitter-scrt-tracker.appspot.com",
    "locationId": "us-central",
    "apiKey": "AIzaSyCW5jfc9QZJtCqM2PrK57YDKXwghGQyFis",
    "authDomain": "twitter-scrt-tracker.firebaseapp.com",
    "messagingSenderId": "494820846559",
    "serviceAccount": "./serviceAccount.json",
    "databaseURL": ""
  }

firebase = pyrebase.initialize_app(config)
media_storage = firebase.storage().child("file_name.png")
# media_storage.put("left_behind.png")
media_url = media_storage.get_url(None)
print(media_url)
