# 🐍 __Estudos sobre Flask__
Nesse repositório, ficará documentado todo o conhecimento adquirido sobre o micro framework __Flask__, usado para desenvolvimento web com __Python__!

## 📚 __Bibliotecas__
__1. Flask:__ classe principal do módulo flask.
``` python
# Importação
from flask import Flask
```
__2. url_for:__ usada para montar URLs internas do nosso servidor web de acordo com o nome da função da rota.
``` python
# Importação
from flask import url_for
```
__3. render_template:__ utilizada tanto para buscar na pasta __templates__ os arquivos HTML do site, quanto para enviar variáveis do back-end para o front-end, através das variávis de contexto.
``` python
# Importação
from flask import render_template
```

__4. jinja:__ utilizada para programar em python dentro de um arquivo HTML. Sua importação acontece junto com a classe Flask (item 1 dessa lista). Existem alguns tipos de delimitadores para o Jinja, são eles:
> - __{%...%}__: para __Declarações__ (estruturas do Python como IF, FOR, ...)
> - __{{...}}__: para __Expressões__ (imprime valores de variáveis e aplica expressões como o __url_for()__)
> - __{#...#}__: para __Comentários__  (insere comentários no código)

__5. Blueprint:__ as Flask Blueprints são utilizadas para dividir uma aplicação em módulos menores, o que permite agrupar funcionalidades e organizar melhor o código.
``` python
# Importação
from flask import Blueprint
```

__6. cru.js:__ Uma biblioteca em Javascript onde o objetivo é facilitar as requisições usando apenas o HTML. Documentação detalhada: [https://github.com/Iazzetta/cru.js](https://github.com/Iazzetta/cru.js)

__7. peewee:__ Peewee é um micro ORM (Object Relational Mapping) para Python. É simples, mas possui muitos recursos e é projetado para ser fácil de usar e entender. Para instalar, é preciso o comando:
```bash
pip install peewee
```
Exemplo de uso:
```python
from peewee import SqliteDatabase, Model, CharField

# Conexão com o banco de dados
db = SqliteDatabase('meu_banco.db')

# Definição do modelo
class Usuario(Model):
    nome = CharField()
    email = CharField()

    class Meta:
        database = db

# Conectar e criar tabelas
db.connect()
db.create_tables([Usuario])

# Criar um novo usuário
usuario = Usuario.create(username='pedro', email='pedro@exemplo.com')
```

> Deixo aqui a [Documentação do Peewee](https://docs.peewee-orm.com/en/latest/index.html).

__8. os:__ O módulo os em Python fornece uma maneira de usar funcionalidades dependentes do sistema operacional, como ler ou escrever no sistema de arquivos.
Aqui está um exemplo de como usar o módulo __os__:
```python
import os

# Obter o caminho atual do diretório
caminho_diretorio_atual = os.getcwd()
print(f'O diretório atual é: {caminho_diretorio_atual}')

# Listar arquivos e diretórios no diretório atual
arquivos = os.listdir(caminho_diretorio_atual)
print(f'Arquivos e diretórios no diretório atual: {arquivos}')

# Criar um novo diretório
os.mkdir('novo_diretorio')
```

__9. dotenv:__ O python-dotenv é uma biblioteca que lê o conteúdo de arquivos .env e carrega as variáveis de ambiente especificadas nesse arquivo para o ambiente do sistema.
Para instalar a biblioteca, é preciso o comando:
```bash
pip install python-dotenv
```

Exemplo de uso:
1. crie um arquivo `.env`:
```makefile
NOME_BANCO=my_database
USUARIO=admin
SENHA=senha_secreta
HOST=localhost
PORT=3306
```

2. Use o dotenv para carregar essas variáveis de ambiente no seu script Python:
```python
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
nome_banco = os.getenv('NOME_BANCO')
usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')
host = os.getenv('HOST')
port = int(os.getenv('PORTA'))

print(f'Banco de Dados: {nome_banco}')
print(f'Usuário: {usuario}')
```



## ⚠️ __Conteúdos Importantes__

__1.  HTTP Status Code:__
- <text style="color: cornflowerblue">__1XX__: Informativo</text>
- <text style="color: lightgreen">__2XX__: Confirmação</text>
- <text style="color: khaki">__3XX__: Redirecionamento</text>
- <text style="color: lightcoral">__4XX__: Erro do cliente</text>
- <text style="color: mediumpurple">__5XX__: Erro do servidor</text>

---

__2. Principais HTTP Status Codes__
- <text style="color: lightgreen">__200__</text>: Solicitação bem sucedida, sucesso no método HTTP
- <text style="color: lightcoral">__404__</text>: Recurso não encontrado no servidor
- <text style="color: lightcoral">__405__</text>: Método de solicitação é oconhecido, porém não é suportado na rota informada
- <text style="color: mediumpurple">__500__</text>: Erro interno do servidor

---

__3. Enviando variáveis do back-end para o front-end__
> Usando a biblioteca __render_template__ é possível enviar variáveis do back-end para o front-end. Neste exemplo, a função render_template é usada não apenas para referenciar a página HTML na pasta templates, como passa 2 variáveis contidas no código.
``` python
# Exemplo
titulo = "Olá Mundo"
texto = "Esse é um exemplo de site usando Flask!"
render_template("index.html", titulo=titulo, texto=texto)
```

- Primeiro damos um nome a ela e depois atribuimos o valor da variável em nosso código.
- As variáveis podem ter qualquer nome, desde que sigam as regras para criação de variáveis em python.
- Os parâmetros das variáveis são opcionais.

> Para usar a variável no HTML, usamos o nome da variável entre duas chaves dentro da estrutura HTML. Exemplo:
``` html
<!-- Exemplo -->
<h1>{{ titulo }}</h1>
<p>{{ texto }}</p>
```

---

__4. Utilizando estruturas Python dentro do HTML__

É possível utilizar estruturas do Python dentro do HTML com o __jinja__ como no exemplo abaixo:
``` html
<!-- Exemplo -->
{% for usuario in usuarios %}
    {% if usuario == "Pedro" %}
        <div style="color: lightblue">{{ usuario }}</div>
    {% else %}
        <div>{{ usuario }}</div>
    {% endif %}
{% endfor %}
```

---

__5. Criando rotas com url_for__

A função `__url_for()__` que importamos consegue passar o nome da função de uma rota que criamos e alternar a página que estamos visualizando na aplicação. Observe o exemplo abaixo:

``` html
<!-- Exemplo -->
<a href="{{ url_for('pagina_teste') }}">Página Teste</a>
```

---

__6. Criando e aplicando Blueprints com url_for__

> O trecho de código abaixo define o nome da Blueprint (no caso: cliente) e recebe um parâmetro que é o nome da função que será acessada nesse arquivo

``` python
# Exemplo de criação de uma Blueprint

cliente_route = Blueprint("cliente", __name__)
```

``` html
<!-- Exemplo de uso da Blueprint + url_for (em outro arquivo) -->

<a href="{{ url_for('cliente.deletar_cliente', cliente_id=cliente.id) }}">Deletar</a>
```

> No trecho acima, chamamos a função deletar cliente no arquivo cliente. Essa função deletar possui como parâmetro o cliente_id, que informamos dentro do url_for, que está definido a rota que o programa irá seguir

---

__7. Blueprint + url_for + cru.js__

Essas 3 ferramentas juntas oferecem diversas possibilidades de ações no site, onde a Blueprint organiza as rotas em grupos menores facilitando a compreensão e manutenção do código, a url_for chama as funções determindas na rota e informa os parâmetros dessa função (caso exija) e o cru.js permite requisições diretamente no HTML, evitando contato direto do programador com o JS para ações simples.

``` html
<!-- Exemplo de aplicação -->

<div c-container="{{ url_for('cliente.form_cliente') }}"></div>
```

> A Blueprint cliente é chamada por um url_for, acionando a função form_cliente, que retorna um formulário HTML préviamente estruturado. Esse trecho HTML é renderizado na div por conta do atributo c-container da div, especificado no [cru.js](https://github.com/Iazzetta/cru.js).

## ✔️ __Dicas__
__1.__ No console, após cada requisição, é retornado um LOG, que informa o método utilizado, a rota e o código de status, nessa ordem;

__2.__ Separar o código principal 4 partes principais, __Importações__, __Inicialização__, __Rotas__ e __Execução__
``` python
# Exemplo de Importação
from flask import Flask

# Exemplo de Inicialização
app = Flask(__name__)

# Exemplo de Rotas
@app.route("/exemplo")
def ola_mundo():
    return "Teste"

# Exemplo de Execução
app.run(debug=True)
```
