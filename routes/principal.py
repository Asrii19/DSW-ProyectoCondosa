from flask import Blueprint, render_template as rt, redirect, url_for

bp = Blueprint('principal', __name__, url_prefix="/principal") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def principal():
    return rt("principal.html")