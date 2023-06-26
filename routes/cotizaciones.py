from flask import Blueprint, render_template as rt, request, redirect, url_for
from models.solicitudCotizacion import SolicitudCotizacion
from models.solicitud import Solicitud
from schemas.solicitudSchema import SolicitudSchema
from schemas.solicitudCotizacionSchema import SolicitudCotizacionSchema
from models.estado import Estado
from models.servicio import Servicio  # Asegúrate de importar el modelo Servicio correctamente
from utils.db import db
from utils.id import formatear_id
from datetime import datetime

bp = Blueprint('cotizaciones', __name__, url_prefix="/cotizaciones")

@bp.route('/', methods=['POST','GET'])
def cotizaciones():
    # Obtener todas las solicitudes
    solicitudes = Solicitud.query.all()

    # Obtener todas las solicitudes con cotizaciones
    solicitudes_con_cotizaciones = SolicitudCotizacion.query.all()
    solicitudes_con_cotizaciones_ids = [cotizacion.id_solicitud for cotizacion in solicitudes_con_cotizaciones]
    
    # Obtener las cotizaciones pendientes y completadas
    cotizaciones_pendientes = [solicitud for solicitud in solicitudes if solicitud.id_solicitud not in solicitudes_con_cotizaciones_ids]
    cotizaciones_completadas = solicitudes_con_cotizaciones

    # Ordenar las solicitudes
    cotizaciones_pendientes = sorted(cotizaciones_pendientes, key=lambda solicitud: solicitud.id_solicitud)
    cotizaciones_completadas = sorted(cotizaciones_completadas, key=lambda solicitud: solicitud.id_solicitud)

    # Serializar los objetos por medio de schemas
    cotizaciones_pendientes_serializadas = SolicitudSchema(many=True).dump(cotizaciones_pendientes)
    cotizaciones_completadas_serializadas = SolicitudCotizacionSchema(many=True).dump(cotizaciones_completadas)

    bandera = ''
    if request.method == "POST":
        bandera = request.form.get('btn-atras')
    
    return rt("cotizaciones.html", cotizaciones_pendientes=cotizaciones_pendientes_serializadas, 
              cotizaciones_completadas=cotizaciones_completadas_serializadas,formatear_id=formatear_id,bandera=bandera)

@bp.route('/aceptar', methods=['POST'])
def aceptar():
    if request.method == "POST":
        # Obtener el id solicitud
        id_solicitud = request.form.get('aceptar__id_solicitud')

        # Se obtiene la solicitud
        solicitud = Solicitud.query.get(id_solicitud)
        #FECHA
        fecha_cotizacion = datetime.now().date()
        #ID_PERSONAL
        id_personal = 1 #por ahora default (se espera al login)
        #IMPORTE
        importe_total=0 #por ahora artificio
        pago = {
            "adm": 500,
            "limp": 300,
            "jar": 300,
            "vig": 400,
        }
        if solicitud.id_servicio == 1:
            total_adm = solicitud.cant_administracion*pago["adm"]
            total_lim = solicitud.cant_plimpieza*pago["limp"]
            total_jar = solicitud.cant_jardineria*pago["jar"]
            total_vig = solicitud.cant_vigilantes*pago["vig"]
            importe_total = total_adm+total_lim+total_jar+total_vig
        elif(solicitud.id_servicio==2):
            total_lim = solicitud.cant_plimpieza*pago["limp"]
            importe_total = total_lim
        elif(solicitud.id_servicio==3):
            total_jar = solicitud.cant_jardineria*pago["jar"]
            importe_total = total_jar
        elif(solicitud.id_servicio==4):
            total_vig = solicitud.cant_vigilantes*pago["vig"]
            importe_total = total_vig
        # Estado activo
        estado = Estado.query.get(1)

        new_solicitud_cotizacion = SolicitudCotizacion(id_solicitud,id_personal,fecha_cotizacion,importe_total,estado.id_estado)
        db.session.add(new_solicitud_cotizacion) # agregación
        db.session.commit() # confirmación
        
        return redirect(url_for('cotizaciones.cotizaciones'))

@bp.route('/rechazar', methods=['POST'])
def rechazar():
    if request.method == "POST":
        id_solicitud = request.form.get('rechazar__id_solicitud')
        print("Rechazado: ",id_solicitud)
        return redirect(url_for('cotizaciones.cotizaciones'))
