from flask import jsonify


def not_found():
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': 'Resource not found',
            'code': 404
        }
    ), 404


def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200
