clientes = []
class Clientes:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


def adicionar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o Nome do cliente: ")
    data_nascimento = input("Digite a Data de Nascimento do cliente: ")

    novo_cliente = Clientes(cpf, nome, data_nascimento)
    clientes.append(novo_cliente)

def busca_cliente_cpf():
    cpf = input("Digite o CPF do cliente: ")
    for cliente in clientes:
        if cliente.cpf == cpf:
            print(cliente.nome)
            return cliente
class MedicamentosFitoterapicos():
    def __init__(self, nome, composto_principal, laboratorio, descricao):
        self.nome = nome
        self.composto_principal = composto_principal
        self.laboratorio = laboratorio
        self.descricao = descricao

# class MedicamentosQuimioterapicos(MedicamentosFitoterapicos):
#     def __init__(self, nome, composto_principal, laboratorio, descricao):
#         MedicamentosFitoterapicos.__init__(self, nome = nome, composto_principal = composto_principal, laboratorio = laboratorio, descricao = descricao, necessita_receita)
     #   self.necessita_receita = necessita_receita




def main():
    while True:
        menu_str = """
\nBoas vindas ao nosso sistema:

1 - Inserir Clientes
2 - Inserir Medicamentos
3 - Sair\n
"""
        print(menu_str)

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            busca_cliente_cpf()  
        elif opcao == '3':
            print("Clientes\/")
            print(clientes[0].cpf, clientes[0].nome, clientes[0].data_nascimento)

        elif opcao == '3':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
