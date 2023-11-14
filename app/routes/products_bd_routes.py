# app/routes/products_bd_routes.py

from flask import Blueprint, request, jsonify
from app.controllers.products_bd_controller import ProductsBdController

products_bd_bp = Blueprint("products_bd", __name__)

products_bd_controller = ProductsBdController()  # Create an instance of the products controller

@products_bd_bp.route("/products_bd", methods=["GET"])
def get_products():
    return products_bd_controller.get_all_products()

@products_bd_bp.route("/products_bd/<int:product_id>", methods=["GET"])
def get_product(product_id):
    return products_bd_controller.get_product_by_id(product_id)

@products_bd_bp.route("/products_bd", methods=["POST"])
def create_product():
    data = request.get_json()
    return products_bd_controller.create_product(data)

@products_bd_bp.route("/products_bd/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    return products_bd_controller.update_product(product_id, data)

@products_bd_bp.route("/products_bd/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    return products_bd_controller.delete_product(product_id)
