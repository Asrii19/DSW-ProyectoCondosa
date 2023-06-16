from flask import Blueprint, render_template as rt
from models.solicitudCotizacion import SolicitudCotizacion
from models.solicitud import Solicitud
from models.predio import Predio
from models.solicitante import Solicitante
from models.servicio import Servicio  # Asegúrate de importar el modelo Servicio correctamente

bp = Blueprint('cotizaciones', __name__, url_prefix="/cotizaciones")

@bp.route('/')
def cotizaciones():
    cotizaciones_pendientes = Solicitud.query.all()
    cotizaciones_completadas = SolicitudCotizacion.query.filter(SolicitudCotizacion.importe.isnot(None)).all()

    predios = Predio.query.all()
    predios_dict = {predio.id_predio: predio.descripcion for predio in predios}

    solicitantes = Solicitante.query.all()
    solicitantes_dict = {solicitante.id_solicitante: solicitante.nombre_completo for solicitante in solicitantes}

    servicios = Servicio.query.all()
    servicios_dict = {servicio.id_servicio: servicio.descripcion for servicio in servicios}

    for solicitudp in cotizaciones_pendientes:
        solicitudp.descripcion_predio = predios_dict.get(solicitudp.id_predio)
        solicitudp.nombre_solicitante = solicitantes_dict.get(solicitudp.id_solicitante)
        solicitudp.descripcion_servicio = servicios_dict.get(solicitudp.id_servicio)  # Obtener la descripción del servicio
        
    return rt("cotizaciones.html", cotizaciones_pendientes=cotizaciones_pendientes, cotizaciones_completadas=cotizaciones_completadas)
