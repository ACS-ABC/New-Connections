from flask import Flask, Blueprint, render_template, request, flash
from models import Post, User, Comment, Like

main = Blueprint('main', __name__)

@main.route('/')
def home_page():
  """Return homepage."""
  return render_template('home_index.html')

@main.route('/feed/<user_id>')
def feed(user_id):
  user = User.query.get(user_id)
  posts = Post.query.all()
  return render_template('feed.html', posts=posts, user=user)

@main.route('/create-post/<user_id>', methods = ['GET', 'POST'])
def create(user_id):
  if request.method == 'POST':
    pass
  else: 
    return render_template('create_post.html')