from flask import Blueprint,g,session
from web_api_eval.models.user_model import create_user_model
from web_api_eval.models.tenants_model import Tenant
from flask import Flask, request, jsonify
from web_api_eval import db, default_token
from web_api_eval.utils.authtoken import token_required
import hashlib 


api_1 = Blueprint('api_1',__name__)

# Setting tenant
@api_1.before_request
def set_current_tenant():
    token =  request.headers.get("AUTHTOKEN")
    if not token:
        return create_response(None,"Token is missing"), 401
        
    tenant_name = request.view_args.get('tenant_name', None)
    g.current_tenant_name = tenant_name

    if tenant_name!="default":
        tenant = Tenant.query.filter_by(name=tenant_name).first()
        if tenant:
            if token != tenant.token:
                return create_response(None,"Invalid Authentication token"), 403           
        else:
            return create_response(None,"Tenant doesn't exist"), 400   
        
    elif tenant_name=="default":
        # default tenant
        if token != default_token:
                return create_response(None,"Invalid Authentication token"), 403

# Create response
def create_response(user,error_message: str):
    if error_message:
        return jsonify({
            "users":[{
            "user_id": None,
            "username":None,
            "password":None
            }],
            "errors":[error_message]}) 
        
    if not error_message:
        return jsonify({
            "users":[{
            "user_id": user.id,
            "username":user.username,
            "password":hashlib.sha256((user.username+user.password).encode()).hexdigest()
            }],
            "errors":[]}) 
    

# Handle GET request without 
@api_1.route('/user',methods=['GET'])
def get_users(tenant_name):
    User = create_user_model(g.current_tenant_name) 
    user_id = request.args.get('user_id')
    
    if not user_id:
        user_list=[]
        users = User.query.order_by(User.id.asc())
    
        for user in users :
            user_list.append(
                {
                "users":[{
                "user_id": user.id,
                "username":user.username,
                "password":hashlib.sha256((user.username+user.password).encode()).hexdigest()
                }],
                "errors":[]}
                )
        return jsonify(user_list), 200
    
    elif user_id:
        user = User.query.filter_by(id=user_id).first()  
        if user:
            return create_response(user,None),200
        else: 
            return create_response(None,"No user found for requested user_id"),400
            
# Handle User creating uinsg POST
@api_1.route("/user", methods=["POST"])
def create_user(tenant_name):
    User = create_user_model(g.current_tenant_name) 
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return create_response(None,"Please provide username and password."), 400

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return create_response(user,None)

# handle updating User
@api_1.route("/user", methods=["PUT"])
def update_user(tenant_name):
    User = create_user_model(g.current_tenant_name) 
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user_id = request.args.get('user_id')
    if not user_id:
        return create_response(None,"Please provide user id of user.")
    if not username or not password:
        return create_response(None,"Please provide username and password."), 400
    
    if user_id:
        user = User.query.filter_by(id=user_id).first()
        if user:
            user.username = username
            user.password = password
            db.session.commit()
            return create_response(user,None)
        elif not user:
            return create_response(None,"No user found for requested user_id")
    

# Handle DELETE request
@api_1.route("/user", methods=["DELETE"])
def delete_users(tenant_name):
    User = create_user_model(g.current_tenant_name) 
    user_id = request.args.get('user_id')
    
    if not user_id:
        return create_response(None,"Please provide user id of user.")
    if user_id:
        user = User.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return create_response(user,None)
        elif not user:
            return create_response(None,"No user found for requested user_id")
        
       
        
        
    
    
     

       




