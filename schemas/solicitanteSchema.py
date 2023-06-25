from marshmallow import Schema, fields
from schemas.personaSchema import PersonaSchema
from schemas.rolSchema import RolSchema

class SolicitanteSchema(Schema):
    id_solicitante = fields.Integer()
    id_persona = fields.Integer()
    id_rol = fields.Integer()
    telefono = fields.Integer()
    correo = fields.String()
    
    persona = fields.Nested(PersonaSchema)
    rol = fields.Nested(RolSchema)