# app/controllers/products_controller.py

from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

class ProductsController:
    def __init__(self):
        self.product_service = ProductService()

    def get_all_products(self):
        try:
            products = self.product_service.get_all_products()
            return jsonify(products), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_product_by_id(self, product_id):
        try:
            product = self.product_service.get_product_by_id(product_id)
            if product:
                return jsonify(product), 200
            else:
                return jsonify({"message": "Product not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def create_product(self, data):
        try:
            new_product = self.product_service.create_product(data)
            return jsonify(new_product), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def update_product(self, product_id, data):
        try:
            updated_product = self.product_service.update_product(product_id, data)
            if updated_product:
                return jsonify(updated_product), 200
            else:
                return jsonify({"message": "Product not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete_product(self, product_id):
        try:
            deleted_product = self.product_service.delete_product(product_id)
            if deleted_product:
                return jsonify({"message": "Product deleted"}), 200
            else:
                return jsonify({"message": "Product not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

