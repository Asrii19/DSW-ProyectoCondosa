from marshmallow import Schema, fields

class TipoPredioSchema(Schema):
    id_tipo_predio = fields.Integer()
    nomre_predio = fields.String()
