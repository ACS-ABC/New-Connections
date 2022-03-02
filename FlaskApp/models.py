from FlaskApp import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=True)
  name = db.Column(db.String, nullable=True)
  age = db.Column(db.String, nullable=True)
  profile_bio = db.Column(db.String, nullable=True)
  # location = db.Column()
  profile_picture = db.Column(db.String, nullable=True)
  #make a table that fxns like genres for user_interests 
  
  def __str__(self):
    self.username
    return

  def __repr__(self):
    self.id
    return

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  time_created = db.Column(db.DateTime)
  # #category
  title = db.Column(db.String, nullable=False)
  description = db.Column(db.String, nullable=False)
  owner = db.Column(db.Integer, db.ForeignKey('user.id'))
  author = db.Column(db.String, nullable=False)
  likes = db.Column(db.Integer, db.ForeignKey('like.id'))
  image = db.Column(db.String, nullable=True)
  def __str__(self):
    return

  def __repr__(self):
    return

class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String, nullable=False)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
  def __str__(self):
    return

  def __repr__(self):
    return

class Like(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  liker = db.Column(db.Integer, db.ForeignKey('user.id'))
  post = db.Column(db.Integer, db.ForeignKey('post.id'))
  def __str__(self):
    return

  def __repr__(self):
    return
    