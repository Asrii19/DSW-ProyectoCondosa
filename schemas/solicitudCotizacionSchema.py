from marshmallow import Schema, fields
from schemas.personalSchema import PersonalSchema
from schemas.estadoSchema import EstadoSchema

class SolicitudCotizacionSchema(Schema):
    id_solicitud = fields.Integer()
    id_personal = fields.Integer()
    fecha_cotizacion = fields.Date()
    importe = fields.Decimal()
    id_estado = fields.Integer()

    personal = fields.Nested(PersonalSchema)
    estado = fields.Nested(EstadoSchema)