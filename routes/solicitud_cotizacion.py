from flask import Blueprint, render_template as rt
from models.solicitud import Solicitud
from models.solicitante import Solicitante
from models.persona import Persona
from models.rol import Rol
from models.predio import Predio
from models.tipoPredio import TipoPredio
from models.servicio import Servicio

bp = Blueprint('solicitud_cotizacion', __name__, url_prefix="/solicitud") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def cotizar():
    id_solicitud = 2
    cotizacion_confirmada = False

    solicitud = Solicitud.query.get(id_solicitud)
    solicitante = Solicitante.query.get(solicitud.id_solicitante)
    persona = Persona.query.get(solicitante.id_persona)
    rol = Rol.query.get(solicitante.id_rol)
    predio = Predio.query.get(solicitud.id_predio)
    tipo_predio = TipoPredio.query.get(predio.id_tipo_predio)
    servicio = Servicio.query.get(solicitud.id_servicio)
    data = {
        "id_solicitud": solicitud.id_solicitud,
        "id_solicitante": solicitud.id_solicitante,
        "id_predio": solicitud.id_predio,
        "id_servicio": solicitud.id_servicio,
        "id_persona": solicitante.id_persona,
        "id_tipo_predio": predio.id_tipo_predio,
        #informacion personal
        "nombres_apellido": persona.nombres + " " + persona.apellido_paterno,
        "ndocumento": persona.ndocumento,
        "rol": rol.descripcion,
        "correo": solicitante.correo,
        #informacion del predio
        "nombre_predio": predio.descripcion,
        "direccion_predio": predio.direccion,
        "tipo_predio": tipo_predio.nomre_predio,
        "ruc_predio": predio.ruc,
        #informacion de los servicios
        "tipo_servicio": servicio.descripcion,
        "cant_plimpieza": solicitud.cant_plimpieza,
        "cant_vigilantes": solicitud.cant_vigilantes,
    }
    return rt("cotizacion.html",data=data,cotizacion_confirmada=cotizacion_confirmada)