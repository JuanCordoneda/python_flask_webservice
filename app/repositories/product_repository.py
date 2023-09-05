# app/repositories/product_repository.py

from app.models.product import Product
from app import db

class ProductRepository:
    def get_all_products(self):
        try:
            products = Product.query.all()
            return products
        except Exception as e:
            raise Exception(f"Error al obtener todos los productos: {str(e)}")

    def get_product_by_id(self, product_id):
        try:
            product = Product.query.get(product_id)
            return product
        except Exception as e:
            raise Exception(f"Error al obtener el producto por ID: {str(e)}")

    def create_product(self, data):
        try:
            new_product = Product(**data)
            db.session.add(new_product)
            db.session.commit()
            return new_product
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al crear el producto: {str(e)}")

    def update_product(self, product_id, data):
        try:
            product = Product.query.get(product_id)
            if product:
                for key, value in data.items():
                    setattr(product, key, value)
                db.session.commit()
                return product
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al actualizar el producto: {str(e)}")

    def delete_product(self, product_id):
        try:
            product = Product.query.get(product_id)
            if product:
                db.session.delete(product)
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al eliminar el producto: {str(e)}")
