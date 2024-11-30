from flask import Blueprint, render_template
from .model import ToDoItem

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    todos = ToDoItem.query.all()
    return render_template('index.html', todos=todos)