from flask import Blueprint, render_template as rt
from models.solicitud import Solicitud
from models.solicitudCotizacion import SolicitudCotizacion
from schemas.solicitudSchema import SolicitudSchema
from schemas.solicitudCotizacionSchema import SolicitudCotizacionSchema

bp = Blueprint('solicitud_cotizacion', __name__, url_prefix="/solicitud") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/<id_solicitud>', methods=['GET'])
def cotizar(id_solicitud):
    
    solicitud_cotizacion = SolicitudCotizacion.query.filter_by(id_solicitud=id_solicitud).first()
    
    if solicitud_cotizacion:
        cotizacion_realizada = "Realizada"
        data = SolicitudCotizacionSchema().dump(solicitud_cotizacion)
    else:
        cotizacion_realizada = "No realizada"
        solicitud=Solicitud.query.get(id_solicitud)
        data = SolicitudSchema().dump(solicitud)
    
    return rt("cotizacion.html",data=data,cotizacion_realizada=cotizacion_realizada)