from flask import Blueprint, render_template as rt
from models.solicitud import Solicitud

bp = Blueprint('solicitud_cotizacion', __name__, url_prefix="/solicitud") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def cotizar():
    id_solicitud = 1
    solicitud = Solicitud.query.get(id_solicitud)


    data = {
        "id_solicitud": 2
    }
    return rt("cotizacion.html")