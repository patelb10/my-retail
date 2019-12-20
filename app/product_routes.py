"""This module will serve the api request."""

from app.mongo_handler import MongoHandler
from app.product_service import ProductService
from app import app
from flask import request, jsonify, Response
import json
import ast


mongo = MongoHandler()
product_service = ProductService()

@app.route("/products/", methods=['GET'])
def get_all_products():
    data = mongo.get_all_products()
    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    data = product_service.get_product(id)
    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    params = ast.literal_eval(json.dumps(request.get_json()))
    save_product = product_service.save_product(id, params)
    resp = jsonify(save_product)
    resp.status_code = 201
    return resp