from flask_sqlalchemy import SQLAlchemy

from web_api_eval import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }

        
