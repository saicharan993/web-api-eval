from flask_sqlalchemy import SQLAlchemy

from web_api_eval import db


class Tenant(db.Model):
    __tablename__ = 'tenants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(100), nullable=False)
