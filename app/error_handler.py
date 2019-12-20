from flask import jsonify
from app import app
from flask import request

class ProductNotFound(Exception):
    pass
class ExternalAPINotFound(Exception):
    pass
class InvalidRequestError(Exception):
    pass
class ProductNotUpdated(Exception):
    pass

@app.errorhandler(ExternalAPINotFound)
def not_found(e):

    return jsonify({
        'status': 404,
        'description': "External API Not Found"
    }), 404

@app.errorhandler(InvalidRequestError)
def api_validation(error=None):

    return jsonify({
        'status': 400,
        'description': "Bad Request, Malformed JSON"
    }), 400

@app.errorhandler(ProductNotFound)
def not_found(e):
    return jsonify({
        'status': 404,
        'description': "Product not found in database",
        'address': request.url
    }), 404

@app.errorhandler(ProductNotUpdated) 
def product_already_exists(error=None):

    return jsonify({
        'status': 409,
        'description': "No operation"
    }), 409

@app.errorhandler(409)
def already_exists(error=None):

    return jsonify({

        'status': 409,
        'description': error.description,
        'address': request.url
    }), 409

@app.errorhandler(501)
def not_implemented(error=None):

    return jsonify({

        'status': 501,
        'description': 'not_implemented',
        'address': request.url
    }), 501

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({

        'status': 404,
        'description': 'not_implemented',
        'address': request.url
    }), 404



