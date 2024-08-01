# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Configurar Flask-HTTPAuth
auth = HTTPTokenAuth(scheme='Bearer')

# Tokens válidos (esto es solo un ejemplo, en producción deberías gestionar los tokens de forma segura)
TOKENS = {
    "7a2b3c4d5e6f7081920a1b2c3d4e5f6g": "user1",
    "0a1b2c3d4e5f6071829a1b2c3d4e5f6g": "user2"
}

@auth.verify_token
def verify_token(token):
    if token in TOKENS:
        return TOKENS[token]
    return None

@auth.error_handler
def auth_error(status):
    return {"message": "Access denied"}, status


