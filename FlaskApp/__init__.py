from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
import psycopg2



app = Flask(__name__)
app.secret_key = os.urandom(24)



migrate = Migrate(compare_type=True)

db = SQLAlchemy()
uri = os.environ.get('DATABASE_URI')

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


conn = psycopg2.connect(
  dbname='d4n6hcaulpeumg',
  user='xlgcwbjezjifrp',
  password='8bded6d11509b4cde65f4213be50750c694e589f6fdead71852831417761f26c',
  host='ec2-54-156-110-139.compute-1.amazonaws.com',
  sslmode='require')

db.init_app(app)

migrate.init_app(db, app)

from FlaskApp.routes import main

app.register_blueprint(main)

