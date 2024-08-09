# app/repositories/entidades_repository.py

from app.models.entidades import Entidad
from ..app import db

class EntidadesRepository:
    def get_all_entidades(self, page, per_page):
        entidades = Entidad.query.paginate(page, per_page, False)
        total = entidades.total
        return [entidad.to_dict() for entidad in entidades.items], total

    def create_entidad(self, data):
        try:
            new_entidad = Entidad(
                id_entidad=data.get('id_entidad'),
                nombre_entidad=data.get('nombre_entidad'),
                fiid_pos=data.get('fiid_pos'),
                fiid_atm=data.get('fiid_atm'),
                fiid_online=data.get('fiid_online'),
                id_banxico=data.get('id_banxico'),
                id_emisor=data.get('id_emisor'),
                id_adquirente=data.get('id_adquirente')
            )
            db.session.add(new_entidad)
            db.session.commit()
            return self.return_entidad(new_entidad)
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error creating entity: {str(e)}")

    def delete_entidad(self, entidad_id):
        entidad = Entidad.query.get(entidad_id)
        if entidad:
            db.session.delete(entidad)
            db.session.commit()
            return True
        return False

    # Método que convierte varias entidades a JSON
    def return_entidades(self, entidades):
        entidades_list = []
        for entidad in entidades:
            entidad_dict = {
                "id_entidad": entidad.id_entidad,
                "nombre_entidad": entidad.nombre_entidad,
                "fiid_pos": entidad.fiid_pos,
                "fiid_atm": entidad.fiid_atm,
                "fiid_online": entidad.fiid_online,
                "id_banxico": entidad.id_banxico,
                "id_emisor": entidad.id_emisor,
                "id_adquirente": entidad.id_adquirente,
            }
            entidades_list.append(entidad_dict)
        return entidades_list

    # Método que convierte una entidad a JSON
    def return_entidad(self, entidad):
        entidad_dict = {
            "id_entidad": entidad.id_entidad,
            "nombre_entidad": entidad.nombre_entidad,
            "fiid_pos": entidad.fiid_pos,
            "fiid_atm": entidad.fiid_atm,
            "fiid_online": entidad.fiid_online,
            "id_banxico": entidad.id_banxico,
            "id_emisor": entidad.id_emisor,
            "id_adquirente": entidad.id_adquirente,
        }
        return entidad_dict
