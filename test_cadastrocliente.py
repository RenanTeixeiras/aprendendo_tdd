from Cliente import Cliente
from CadastroCliente import CadastroCliente

def test_que_cliente_seja_cadastrado_com_sucesso():
    cliente = Cliente("Renan",24,"teste@email.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert  "Cadastrado com sucesso" == resposta

def test_que_o_cliente_nao_pode_ser_menor_de_idade():
    cliente = Cliente("Miguel",14,"teste@email.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente menor de idade, não cadastrado" == resposta

def test_que_email_deve_ser_valido():
    cliente = Cliente("Miguel",22,"testeemail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Email inválido, não cadastrado" == resposta

def test_qtd_caracteres():
    cliente = Cliente("Mi",22,"teste@email.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Quantidade de caracteres deve ser maior que 3, não cadastrado" == resposta
