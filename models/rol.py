from utils.db import db

class Rol(db.Model):
    id_tipo_solicitante = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(60))
    def __init__(self, id_tipo_solicitante, descripcion):
        self.id_tipo_solicitante = id_tipo_solicitante
        self.descripcion = descripcion