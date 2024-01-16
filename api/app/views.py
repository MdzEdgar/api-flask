from flask import Blueprint

from .models.task import Task
from .responses import response
from .responses import not_found

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()

    return response([
        task.serialize() for task in tasks
    ])


@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.filter_by(id=id).first()

    if task is None:
        return not_found()

    return response(task.serialize())


@api_v1.route('/tasks', methods=['POST'])
def create_task():
    pass


@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    pass


@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_tasks():
    pass
