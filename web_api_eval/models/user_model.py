from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from web_api_eval import db

def create_user_model(tenant_id):
    class User(db.Model):
    
        __tablename__= f'user_{tenant_id}'
        __table_args__ = {'extend_existing': True}
        
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=False, nullable=False)
        password = db.Column(db.String(120),nullable=False)
        
        def serialize(self):
            return {
                "id": self.id,
                "username": self.username
        }
    with current_app.app_context():
        db.create_all()
    return User


        
