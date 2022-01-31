from flask import Flask, Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home_page():
  """Return homepage."""
  return render_template('home_index.html')