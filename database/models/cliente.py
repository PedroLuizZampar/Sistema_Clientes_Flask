import datetime
from peewee import Model, CharField, DateTimeField
from database.database import db # Importa a conexão do banco de dados

class Cliente(Model): # O Peewee já cria um ID automático, por isso não criamos um
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db