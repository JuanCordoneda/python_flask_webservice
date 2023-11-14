# app/controllers/products_bd_controller.py

from app.repositories.products_repository import ProductsRepository
from app.dtos.response_standard import format_success_created_response, format_error_response, format_success_response

class ProductsBdController:
    def __init__(self):
        self.product_repository = ProductsRepository()

    def get_all_products(self):
        try:
            products = self.product_repository.get_all_products()
            return format_success_response(products), 200
        except Exception as e:
            return format_error_response(str(e)), 500

    def get_product_by_id(self, product_id):
        try:
            product = self.product_repository.get_product_by_id(product_id)
            if product:
                return format_success_response(product), 200
            else:
                return format_error_response("Product not found"), 404
        except Exception as e:
            return format_error_response(str(e)), 500

    def create_product(self, data):
        try:
            new_product = self.product_repository.create_product(data)
            return format_success_created_response(new_product), 201
        except Exception as e:
            return format_error_response(str(e)), 500

    def update_product(self, product_id, data):
        try:
            updated_product = self.product_repository.update_product(product_id, data)
            if updated_product:
                return format_success_created_response(updated_product), 200
            else:
                return format_error_response("Product not found"), 404
        except Exception as e:
            return format_error_response(str(e)), 500

    def delete_product(self, product_id):
        try:
            deleted_product = self.product_repository.delete_product(product_id)
            if deleted_product:
                return format_success_created_response("Product deleted"), 200
            else:
                return format_error_response("Product not found"), 404
        except Exception as e:
            return format_error_response(str(e)), 500

