from flask import Flask, Blueprint, render_template, request, flash, redirect
from FlaskApp.forms import LoginForm, SignUpForm
from FlaskApp.models import Post, User, Comment, Like
from FlaskApp import db
main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
  return render_template('landing_page.html')

@main.route('/sign-up', methods = ['GET', 'POST'])
def sign_up_page():
  form = SignUpForm()
  if form.validate_on_submit():
    new_user = User(
      username = form.username,
      password = form.password,
      email = form.email,
      name = form.name,
      age = form.age
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect(f'/account-profile/{new_user.id}')
    
  return render_template('login_page.html', form=form)

@main.route('/login', methods = ['GET', 'POST'])
def login_page():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username)
    if user:
      if user.password == form.password:
        user = user
        return redirect(f'/feed/{user.id}')
      else:
        flash('username or password invalid')
    pass
  else: 
    return render_template('login_page.html', form=form)

@main.route('/feed/<user_id>')
def display_feed(user_id):
  user = User.query.get(user_id)
  posts = Post.query.all()
  return render_template('feed.html', posts=posts, user=user)

@main.route('/create-post/<user_id>', methods = ['GET', 'POST'])
def create_post(user_id):
  user = User.query.get(user_id)
  if request.method == 'POST':
    pass
  else: 
    return render_template('create_post.html')

@main.route('/account-profile/<user_id>')
def account_profile(user_id):
  user = User.query.get(user_id)
  #ask christian on how to display edit vs noraml display
  return render_template('account_profile.html', user=user)