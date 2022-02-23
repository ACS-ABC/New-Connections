from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from pyuploadcare import conf

app = Flask(__name__)
app.secret_key = os.urandom(24)
conf.pub_key = 'mypublicley'
conf.secret = os.environ.get('UPLOAD_CARE_SECRET')


migrate = Migrate(compare_type=True)

db = SQLAlchemy()
uri = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
print(uri)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(db, app)






from FlaskApp.routes import main

app.register_blueprint(main)

with app.app_context():
  db.create_all()