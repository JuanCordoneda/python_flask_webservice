# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from app.routes.products_service_routes import products_service_bp
from app.routes.products_bd_routes import products_bd_bp

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

app.register_blueprint(products_service_bp)  # Registra el Blueprint de productos service
app.register_blueprint(products_bd_bp)  # Registra el Blueprint de productos bd

if __name__ == "__main__":
    app.run(debug=True)
