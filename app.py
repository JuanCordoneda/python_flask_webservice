# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config.config import Config
from app.routes.entidades_routes import entidades_bp

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Configurar CORS
CORS(app)

app.register_blueprint(entidades_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
