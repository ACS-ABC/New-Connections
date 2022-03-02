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
print(uri)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DATABASE_URL = uri

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

db.init_app(app)
migrate.init_app(db, app)

from FlaskApp.routes import main

app.register_blueprint(main)

