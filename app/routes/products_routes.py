from flask import Blueprint
from app.controllers.products_controller import ProductsController

products_bp = Blueprint("products", __name__)

products_controller = ProductsController()  # Crea una instancia del controlador de productos

@products_bp.route("/products", methods=["GET"])
def get_products():
    return products_controller.get_all_products()