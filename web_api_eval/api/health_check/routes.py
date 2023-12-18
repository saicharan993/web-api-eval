from flask import Blueprint

health_check = Blueprint('health_check',__name__,)

@health_check.route('/status',methods=['GET'])
def get_status():
    return {'message': 'Healthy'}