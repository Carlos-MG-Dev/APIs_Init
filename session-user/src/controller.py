from src.models import User
from src import db


def create_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    
    if not username: return {'message': 'username undefined'}
    if not email: return {'message': 'email undefined'}
    if not password: return {'message': 'password undefined'}
    
    user = User.query.filter_by(username=username).all()
    if user: return {'message': 'nombre de usuario en uso'}
    user = User.query.filter_by(email=email).all()
    if user: return {'message': 'correo en uso'}
    
    user = User(username=username, email=email, password=password)
    
    db.session.add(user)
    db.session.commit()
    
    return {'message':'OK'}
    
    
    