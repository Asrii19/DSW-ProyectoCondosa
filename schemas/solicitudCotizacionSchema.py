from marshmallow import Schema, fields
from schemas.personalSchema import PersonalSchema
from schemas.estadoSchema import EstadoSchema
from schemas.solicitudSchema import SolicitudSchema

class SolicitudCotizacionSchema(Schema):
    id_solicitud = fields.Integer()
    id_personal = fields.Integer()
    fecha_cotizacion = fields.Date()
    importe = fields.Decimal()
    id_solicitud_cotizacion = fields.Integer()
    id_estado = fields.Integer()

    solicitud = fields.Nested(SolicitudSchema)
    personal = fields.Nested(PersonalSchema)
    estado = fields.Nested(EstadoSchema)