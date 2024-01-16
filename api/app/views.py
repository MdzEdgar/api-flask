from flask import Blueprint

from .responses import response

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    return response({
        'mensaje': 'Nuevo mensaje'
    })


@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task():
    pass


@api_v1.route('/tasks', methods=['POST'])
def create_task():
    pass


@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    pass


@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_tasks():
    pass
