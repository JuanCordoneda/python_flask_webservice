# app/routes/products_service_routes.py

from flask import Blueprint, request, jsonify
from app.controllers.products_service_controller import ProductsServiceController

products_service_bp = Blueprint("products_service", __name__)

products_service_controller = ProductsServiceController()  # Create an instance of the products controller

@products_service_bp.route("/products_service", methods=["GET"])
def get_products():
    return products_service_controller.get_all_products()

@products_service_bp.route("/products_service/<int:product_id>", methods=["GET"])
def get_product(product_id):
    return products_service_controller.get_product_by_id(product_id)

@products_service_bp.route("/products_service", methods=["POST"])
def create_product():
    data = request.get_json()
    return products_service_controller.create_product(data)

@products_service_bp.route("/products_service/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    return products_service_controller.update_product(product_id, data)

@products_service_bp.route("/products_service/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    return products_service_controller.delete_product(product_id)
