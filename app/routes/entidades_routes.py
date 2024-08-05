# app/routes/entidades_routes.py

from flask import Blueprint, request
from app.controllers.entidades_controller import EntidadesController
from ..app import auth

entidades_bp = Blueprint("entidades", __name__)
entidades_controller = EntidadesController()

@entidades_bp.route("/entidades", methods=["GET"])
@auth.login_required
def get_entidades():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return entidades_controller.get_all_entidades(page, per_page)

@entidades_bp.route("/entidades", methods=["POST"])
@auth.login_required
def create_entidad():
    data = request.get_json()
    return entidades_controller.create_entidad(data)

@entidades_bp.route("/entidades/<int:entidad_id>", methods=["DELETE"])
@auth.login_required
def delete_entidad(entidad_id):
    return entidades_controller.delete_entidad(entidad_id)