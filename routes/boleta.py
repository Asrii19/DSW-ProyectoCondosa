from flask import Blueprint
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from flask import make_response, request

from models.solicitud import Solicitud
from models.solicitante import Solicitante
from models.persona import Persona
from models.rol import Rol
from models.predio import Predio
from models.tipoPredio import TipoPredio
from models.servicio import Servicio
from models.solicitudCotizacion import SolicitudCotizacion

bp = Blueprint('boleta', __name__, url_prefix="/boleta") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/', methods=['POST'])
def generar_pdf():
    # Crear un objeto de lienzo PDF
    buffer = BytesIO()  # Crear un buffer de bytes para almacenar el PDF generado
    pdf = canvas.Canvas(buffer)
    id_solicitud = request.form.get('descargar__id_solicitud')
    dibujar_encabezado(pdf)
    dibujar_body(pdf,id_solicitud)
    dibujar_footer(pdf)

    # Guardar el lienzo y finalizar el PDF
    pdf.save()

    buffer.seek(0)  # Restablecer el puntero del buffer al principio
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=archivo.pdf'

    return response

# ENCABEZADO
def dibujar_encabezado(pdf):
    # Definir las coordenadas para el encabezado y la línea
    x_encabezado = 50  # posición x del encabezado
    y_encabezado = 800  # posición y del encabezado
    x_linea = 50  # posición x de la línea
    y_linea = y_encabezado - 10  # posición y de la línea (ajusta la separación)
    # Configurar la fuente y el tamaño del texto del encabezado
    pdf.setFont("Helvetica-Bold", 18)
    # Dibujar el encabezado
    pdf.drawString(x_encabezado, y_encabezado, "CONDOSA S.A.")
    # Dibujar la línea
    pdf.setLineWidth(5)  # grosor de la línea
    pdf.setStrokeColorRGB(4/255, 26/255, 47/255) 
    pdf.line(x_linea, y_linea, pdf._pagesize[0] - x_linea, y_linea)  # dibujar línea horizontal

# BODY
def dibujar_body(pdf,id_solicitud):
    pdf.setFont("Helvetica-Bold", 14)
    # Agregar texto al lienzo
    pdf.drawString(100, 750, f"Hola, este es un PDF generado dinámicamente {id_solicitud}.")

    data = obtener_data(id_solicitud)
    generar_tabla(pdf,data)

#generar tabla del body
def generar_tabla(pdf,data):
    administracion =False
    # Tus cuatro listas con valores unitarios
    lista1 = [data["id_servicio"]]
    lista2 = [data["tipo_servicio"]]
    if data["id_servicio"] == 1:
        data["cantidad_total"]=data["cant_administracion"]
        data["importe_total"]=data["importe_administracion"]*data["cantidad_total"]
        administracion=True
    elif(data["id_servicio"]==2):
        data["cantidad_total"]=data["cant_plimpieza"]
        data["importe_total"]=data["importe_plimpieza"]*data["cantidad_total"]
    elif(data["id_servicio"]==3):
        data["cantidad_total"]=data["cant_jardineria"]
        data["importe_total"]=data["importe_jardineria"]*data["cantidad_total"]
    elif(data["id_servicio"]==4):
        data["cantidad_total"]=data["cant_vigilantes"]
        data["importe_total"]=data["importe_vigilantes"]*data["cantidad_total"]

    lista3 = [data["cantidad_total"]]
    lista4 = [data["importe_total"]]
    
    if administracion:
        if(data["cant_plimpieza"]!=0):
            lista1.append("2")
            lista2.append("Limpieza")
            lista3.append(data["cant_plimpieza"])
            lista4.append(data["importe_plimpieza"]*data["cant_plimpieza"])
        if(data["cant_jardineria"]!=0):
            lista1.append("3")
            lista2.append("Jardinería")
            lista3.append(data["cant_jardineria"])
            lista4.append(data["importe_jardineria"]*data["cant_jardineria"])
        if(data["cant_vigilantes"]!=0):
            lista1.append("4")
            lista2.append("Vigilancia")
            lista3.append(data["cant_vigilantes"])
            lista4.append(data["importe_vigilantes"]*data["cant_vigilantes"])
    
    # Combina las listas utilizando zip()
    data = zip(lista1, lista2, lista3, lista4)
    # Construye la estructura de datos para la tabla
    table_data = [
        ['Id_Servicio', 'Descripción', 'Cantidad', 'Monto (S/)'],  # Nombres de las columnas
    ]
    # Agrega las filas de datos a la estructura de la tabla
    for row in data:
        table_data.append(list(row))

    table_data.append(["","","Monto Neto (S/)",round(sum(lista4)*100/118,2)])
    table_data.append(["","","IGV (18%)",round(sum(lista4)*(100/118)*(18/100),2)])
    table_data.append(["","","Monto Total (S/)",sum(lista4)])

    table = Table(table_data, colWidths=100, rowHeights=30)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    table.wrapOn(pdf, 400, 500)
    table.drawOn(pdf, 100, 600-table._height)

#obtener la data para imprimirla
def obtener_data(id_solicitud):
    solicitud = Solicitud.query.get(id_solicitud)
    solicitante = Solicitante.query.get(solicitud.id_solicitante)
    persona = Persona.query.get(solicitante.id_persona)
    rol = Rol.query.get(solicitante.id_rol)
    predio = Predio.query.get(solicitud.id_predio)
    tipo_predio = TipoPredio.query.get(predio.id_tipo_predio)
    servicio = Servicio.query.get(solicitud.id_servicio)
    solicitud_cotizacion = SolicitudCotizacion.query.get(solicitud.id_solicitud)

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
        "cant_administracion": solicitud.cant_administracion,
        "cant_plimpieza": solicitud.cant_plimpieza,
        "cant_jardineria": solicitud.cant_jardineria,
        "cant_vigilantes": solicitud.cant_vigilantes,
        "importe_administracion": 500,
        "importe_plimpieza" : 300,
        "importe_jardineria": 300,
        "importe_vigilantes": 400,
        "cantidad_total": 0
    }
    return data

# FOOTER
def dibujar_footer(pdf):
    pdf.setFont("Helvetica-Bold", 10)
    # Definir las coordenadas para el footer y la línea
    x_footer = 50  # posición x del footer
    y_footer = 50  # posición y del footer
    x_linea = 50  # posición x de la línea
    y_linea = y_footer + 20  # posición y de la línea (ajusta la separación)
    # Dibujar una línea negra encima del footer
    pdf.setLineWidth(5)  # Establecer el ancho de línea
    pdf.setStrokeColorRGB(4/255, 26/255, 47/255)  
    pdf.line(x_linea, y_linea, pdf._pagesize[0] - x_linea, y_linea)  # dibujar línea horizontal
    # Agregar texto al lienzo
    pdf.drawString(x_footer, y_footer, "\u00A9 2023 CONDOSA. Todos los derechos reservados.")