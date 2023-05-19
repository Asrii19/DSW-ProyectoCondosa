from flask import Flask
from src.config import Config

def crear_app():
    app = Flask(__name__)
    #CARGAR CONFIGURACION
    app.config.from_object(Config)
    #BLUEPRINTS
    from routes import inicio
    app.register_blueprint(inicio.bp)
    from routes import cotizar
    app.register_blueprint(cotizar.bp)
    
    return app