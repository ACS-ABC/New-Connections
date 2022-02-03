from flask import Flask, Blueprint, render_template, request, flash, redirect
from FlaskApp.forms import LoginForm
from FlaskApp.models import Post, User, Comment, Like

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
  return render_template('landing_page.html')

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
def feed(user_id):
  user = User.query.get(user_id)
  posts = Post.query.all()
  return render_template('feed.html', posts=posts, user=user)

@main.route('/create-post/<user_id>', methods = ['GET', 'POST'])
def create(user_id):
  user = User.query.get(user_id)
  if request.method == 'POST':
    pass
  else: 
    return render_template('create_post.html')