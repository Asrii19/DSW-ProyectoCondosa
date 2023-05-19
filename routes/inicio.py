from flask import Blueprint, render_template as rt

bp = Blueprint('index', __name__) #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def index(): #esta función debe coincidir con el url_for del html (base)
    return rt("index.html") #El rendertemplate siempre buscará el archivo en templates