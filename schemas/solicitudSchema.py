from marshmallow import Schema, fields
from schemas.predioSchema import PredioSchema
from schemas.solicitanteSchema import SolicitanteSchema
from schemas.servicioSchema import ServicioSchema

class SolicitudSchema(Schema):
    id_solicitud = fields.Integer()
    id_predio = fields.Integer()
    id_solicitante = fields.Integer()
    id_servicio =fields.Integer()
    area_predio = fields.Decimal()
    num_casas = fields.Integer()
    cant_acomunes = fields.Integer()
    area_acomunes = fields.Integer()
    cant_vigilantes = fields.Integer()
    cant_plimpieza = fields.Integer()
    cant_administracion = fields.Integer()
    cant_jardineria = fields.Integer()

    predio = fields.Nested(PredioSchema)
    solicitante = fields.Nested(SolicitanteSchema)
    servicio = fields.Nested(ServicioSchema)
