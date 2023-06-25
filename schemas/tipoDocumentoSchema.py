from marshmallow import Schema, fields

class TipoDocumentoSchema(Schema):
    id_tipo_documento = fields.Integer()
    descripcion = fields.String()