from flask import Blueprint
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from flask import make_response

bp = Blueprint('boleta', __name__, url_prefix="/boleta") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/', methods=['GET','POST'])
def generar_pdf():
    # Crear un objeto de lienzo PDF
    buffer = BytesIO()  # Crear un buffer de bytes para almacenar el PDF generado
    pdf = canvas.Canvas(buffer)

    dibujar_encabezado(pdf)
    dibujar_body(pdf)
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
def dibujar_body(pdf):
    pdf.setFont("Helvetica-Bold", 14)
    # Agregar texto al lienzo
    pdf.drawString(100, 750, "Hola, este es un PDF generado dinámicamente.")
    generar_tabla(pdf)

#generar tabla del body
def generar_tabla(pdf):
    # Tus cuatro listas con valores unitarios
    lista1 = [10, 20, 30, 40]
    lista2 = [5, 15, 25, 35]
    lista3 = [8, 18, 28, 38]
    lista4 = [12, 22, 32, 42]
    # Combina las listas utilizando zip()
    data = zip(lista1, lista2, lista3, lista4)
    # Construye la estructura de datos para la tabla
    table_data = [
        ['Id_Servicio', 'Descripción', 'Cantidad', 'Monto (S/)'],  # Nombres de las columnas
    ]
    # Agrega las filas de datos a la estructura de la tabla
    for row in data:
        table_data.append(list(row))
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
    table.wrapOn(pdf, 400, 200)
    table.drawOn(pdf, 100, 500)


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