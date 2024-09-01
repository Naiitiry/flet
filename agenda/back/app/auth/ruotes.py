from flask import Blueprint,request,jsonify
from flask_login import logout_user, login_required
from app.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'],email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message':'User registered successfully'}), 201

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        # Implementar token o sesión
        return jsonify({'message':'Login successful'}), 200
    return jsonify({'message':'Invalid credentials'}), 401

@auth_bp.route('/logout',methods=['GET','POST'])
def logout():
    db.session.close()
    return jsonify({'message':'Logout succesfull'})