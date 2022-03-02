from flask import Flask, Blueprint, render_template, request, flash, redirect
from flask_login import LoginManager
from FlaskApp.forms import CommentForm, LoginForm, PostForm, SignUpForm, EditAccountForm
from FlaskApp.models import Post, User, Comment, Like
from flask_login import current_user, login_required, login_user, logout_user
from FlaskApp import db, app

main = Blueprint('main', __name__)
login_manager = LoginManager()
login_manager.login_view = 'main.login_page'
login_manager.init_app(app)

# with app.app_context():
#   db.create_all()

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)
@main.route('/')
def landing_page():
  return render_template('landing_page.html')

@main.route('/sign-up', methods = ['GET', 'POST'])
def sign_up_page():
  form = SignUpForm()
  if form.validate_on_submit():
    new_user = User(
      username = form.username.data,
      password = form.password.data,
      email = 'None',
      name = 'None',
      age = 18
    )
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return redirect(f'/account-profile/{new_user.id}')
  return render_template('sign_up_page.html', form=form)

@main.route('/login', methods = ['GET', 'POST'])
def login_page():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user:
      if user.password == form.password.data: 
        login_user(user)
        return redirect(f'/feed/{user.id}')
      else:
        flash('Password doesn\'t match. Please try again.') 
    else:
      flash('No user with that username. Please try again.')
  return render_template('login_page.html', form=form)

@main.route('/feed/<user_id>', methods = ['GET', 'POST'])
@login_required
def display_feed(user_id):
  user = current_user
  posts = Post.query.all()
  # comments = Comment.query.all()
  form = CommentForm()
  # if form.validate_on_submit():
  #   new_comment = Comment(
  #     content = form.content.data,
  #     author_id = user_id,
  #     post_id = form.post.data
  #   )
  #   db.session.add(new_comment)
  #   db.session.commit()

  #   return render_template('feed.html', posts=posts, user=user, form=form, comments=comments)
  return render_template('feed.html', posts=posts, user=user, form=form)

@main.route('/create-post/<user_id>', methods = ['GET', 'POST'])
@login_required
def create_post(user_id):
  form = PostForm()
  if form.is_submitted():
    author = User.query.get(user_id).username
    new_post = Post(
      time_created = form.time.data,
      title = form.title.data,
      description = form.description.data,
      owner = user_id,
      author = author
    )
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/feed/{user_id}')
   
  return render_template('create_post.html', form=form, user=current_user)

@main.route('/account-profile/<user_id>')
@login_required
def account_profile(user_id):
  user_profile = User.query.get(user_id)
  posts = Post.query.filter_by(owner=user_id)
  return render_template('account_profile.html', user=current_user, posts=posts, profile=user_profile)

@main.route('/account-profile/<user_id>/edit', methods = ['GET', 'POST'])
@login_required
def edit_profile(user_id):
  user = current_user
  form = EditAccountForm(obj=user)
  if form.validate_on_submit():
    user.username = form.username.data
    user.name = form.name.data
    user.profile_bio = form.profile_bio.data
    return redirect(f'/account-profile.html/{user_id}')
  return render_template('edit_profile.html', user=user, form=form)

@main.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect('/')