# app/routes/entidades_routes.py

from flask import Blueprint, request, jsonify
from app.controllers.entidades_controller import EntidadesController

entidades_bp = Blueprint("entidades", __name__)

entidades_controller = EntidadesController()

@entidades_bp.route("/entidades", methods=["GET"])
def get_entidades():
    return entidades_controller.get_all_entidades()

@entidades_bp.route("/entidades", methods=["POST"])
def create_entidad():
    data = request.get_json()
    return entidades_controller.create_entidad(data)
