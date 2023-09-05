# app/models/invoice.py

from app import db

class Invoice(db.Model):
    # Definir los campos del modelo
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    # ... otros campos
