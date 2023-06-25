from marshmallow import Schema, fields
from schemas.tipoPredioSchema import TipoPredioSchema

class PredioSchema(Schema):
    id_predio = fields.Integer()
    id_tipo_predio = fields.Integer()
    descripcion = fields.String()
    ruc = fields.String()
    telefono = fields.String()
    correo = fields.String()
    direccion = fields.String()
    
    tipo_predio = fields.Nested(TipoPredioSchema)
