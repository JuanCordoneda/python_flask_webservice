from ..app import db

class Entidad(db.Model):
    __tablename__ = 'entidades'

    id_entidad = db.Column(db.Integer, primary_key=True)
    nombre_entidad = db.Column(db.String(255), nullable=False)
    fiid_pos = db.Column(db.String(255), nullable=False)
    fiid_atm = db.Column(db.String(220), nullable=False)
    fiid_online = db.Column(db.String(255), nullable=False)
    id_banxico = db.Column(db.String(255), nullable=True)
    id_emisor = db.Column(db.String(255), nullable=True)
    id_adquirente = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            "id_entidad": self.id_entidad,
            "nombre_entidad": self.nombre_entidad,
            "fiid_pos": self.fiid_pos,
            "fiid_atm": self.fiid_atm,
            "fiid_online": self.fiid_online,
            "id_banxico": self.id_banxico,
            "id_emisor": self.id_emisor,
            "id_adquirente": self.id_adquirente,
        }
