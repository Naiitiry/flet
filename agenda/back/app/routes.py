from flask import Flask, Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Task

home_bp = Blueprint('home',__name__)

# Inicio de la aplicación, con requerimiento de inicio de sesión
@home_bp.route('/', methods=['GET'])
@login_required
def home():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.title).limit(10).all()
    return jsonify([{
        'id':task.id,
        'title':task.title,
        'description':task.description,
        'creation':task.creation_date.isoformat(),
        'deadline':task.deadline.isoformat(),
        'completed':task.completed,
        'user':task.user_id
    } for task in tasks]), 200