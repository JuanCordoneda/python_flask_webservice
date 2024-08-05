# app/controllers/entidades_controller.py

from app.repositories.entidades_repository import EntidadesRepository
from app.dtos.response_standard import format_success_created_response, format_error_response, format_success_response, format_deleted_response

class EntidadesController:
    def __init__(self):
        self.entidades_repository = EntidadesRepository()

    def get_all_entidades(self, page, per_page):
        try:
            entidades, total = self.entidades_repository.get_all_entidades(page, per_page)
            response = {
                "total": total,
                "page": page,
                "per_page": per_page,
                "entidades": entidades
            }
            return format_success_response(response), 200
        except Exception as e:
            return format_error_response(str(e)), 500

    def create_entidad(self, data):
        try:
            # Convert 'NULL' strings to None
            for key, value in data.items():
                if value == 'NULL':
                    data[key] = None
            
            new_entidad = self.entidades_repository.create_entidad(data)
            return format_success_created_response(new_entidad), 201
        except Exception as e:
            return format_error_response(str(e)), 500

    def delete_entidad(self, entidad_id):
            try:
                deleted = self.entidades_repository.delete_entidad(entidad_id)
                if deleted:
                    return format_deleted_response('Entidad eliminada correctamente'), 202
                else:
                    return format_error_response("Entidad no encontrada"), 500
            except Exception as e:
                return format_error_response(str(e)), 500