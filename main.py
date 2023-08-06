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
            print("opção 1")
        elif opcao == '2':
            print("opção 2")
        elif opcao == '3':
            print("Saindo...")
            break

class Clientes:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    

class MedicamentosFitoterapicos():
    def __init__():
        pass


if __name__ == "__main__":
    main()
