from flask_sqlalchemy import SQLAlchemy  
from . import app

db= SQLAlchemy(app)
  
class Call(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(80), nullable=False)  
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Bool,nullable=False)
    

db.create_all()  