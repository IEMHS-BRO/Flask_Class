from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

bp = Blueprint('auth', __name__, url_prefix='/auth')

'''
로그인
'''
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.verify_password(data['password']):
        return jsonify({'msg': 'Invalid username or password'}), 401
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=30))
    return jsonify(access_token=access_token), 200


'''
회원가입
'''
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], name=data['name'], phone=data['phone'])
    new_user.hash_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'msg': 'User created successfully'}), 201


'''
자동 로그인
'''
@bp.route('/auto-login', methods=['POST'])
@jwt_required()
def auto_login():
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id, expires_delta=timedelta(minutes=30))
    return jsonify(access_token=access_token), 200

#TODO: 로그아웃을 없앴습니다.

'''
사용자 정보 획득
'''
@bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_info():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(user.to_json()), 200