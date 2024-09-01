from flask import Blueprint, request, jsonify
from app.models import Task, db
from datetime import datetime

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('tasks',methods = ['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route('/create_tasks',methods = ['POST'])
def create_task():
    data = request.get_json()
    task = Task(
        title = data['title'],
        description = data.get('Description'),
        deadline = datetime.strptime(data['deadline'], '%Y-%m-%d %H:%H:%S'),
        user_id = data['user_id']
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({'message':'Task created successfully'}), 201

@tasks_bp.route('/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    if not task:
        return jsonify({'message':'Task no found'}), 404
    task = Task(
        title = data['title'],
        description = data['description'],
    )
    db.session.commit
    return jsonify({'message':'Task updated successfully'}), 200

@tasks_bp.route('/tasks/<int:task_id>/extend', methods = ['POST'])
def extend_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if task:
        task.extend_deadline(data['days'])
        db.session.commit()
        return jsonify({'message': 'Task deadline extended'}), 200
    return jsonify({'message': 'Task not found'}), 404