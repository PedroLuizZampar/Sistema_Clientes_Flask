from flask import Blueprint, render_template, request
from database.models.cliente import Cliente # Tudo que usar a classe Cliente, está usando os dados da tabela Cliente do banco de dados

cliente_route = Blueprint("cliente", __name__)

"""
Rota da Home:
    -/

Rota de Clientes:
    -> /clientes/ (GET) - Lista os clientes
    -> /clientes/ (POST) - Insere o cliente no servidor (envia os dados do cliente inseridos no formulário especificado logo a baixo)
    -> /clientes/new (GET) - Renderiza o formulário para criar o cliente
    -> /clientes/<id> (GET) - Obtém os dados de um único cliente
    -> /clientes/<id>/edit (GET) - Renderiza um formulário para editar um cliente
    -> /clientes/<id>/update (PUT) - Atualiza os dados do cliente
    -> /clientes/<id>/delete (DELETE) - Deleta o registro do usuário
"""

# GET é o método padrãom então, quando usado, não é preciso referenciá-lo igual os outros métodos

@cliente_route.route('/') # não conflita com o caminho da home (explicação acima)
def lista_clientes():

    """" Renderiza a lista de clientes """

    clientes = Cliente.select()
    return render_template("lista_clientes.html", clientes=clientes)

@cliente_route.route('/', methods=["POST"]) # Informa a rota e o método da requisição
def inserir_cliente():
    
    """ Insere um cliente """
    
    data = request.json # Data é o nome que estou usando para dados

    novo_cliente = Cliente.create(
        nome = data['nome'],
        email = data['email']

    )

    return render_template('item_cliente.html', cliente=novo_cliente)

@cliente_route.route('/new')
def form_cliente():
    
    """ Renderiza o formulário de clientes """

    return render_template("form_cliente.html")

@cliente_route.route('/<int:cliente_id>') # aplica o número inteiro ID para deixar a rota dinâmica
def detalhe_cliente(cliente_id): # variável que informamos na rota e que agora entra como parâmetro da função
    
    """ Visualiza o cadastro do cliente """

    cliente_selecionado = Cliente.get_by_id(cliente_id)

    return render_template("detalhe_cliente.html", cliente=cliente_selecionado)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    
    """ Renderiza o formulário de clientes para editar um cadastro existente """
    
    cliente_selecionado = Cliente.get_by_id(cliente_id)

    return render_template("form_cliente.html", cliente=cliente_selecionado)

@cliente_route.route('/<int:cliente_id>/update', methods=["PUT"])
def atualizar_cliente(cliente_id):
    
    """ Atualiza o cliente com os novos dados informados no formulário """

    # obter dados do formulário de edição
    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)

    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save() # Salva, no banco de dados, o registro feito através do formulário de edição

    # editar cliente
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=["DELETE"])
def deletar_cliente(cliente_id):
    
    """ Apaga um cliente do sistema """
    
    cliente = Cliente.get_by_id(cliente_id) # Quando estamos passando o valor de uma classe para uma variável, estamos instanciando ela
    cliente.delete_instance() # Aqui deletamos a instância

    return {'deleted': 'ok'}