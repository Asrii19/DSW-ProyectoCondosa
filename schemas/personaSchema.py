from marshmallow import Schema, fields
from schemas.tipoDocumentoSchema import TipoDocumentoSchema
from schemas.ubigeoSchema import UbigeoSchema

class PersonaSchema(Schema):
    id_persona = fields.Integer()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    nombres = fields.String()
    fecha_nacimiento = fields.Date()
    id_tipo_documento = fields.Integer()
    ndocumento = fields.String()
    direccion = fields.String()
    idubigeo = fields.String()

    tipo_documento = fields.Nested(TipoDocumentoSchema)
    ubigeo = fields.Nested(UbigeoSchema)

    #extra
    nombre_completo = fields.Method('get_nombre_completo')

    def get_nombre_completo(self, obj):
        return obj.apellido_paterno + ' ' + obj.apellido_materno + ' ' + obj.nombres
