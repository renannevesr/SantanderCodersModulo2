def main():
    while True:
        menu_str = """
\nBoas vindas ao nosso sistema:

1 - Inserir Clientes
2 - Inserir Medicamentos
3 - Sair\n
"""
        print(menu_str)

        option = input("Escolha uma opção: ")
        if option == '1':
            print("opção 1")
        elif option == '2':
            print("opção 2")
        elif option == '3':
            print("Saindo...")
            break



if __name__ == "__main__":
    main()
