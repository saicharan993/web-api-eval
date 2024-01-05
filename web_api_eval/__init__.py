from flask import Flask, g
import os
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CreateSchema
from web_api_eval.config import prod_config,dev_config
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

print(os.getenv("ENV"))

if os.getenv("ENV")=="DEV":
    env_config = dev_config.dev_config()
if os.getenv("ENV")=="PROD":
    env_config = prod_config.prod_config()

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.sqlite')
db = SQLAlchemy(app)

default_token= prod_config.prod_config().AUTHTOKEN


#Blue print regiester routes

from web_api_eval.api.v1.routes import api_1 as api_v1
from web_api_eval.api.v2.routes import api_2 as api_v2
from web_api_eval.api.health_check.routes import health_check
from web_api_eval.api.tenant.routes import tenant
app.register_blueprint(api_v1, url_prefix='/<string:tenant_name>/api/v1')
app.register_blueprint(api_v2, url_prefix='/api/v2')
app.register_blueprint(health_check)
app.register_blueprint(tenant)

from web_api_eval.models.user_model import create_user_model
from web_api_eval.models.tenants_model import Tenant

with app.app_context():
    db.create_all()




