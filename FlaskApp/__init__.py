from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

from FlaskApp.routes import main

app.register_blueprint(main)

with app.app_context():
  db.create_all()