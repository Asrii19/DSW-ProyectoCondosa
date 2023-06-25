from marshmallow import Schema, fields

class UbigeoSchema(Schema):
    idubigeo = fields.String()
    departamento = fields.String()
    provincia = fields.String()
    distrito = fields.String()
    superficie = fields.Number()
    altitud = fields.Number()
    latitud = fields.Number()
    longitud = fields.Number()
