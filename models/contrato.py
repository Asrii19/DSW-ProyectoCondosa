from src.db import db

class Contrato(db.Model):
    id_contrato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column(db.Numeric, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(1024), nullable=True)
    
    def __init__(self, monto, fecha, descripcion=None):
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion
