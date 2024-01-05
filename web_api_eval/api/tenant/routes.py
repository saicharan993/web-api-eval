from flask import Blueprint
from flask import Flask, request, jsonify,Response
from web_api_eval.models.tenants_model import Tenant
from web_api_eval.utils.authtoken import token_required
from web_api_eval import db
import json
import urllib

tenant = Blueprint('tenant',__name__)

# Set Tenant 
@tenant.route('/tenant', methods=['POST'])
@token_required
def create_tenant():
    data = request.json
    new_tenant_name = data.get('name')
    new_tenant_token = data.get('token')

    if not new_tenant_name or not new_tenant_token:
        return jsonify({'error': 'Invalid request'}), 400
    
    old_tenant = Tenant.query.filter_by(name=new_tenant_name).first()
    
    if old_tenant:
        return jsonify({'error': 'Tenant already exists'}), 400

    new_tenant = Tenant(name=new_tenant_name,token=new_tenant_token)
    db.session.add(new_tenant)
    db.session.commit()

    return jsonify({'message': f'Tenant {new_tenant_name} created successfully'})

@tenant.route('/tenant', methods=['GET'])
@token_required
def get_tenants():
    tenant_list=[]
    tenants = Tenant.query.order_by(Tenant.id.asc())

    for tenant in tenants :
        tenant_list.append(
            {
            "tenants":[{
            "name": tenant.name,
            "token":tenant.token,
            }],
            "errors":[]}
            )
    return jsonify(tenant_list), 200



    