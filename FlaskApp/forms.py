from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField
from wtforms_sqlalchemy import fields
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from FlaskApp.models import Post, User, Comment

class PostForm(FlaskForm):
  time_created = DateField
  title = StringField('Post Title',
    validators=[
      DataRequired(),
      Length(min=3, max = 50, message='Your Title needs to be within 3 and 50 characters')
    ])
  description = StringField('Post Description',
    validators=[
      DataRequired()
    ])
  owner = fields.QuerySelectField('Owner', query_factory=lambda: User.query, allow_blank=False)
  submit = SubmitField('Submit')

class LoginForm(FlaskForm):
  username = StringField('Username',
    validators=[
      DataRequired(),
      Length(min=4, max=20, message=None)])
  password = StringField('Password',
    validators=[
    DataRequired(),
    Length(min=4, max=20, message=None)])
  submit = SubmitField('Submit')

class NewUserForm(FlaskForm):
  username = StringField('Username',
    validators=[
      DataRequired(),
      Length(min=4, max=20, message=None)])
  password = StringField('Password',
    validators=[
      DataRequired(),
      Length(min=4, max=20, message=None)])
  email = StringField('Email',
    validators=[
      DataRequired()
    ])
  name = StringField('Name',
    validators=[
      DataRequired()
    ])
  age = IntegerField('Age',
    validators=[
      DataRequired(),
      NumberRange(min=18,max=None,message='Must be above 18 yeard old')
      ])
  profile_bio = StringField('Bio')
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  content = StringField('Comment')
  submit = SubmitField('Submit')