# app/models/product.py

from ..app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    userId = db.Column(db.Integer, nullable=False)
