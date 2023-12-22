class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []
    
    def cadastrar_cliente(self, cliente):
        self.clientes_cadastrados.append(cliente)
        
        if cliente.idade < 18:
            return 'Cliente menor de idade, não cadastrado'
        
        if not "@" in cliente.email:
            return "Email inválido, não cadastrado"
        
        if len(cliente.nome) < 3:
            return 'Quantidade de caracteres deve ser maior que 3, não cadastrado'
        
        if len(self.clientes_cadastrados) > 0:
            return 'Cadastrado com sucesso'
    