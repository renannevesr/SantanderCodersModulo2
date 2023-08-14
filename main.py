from datetime import datetime, date
from typing import List

clientes = []
medicamentos = []


class Clientes:
    cpfs_utilizados: List[str] = []
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        if self.cpf_utilizado(cpf):
            # print('CPF já cadastrado: ', cpf)
            return
        else:
            self.adicionar_cpf(cpf)
        self._cpf = cpf
        self.nome: str = nome
        self.data_nascimento: date = data_nascimento
        self._idade = int((date.today() - datetime.strptime(data_nascimento, "%Y-%m-%d").date()).days / 365)
    
    @classmethod
    def cpf_utilizado(cls, cpf: str) -> bool:
        if cpf in cls.cpfs_utilizados:
            print('CPF já cadastrado: ', cpf)
            return True
        return False
    
    @classmethod
    def adicionar_cpf(cls, cpf: str) -> None:
        cls.cpfs_utilizados.append(cpf)


    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def setter_cpf(self):
        pass
    
    @property
    def idade(self) -> str:
        return self._idade
    
    @idade.setter
    def setter_idade(self):
        pass

    def adicionar_cliente() -> None:
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o Nome do cliente: ")
        data_nascimento = input("Digite a Data de Nascimento do cliente: ")

        novo_cliente = Clientes(cpf, nome, data_nascimento)
        clientes.append(novo_cliente)

    # def busca_cliente_cpf() -> Clientes:
    #     cpf = input("Digite o CPF do cliente: ")
    #     for cliente in clientes:
    #         if cliente.cpf == cpf:
    #             print(cliente.nome)
    #             return cliente



class Laboratorios():
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.nome: str = nome
        self.endereco: str = endereco
        self.telefone: str = telefone
        self.cidade: str = cidade
        self.estado: str = estado


class Medicamentos():
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float):
        self.nome: str = nome
        self.composto_principal: str = composto_principal
        self.laboratorio: Laboratorios = laboratorio
        self.descricao: str = descricao
        self.valor: float = valor
    
        
class MedicamentosFitoterapicos(Medicamentos):
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float):
        super().__init__(nome, composto_principal, laboratorio, descricao, valor)


class MedicamentosQuimioterapicos(Medicamentos):
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float, receita: bool):
        super().__init__(nome, composto_principal, laboratorio, descricao, valor )
        self.receita: bool = receita



    def adicionar_medicamento() -> None:

            nome = input("Digite o Nome do Medicamento: ")
            composto_principal = input("Digite o Composto Principal do Medicamento: ")
            laboratorio = input("Digite o Laboratório do Medicamento: ")
            descricao = input("Digite a Descrição do Medicamento: ")
            valor = float(input("Digite o valor do Medicamento: "))
            tipo = input("Esse Medicamento é Fitoterápico? (SIM/NÃO) ").upper()
            #Fitoterápico Não Precisa de Receita
            
            controle_tipo = True
            while controle_tipo:
                if tipo == "SIM":
                    novo_medicamento = MedicamentosFitoterapicos(nome, composto_principal, laboratorio, descricao, valor)
                    medicamentos.append(novo_medicamento)
                    controle_tipo = False
                
                elif tipo == "NÃO":
                    receita = input("Esse Medicamento exige Receita? (SIM/NÃO )").upper()

                    controle_receita = True
                    while controle_receita:
                        if receita == 'SIM':
                            novo_medicamento = MedicamentosQuimioterapicos(nome, composto_principal, laboratorio, descricao, valor, True)
                            medicamentos.append(novo_medicamento)
                            controle_receita = False

                        elif receita == 'NÃO':
                            novo_medicamento = MedicamentosQuimioterapicos(nome, composto_principal, laboratorio, descricao, valor, False)
                            medicamentos.append(novo_medicamento)
                            controle_receita = False
                        else:
                            print("Opção Inválida")        
                    controle_tipo = False 
                else:
                    print("Opção Inválida")


    def busca_medicamentos_nome() -> Medicamentos:
        nome = input("Digite o Nome do Medicamento: ")
        for medicamento in medicamentos:
            if medicamento.nome == nome:
                print(medicamento.nome)
                return medicamento

    def busca_medicamentos_laboratorio() -> Medicamentos:
        lista_medicamentos_laboratorio = []
        laboratorio = input("Digite o Laboratório do Medicamento: ")
        for medicamento in medicamentos:
            if medicamento.laboratorio == laboratorio:
                lista_medicamentos_laboratorio.append(medicamento)
                print(medicamento.laboratorio)
                return lista_medicamentos_laboratorio
            
    def busca_medicamentos_descricao() -> Medicamentos:
        lista_medicamentos_descricao = []
        descricao = input("Digite a Descrição do Medicamento: ")
        for medicamento in medicamentos:
            if descricao in medicamento.descricao:
                lista_medicamentos_descricao.append(medicamento)
                print(medicamento.laboratorio)
                return lista_medicamentos_descricao
            


class Relatorios():
    pass


class Vendas():
    def __init__(self, cliente: Clientes, produto_vendido: Medicamentos, qtd: int):
        self._data: datetime = datetime.now()
        self._cliente: Clientes = cliente
        self._produto_vendido: Medicamentos = produto_vendido
        self._qtd: int = qtd
        self._valor_total: float  # Tirei a formula porque estava dando erro usar a função pra ter o valor dessa varável
        ## Se quiserem, podemos tentar colocar self._valor_total: automático com @classmethod

# FUNÇÃO _calculo_valor_total FUNCIONA CORRETAMENTE (TESTEI EM OUTRO ARQUIVO)
# PORÉM NÃO CONSEGUI ENCAIXÁ-LA NO PROJETO, POIS O PROJETO DA DESCONTO NO FINAL DA VENDA
# E A CLASSE VENDA ESTÁ INCLUINDO SOMENTE 1 PRODUTO E NÃO A VENDA COMPLETA 
# VENDA COMPLETA = TODOS OS PRODUTOS DAQUELA VENDA
# FUNÇÃO _calculo_valor_total ESTÁ CALCULANDO O VALOR COM DESCONTO

    def _calculo_valor_total(self):
        # Sorry quem tinha feito essa parte, acabei mudando bastante: ajustei o tema da idade que pediram no comentário e dei uma simplificada na sintaxe
        total_sem_desconto = self._qtd * self._produto_vendido.valor
        desconto_valor = 0.1 if total_sem_desconto > 150.00 else 0.0
        desconto_idade = 0.2 if self._cliente.idade > 65 else 0.0
        desconto_final = max(desconto_valor,desconto_idade)

        total_final = total_sem_desconto - (total_sem_desconto * desconto_final)
        return total_final








### BRENDA NÃO MEXEU ABAIXO (12/08/2023):

def main():
    while True:
        menu_str = """
\nBoas vindas ao nosso sistema:

1 - Inserir Clientes
2 - Inserir Medicamentos
0 - Sair\n
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
        elif opcao == '0':
            print("Saindo do sistema.")
            break

if __name__ == "__main__":
    main()
