# app/models/entidad.py

from ..app import db

class Entidad(db.Model):
    __tablename__ = 'entidades'

    NUMERO_PROSA = db.Column(db.Float, primary_key=True)
    TIE_NUMERO = db.Column(db.Integer, nullable=True)
    DESCRIPCION = db.Column(db.String(255), nullable=True)
    NUMERO_FIID = db.Column(db.String(255), nullable=True)
    NUMERO_TSYS_EMI = db.Column(db.String(255), nullable=True)
    NUMERO_TSYS_ADQ = db.Column(db.String(255), nullable=True)
    DESC_VENTAS = db.Column(db.String(255), nullable=True)
    DESC_PAGOS = db.Column(db.String(255), nullable=True)
    NUMERO_LN = db.Column(db.String(255), nullable=True)
    GCO_NUMERO = db.Column(db.Float, nullable=True)
    ID_UNICO_CARNET = db.Column(db.String(255), nullable=True)
    TRANSCOD = db.Column(db.Float, nullable=True)
    CAMARA = db.Column(db.Integer, nullable=True)
    ID_BANXICO = db.Column(db.Float, nullable=True)
    ENV_BANXICO = db.Column(db.Float, nullable=True)
    RED_MCD_ID_01 = db.Column(db.String(255), nullable=True)
    RED_MCD_ID_02 = db.Column(db.String(255), nullable=True)
    RED_VSA_ID_01 = db.Column(db.String(255), nullable=True)
    AMEX_CAP = db.Column(db.String(255), nullable=True)
    IND_COLLECTION = db.Column(db.String(255), nullable=True)
