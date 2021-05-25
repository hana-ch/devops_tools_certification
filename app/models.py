from app import DB
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class User(DB.Model):
    """Simple database model to track Users"""
    
    __tablename__ = 'user'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    email = DB.Column(DB.String(120))
    addr = DB.Column(DB.String(120))
    certificate = DB.ForeignKey("certificate.id")

    def __init__(self, name=None, email=None, addr=None):
        self.name = name
        self.email = email
        self.addr = addr

    def __repr__(self):
        return f"{self.name}:{self.id}"

class Certificate(DB.Model):
    """Simple database model to track Users"""
    
    __tablename__ = 'certificate'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"{self.name}:{self.id}"