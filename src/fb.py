import pyrebase
import json

with open('.config.json') as f:
  config = json.load(f)
  app = pyrebase.initialize_app(config)
  db = app.database()