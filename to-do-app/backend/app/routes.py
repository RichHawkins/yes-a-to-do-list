from flask import Blueprint, render_template
from .model import User, TodoItem
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    todos = TodoItem.query.all()
    return render_template('index.html', todos=todos)