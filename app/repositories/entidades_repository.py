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
                NUMERO_PROSA=data.get('NUMERO_PROSA'),
                TIE_NUMERO=data.get('TIE_NUMERO'),
                DESCRIPCION=data.get('DESCRIPCION'),
                NUMERO_FIID=data.get('NUMERO_FIID'),
                NUMERO_TSYS_EMI=data.get('NUMERO_TSYS_EMI'),
                NUMERO_TSYS_ADQ=data.get('NUMERO_TSYS_ADQ'),
                DESC_VENTAS=data.get('DESC_VENTAS'),
                DESC_PAGOS=data.get('DESC_PAGOS'),
                NUMERO_LN=data.get('NUMERO_LN'),
                GCO_NUMERO=data.get('GCO_NUMERO'),
                ID_UNICO_CARNET=data.get('ID_UNICO_CARNET'),
                TRANSCOD=data.get('TRANSCOD'),
                CAMARA=data.get('CAMARA'),
                ID_BANXICO=data.get('ID_BANXICO'),
                ENV_BANXICO=data.get('ENV_BANXICO'),
                RED_MCD_ID_01=data.get('RED_MCD_ID_01'),
                RED_MCD_ID_02=data.get('RED_MCD_ID_02'),
                RED_VSA_ID_01=data.get('RED_VSA_ID_01'),
                AMEX_CAP=data.get('AMEX_CAP'),
                IND_COLLECTION=data.get('IND_COLLECTION')
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
                "NUMERO_PROSA": entidad.NUMERO_PROSA,
                "TIE_NUMERO": entidad.TIE_NUMERO,
                "DESCRIPCION": entidad.DESCRIPCION,
                "NUMERO_FIID": entidad.NUMERO_FIID,
                "NUMERO_TSYS_EMI": entidad.NUMERO_TSYS_EMI,
                "NUMERO_TSYS_ADQ": entidad.NUMERO_TSYS_ADQ,
                "DESC_VENTAS": entidad.DESC_VENTAS,
                "DESC_PAGOS": entidad.DESC_PAGOS,
                "NUMERO_LN": entidad.NUMERO_LN,
                "GCO_NUMERO": entidad.GCO_NUMERO,
                "ID_UNICO_CARNET": entidad.ID_UNICO_CARNET,
                "TRANSCOD": entidad.TRANSCOD,
                "CAMARA": entidad.CAMARA,
                "ID_BANXICO": entidad.ID_BANXICO,
                "ENV_BANXICO": entidad.ENV_BANXICO,
                "RED_MCD_ID_01": entidad.RED_MCD_ID_01,
                "RED_MCD_ID_02": entidad.RED_MCD_ID_02,
                "RED_VSA_ID_01": entidad.RED_VSA_ID_01,
                "AMEX_CAP": entidad.AMEX_CAP,
                "IND_COLLECTION": entidad.IND_COLLECTION
            }
            entidades_list.append(entidad_dict)
        return entidades_list

    # Método que convierte una entidad a JSON
    def return_entidad(self, entidad):
        entidad_dict = {
            "NUMERO_PROSA": entidad.NUMERO_PROSA,
            "TIE_NUMERO": entidad.TIE_NUMERO,
            "DESCRIPCION": entidad.DESCRIPCION,
            "NUMERO_FIID": entidad.NUMERO_FIID,
            "NUMERO_TSYS_EMI": entidad.NUMERO_TSYS_EMI,
            "NUMERO_TSYS_ADQ": entidad.NUMERO_TSYS_ADQ,
            "DESC_VENTAS": entidad.DESC_VENTAS,
            "DESC_PAGOS": entidad.DESC_PAGOS,
            "NUMERO_LN": entidad.NUMERO_LN,
            "GCO_NUMERO": entidad.GCO_NUMERO,
            "ID_UNICO_CARNET": entidad.ID_UNICO_CARNET,
            "TRANSCOD": entidad.TRANSCOD,
            "CAMARA": entidad.CAMARA,
            "ID_BANXICO": entidad.ID_BANXICO,
            "ENV_BANXICO": entidad.ENV_BANXICO,
            "RED_MCD_ID_01": entidad.RED_MCD_ID_01,
            "RED_MCD_ID_02": entidad.RED_MCD_ID_02,
            "RED_VSA_ID_01": entidad.RED_VSA_ID_01,
            "AMEX_CAP": entidad.AMEX_CAP,
            "IND_COLLECTION": entidad.IND_COLLECTION
        }
        return entidad_dict
