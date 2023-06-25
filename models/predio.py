from utils.db import db

class Predio(db.Model):
    id_predio = db.Column(db.Integer, primary_key=True)
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey('tipo_predio.id_tipo_predio'))
    descripcion = db.Column(db.String(255))
    ruc = db.Column(db.String(11))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(255))
    direccion = db.Column(db.String(255))

    tipo_predio = db.relationship('TipoPredio', backref='predio')

    def __init__(self, id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion):
        self.id_predio = id_predio
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion