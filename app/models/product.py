# app/models/product.py

from app import db

class Product(db.Model):
    # Definir los campos del modelo
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # ... otros campos