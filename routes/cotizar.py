from flask import Blueprint, render_template as rt, request, flash, redirect, url_for
from src.db import db
from models.contrato import Contrato
from models.predio import Predio
from models.presidentePredio import PresidentePredio
from datetime import datetime

bp = Blueprint('cotizar', __name__,url_prefix="/cotizar")

@bp.route('/')
def cotizar(): #esta función debe coincidir con el url_for
    return rt('cotizar.html')


# Crear una ruta que permita agregar un nuevo contacto a la base de datos
@bp.route('/new', methods=['POST'])
def add_cotizacion():
    if request.method == 'POST':
        # OBTENER LOS DATOS DEL FORMULARIO ENVIADO
        # datos del representante
        dni = request.form['documento']
        apellidos = request.form['apellidos']
        nombres = request.form['nombres']
        predio = request.form['predio']
        telefono = request.form['telefono']
        correo = request.form['correo']
        # datos del predio
        area = request.form['area']
        areas_comunes = request.form['areascomunes']
        NroPuertasAcceso = request.form['NroPuertasAcceso']
        NroHabitaciones = request.form['NroHabitaciones']
        # datos del contrato
        total = request.form['total']
        fecha = datetime.now().date()
        # Crear un nuevo objeto Contact con los datos recibidos del formulario
        new_predio = Predio(area,areas_comunes,NroPuertasAcceso,NroHabitaciones)
        new_contrato = Contrato(total,fecha)
        # Agregar el nuevo contacto a la base de datos y confirmar la operación
        db.session.add(new_predio) # agregación
        db.session.add(new_contrato) # agregación
        db.session.commit() # confirmación
        new_representante = PresidentePredio(new_contrato.id_contrato,new_predio.id_predio,dni,apellidos,
                                             nombres,predio,telefono,correo)
        db.session.add(new_representante) # agregación
        db.session.commit() # confirmación
        # Mostrar un mensaje de éxito en la siguiente petición
        flash('Operación realizada correctamente!')

        # Redirigir a la página principal
        return redirect(url_for('cotizar.cotizar'))