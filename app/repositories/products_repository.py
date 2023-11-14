# app/repositories/products_repository.py

from app.models.product import Product
from ..app import db

class ProductsRepository:
    def get_all_products(self):
        try:
            products = Product.query.all()
            return self.return_products(products)
        except Exception as e:
            raise Exception(f"Error retrieving all products: {str(e)}")

    def get_product_by_id(self, product_id):
        try:
            product = Product.query.get(product_id)
            return self.return_product(product)
        except Exception as e:
            raise Exception(f"Error retrieving product by ID: {str(e)}")

    def create_product(self, data):
        try:
            new_product = Product(title=data['title'], body=data['body'], userId=data['userId'])
            db.session.add(new_product)
            db.session.commit()
            return self.return_product(new_product)
        
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error creating product: {str(e)}")

    def update_product(self, product_id, data):
        try:
            product = Product.query.get(product_id)
            if product:
                for key, value in data.items():
                    setattr(product, key, value)
                db.session.commit()
                return self.return_product(product)
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error updating product: {str(e)}")

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
            raise Exception(f"Error deleting product: {str(e)}")
        
    # metodo que setea las variables de varios productos como JSON
    def return_products(self, products):
        products_list = []
        for product in products:
            product_dict = {
                "id": product.id,
                "title": product.title,
                "body": product.body,
                "userId": product.userId
            }
            products_list.append(product_dict)
        return products_list
    
    # metodo que setea las variables de 1 producto como JSON
    def return_product(self, product):
        product_dict = {
            "id": product.id,
            "title": product.title,
            "body": product.body,
            "userId": product.userId
        }
        return product_dict
