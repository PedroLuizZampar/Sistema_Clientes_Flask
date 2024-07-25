from routes.home import home_route # Importa a variável home_route do arquivo home na pasta routes
from routes.cliente import cliente_route # Importa a variável cliente_route do arquivo cliente na pasta routes
from database.database import db # Importa a conexão do banco de dados
from database.models.cliente import Cliente # Importa a tabela Cliente do nosso banco de dados

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route) # prefix = "/"
    app.register_blueprint(cliente_route, url_prefix = "/clientes")

def configure_db():
    db.connect()
    db.create_tables([Cliente])