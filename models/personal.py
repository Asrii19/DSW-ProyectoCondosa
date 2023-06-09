from utils.db import db

class Personal(db.Model):
    id_personal = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_tipo_solicitante = db.Column(db.Integer, db.ForeignKey('rol.id_tipo_solicitante'))
    fecha_contrato = db.Column(db.Date)
    fecha_cese = db.Column(db.Date)
    def __init__(self, id_personal, id_persona, id_tipo_solicitante, fecha_contrato, fecha_cese):
        self.id_personal = id_personal
        self.id_persona = id_persona
        self.id_tipo_solicitante = id_tipo_solicitante
        self.fecha_contrato = fecha_contrato
        self.fecha_cese = fecha_cese