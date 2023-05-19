from app import crear_app
from src.db import db

app = crear_app()

#   SE VINCULA EL DB CON NUESTRA APP
db.init_app(app)

from models.contrato import Contrato
from models.predio import Predio 
from models.presidentePredio import PresidentePredio

with app.app_context():
        db.create_all()

#   METODO MAIN
if __name__ == '__main__':
    app.run()