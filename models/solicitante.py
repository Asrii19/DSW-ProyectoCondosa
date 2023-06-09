from utils.db import db

class Solicitante(db.Model):
    id_solicitante = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_tipo_solicitante = db.Column(db.Integer, db.ForeignKey('rol.id_tipo_solicitante'))
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(30))
    def __init__(self, id_solicitante, id_persona, id_tipo_solicitante, telefono, correo):
        self.id_solicitante = id_solicitante
        self.id_persona = id_persona
        self.id_tipo_solicitante = id_tipo_solicitante
        self.telefono = telefono
        self.correo = correo