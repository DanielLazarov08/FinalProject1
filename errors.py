from flask import Blueprint
from flask import jsonify

errors= Blueprint('errors', __name__)

def ok(message):
    response = jsonify({'error': 'OK', 'message': message})
    response.status_code = 200
    return response

def created(message):
    response = jsonify({'error': 'Created', 'message': message})
    response.status_code = 201
    return response

def nocontent(message):
    response = jsonify({'error': 'No content', 'message': message})
    response.status_code = 204
    return response

def badrequest(message):
    response = jsonify({'error': 'Bad Request', 'message': message})
    response.status_code = 400
    return response

def forbidden(message):
    response = jsonify({'error': 'Forbidden', 'message': message})
    response.status_code = 403
    return response

def unauthorized(message):
    response = jsonify({'error': 'Unauthorized', 'message': message})
    response.status_code = 401
    return response

def page_not_found(e):
    response = jsonify({'error': 'Notfound', 'message': 'Page Not Found'})
    response.status_code = 404
    return response

def internal_server_error(e):
    response = jsonify({'error': 'Internal server error',
                        'message': 'Internal server error'})
    response.status_code = 500
    return response