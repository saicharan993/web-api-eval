from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
from web_api_eval.config import prod_config

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "AUTHTOKEN" in request.headers:
            token = request.headers["AUTHTOKEN"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "error": "Unauthorized"
            }, 401
        try:
            if token!= prod_config.prod_config().AUTHTOKEN:
                return {
                "message": "Invalid Authentication token!",
                "error": "Unauthorized"
            }, 401
        
        except Exception as e:
            return {
                "message": "Something went wrong",
                "error": str(e)
            }, 500

        return f()

    return decorated