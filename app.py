# app.py

from flask import Flask
from config.config import Config
from app.routes.number_routes import number_ruotes

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(number_ruotes)  # Registra el Blueprint de productos service

if __name__ == "__main__":
    app.run(debug=True)
