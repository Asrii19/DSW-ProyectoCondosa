from flask import Blueprint, render_template as rt
from models.solicitud import Solicitud
from models.solicitante import Solicitante

bp = Blueprint('solicitud_cotizacion', __name__, url_prefix="/solicitud") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def cotizar():
    id_solicitud = 2
    solicitud = Solicitud.query.get(id_solicitud)
    solicitante = Solicitante.query.get(solicitud.id_solicitante)

    data = {
        "id_solicitud": solicitud.id_solicitud,
        "id_solicitante": solicitud.id_solicitante,
        "id_predio": solicitud.id_predio,
        "id_servicio": solicitud.id_servicio,
        #informacion personal
        "id_persona": solicitante.id_persona,
        
    }
    return rt("cotizacion.html")