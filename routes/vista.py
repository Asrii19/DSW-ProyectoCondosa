from flask import Blueprint, render_template as rt, flash, redirect, url_for, request, jsonify
from models.contrato import Contrato
from models.predio import Predio
from models.presidentePredio import PresidentePredio
from utils.db import db
from utils.json import model_to_dict
import json

bp = Blueprint('vista', __name__, url_prefix="/vista") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def vista(): #esta función debe coincidir con el url_for del html (base)
    data=[]
    contrato = Contrato.query.all()
    predio = Predio.query.all()
    representante = PresidentePredio.query.all()
    data = zip(representante, predio, contrato)

    # Crear una lista para almacenar los datos convertidos a json
    for obj1 in contrato:
        data_contrato = model_to_dict(obj1)
    for obj2 in predio:
        data_predio = model_to_dict(obj2)
    for obj3 in representante:
        data_representante = model_to_dict(obj3)
    
    
    result = {
        'contrato': data_contrato,
        'predio': data_predio,
        'presidente_predio': data_representante
    }

    
    
    return jsonify(result)
    #return rt("vista.html",data=data) #El rendertemplate siempre buscará el archivo en templates

@bp.route("/update_predio/<string:id_predio>", methods=["GET", "POST"])
def update_predio(id_predio):
    # Obtener la data correspondiente al id recibido como argumento
    predio = Predio.query.get(id_predio)

    if request.method == "POST":
        # Obtener los nuevos datos del predio desde el formulario y actualizarlos en la base de datos
        predio.area = request.form['update_area']
        predio.areas_comunes = request.form['update_areascomunes']
        predio.NroPuertasAcceso = request.form['update_NroPuertasAcceso']
        predio.NroHabitaciones = request.form['update_NroHabitaciones']
        db.session.commit()

        # Mostrar un mensaje de éxito en la siguiente petición
        flash('Contact updated successfully!')

        # Redirigir a la página principal
        return redirect(url_for('vista.vista'))

    # Renderizar la página de actualización
    return rt("update_predio.html", predio=predio)

@bp.route("/update_representante/<string:id_representante>", methods=["GET", "POST"])
def update_representante(id_representante):
    # Obtener la data correspondiente al id recibido como argumento
    representante = PresidentePredio.query.get(id_representante)

    if request.method == "POST":
        # Obtener los nuevos datos del predio desde el formulario y actualizarlos en la base de datos
        representante.dni = request.form['update_documento']
        representante.apellidos = request.form['update_apellidos']
        representante.nombres = request.form['update_nombres']
        representante.predio_asignado = request.form['update_predio']
        representante.telefono = request.form['update_telefono']
        representante.correo = request.form['update_correo']
        db.session.commit()

        # Mostrar un mensaje de éxito en la siguiente petición
        flash('Contact updated successfully!')

        # Redirigir a la página principal
        return redirect(url_for('vista.vista'))

    # Renderizar la página de actualización
    return rt("update_representante.html", representante=representante)

@bp.route('/delete/<int:id_representante>/<int:id_predio>/<int:id_contrato>')
def delete(id_representante, id_predio, id_contrato):
    # Obtener el contacto correspondiente al id recibido como argumento
    predio= Predio.query.get(id_predio)
    representante= PresidentePredio.query.get(id_representante)
    contrato= Contrato.query.get(id_contrato)

    # Eliminar el contacto de la base de datos y confirmar la operación
    db.session.delete(representante)
    db.session.commit()
    db.session.delete(contrato)
    db.session.delete(predio)
    db.session.commit()
    # Mostrar un mensaje de éxito en la siguiente petición
    flash('Datos eliminados correctamente!')

    # Redirigir a la página principal
    return redirect(url_for('vista.vista'))