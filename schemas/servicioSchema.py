from marshmallow import Schema, fields

class ServicioSchema(Schema):
    id_servicio = fields.Integer()
    descripcion = fields.String()
