from flask import Blueprint
from web_api_eval.models.user_model import User
from flask import Flask, request, jsonify
from web_api_eval import db
from web_api_eval.utils.authtoken import token_required
import hashlib 



api_1 = Blueprint('api_1',__name__)

# Create response
def create_response(user: User,error_message: str):
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
@token_required
def get_users():
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
@token_required
def create_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return create_response(None,"Please provide username and password."), 400
    
    user = User.query.filter_by(username=username).first()
    if user:  
        return create_response(None,"User already exists."), 400


    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return create_response(user,None)

# handle updating User
@api_1.route("/user", methods=["PUT"])
@token_required
def update_user():
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
@token_required
def delete_users():
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
        
       
        
        
    
    
     

       




