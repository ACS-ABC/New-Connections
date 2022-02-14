from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from sqlalchemy import create_engine
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = os.urandom(24)

migrate = Migrate(compare_type=True)

db = SQLAlchemy()
uri = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
print(uri)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(db, app)


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
from FlaskApp.models import User

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)



from FlaskApp.routes import main

app.register_blueprint(main)

with app.app_context():
  db.create_all()