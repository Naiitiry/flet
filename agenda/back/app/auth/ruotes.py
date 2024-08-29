from flask import Blueprint,request,jsonify
from app.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'],email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message':'User registered successfully'}), 201

@auth_bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        # Implementar token o sesión
        return jsonify({'message':'Login successful'}), 200
    return jsonify({'message':'Invalid credentials'}), 401

@auth_bp.route('/logout')
def logout():
    db.session.pop('logged_in', None)
    db.session.pop('username', None)
    return jsonify({'message': 'Logout successful'}), 200