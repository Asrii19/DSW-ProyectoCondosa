from marshmallow import Schema, fields
from schemas.personaSchema import PersonaSchema
from schemas.rolSchema import RolSchema

class PersonalSchema(Schema):
    id_personal = fields.Integer()
    id_persona = fields.Integer()
    id_rol = fields.Integer()
    fecha_contrato = fields.Date()
    fecha_cese = fields.Date()

    persona = fields.Nested(PersonaSchema)
    rol = fields.Nested(RolSchema)