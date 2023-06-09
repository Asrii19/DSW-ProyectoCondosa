from utils.db import db

class PresidentePredio(db.Model):
    id_presidente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_contrato = db.Column(db.Integer, db.ForeignKey('contrato.id_contrato'), nullable=False, unique=True)
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'), nullable=False, unique=True)
    dni = db.Column(db.String(8), nullable=False, unique=True)
    apellidos = db.Column(db.String(40), nullable=True)
    nombre = db.Column(db.String(30), nullable=False)
    predio_asignado = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(30), nullable=False)

    contrato = db.relationship('Contrato', backref='presidente_predio', uselist=False)
    predio = db.relationship('Predio', backref='presidente_predio', uselist=False)

    def __init__(self, id_contrato, id_predio, dni, apellidos, nombre, predio_asignado, telefono, correo):
        self.id_contrato = id_contrato
        self.id_predio = id_predio
        self.dni = dni
        self.apellidos = apellidos
        self.nombre = nombre
        self.predio_asignado = predio_asignado
        self.telefono = telefono
        self.correo = correo
