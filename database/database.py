import os
from peewee import MySQLDatabase
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Conexão com o banco de dados
db = MySQLDatabase(
    os.getenv('NOME_BANCO', ''), # nome do banco
    user=os.getenv('USUARIO', ''), # usuário
    password=os.getenv('SENHA', ''), # senha
    host=os.getenv('HOST', ''), # endereço do servidor
    port=int(os.getenv('PORTA', '')) # porta
)