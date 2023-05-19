from src.db import db

class Predio(db.Model):
    id_predio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.Numeric, nullable=False)
    areas_comunes = db.Column(db.Numeric, nullable=False)
    NroPuertasAcceso = db.Column(db.Integer, nullable=False)
    NroBloques = db.Column(db.Integer, nullable=False)
    
    def __init__(self,area,areas_comunes,NroPuertasAcceso,NroBloques):
        self.area = area
        self.areas_comunes = areas_comunes
        self.NroPuertasAcceso = NroPuertasAcceso
        self.NroBloques = NroBloques