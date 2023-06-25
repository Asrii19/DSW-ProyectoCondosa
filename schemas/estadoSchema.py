from marshmallow import Schema, fields

class EstadoSchema(Schema):
    id_estado = fields.Integer()
    descripcion = fields.String()
