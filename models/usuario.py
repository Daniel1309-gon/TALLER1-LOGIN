from flask_login import UserMixin
from db import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable = False)
    password = db.Column(db.String(30), nullable = False)
    is_admin = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, id, username, password, is_admin):
        self.id = id
        self.username = username
        self.password = password
        self.is_admin = is_admin
        
usuario1 = Usuario(1, 'daniel', '123456789', True)
usuario2 = Usuario(2, 'alejandro', '123456789', False)
usuario3 = Usuario(3, 'santiago', '123456789', False)