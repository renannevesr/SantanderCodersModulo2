from datetime import datetime, date
from typing import List

#### PENDENCIAS ####
### CLIENTES
# RELATORIO CLIENTES ORDEM ALFABETICA
### VENDAS
# RELATORIO DE VENDAS
# QUANTIDADE DE VENDAS NO DIA (DIA É QUANDO ABRE O PROGRAMA ATÉ FECHAR)
# QUANTIDADE DE PESSOAS DIFERENTES ANTENDIDAS
# QTD REMEDIOS FISIO VENDIDOS
# QTD REMEDISO QUIMIO VENDIDOS
# ALERTA PARA PEDIR RECEITA QUANDO FIZER VENDA DE QUIMIO
### MEDICAMENTOS
## BUSCA POR NOME, FABRICANTE OU ??DESCRICAO PARCIAL?? -- if in :
## 

class Clientes:
    clientes = []
    cpfs_utilizados: List[str] = []

    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        if self.cpf_utilizado(cpf):
            return
        else:
            self.adicionar_cpf(cpf)
        self._cpf = cpf
        self.nome: str = nome
        self.data_nascimento: date = data_nascimento
        self._idade = int((date.today() - datetime.strptime(data_nascimento, "%Y-%m-%d").date()).days / 365)
    
    @classmethod
    def relatorio_cliente(cls):
        clientes_ordenados = sorted(Clientes.clientes, key=lambda cliente: cliente.nome)
        for cliente in clientes_ordenados:
            print(f"Nome: {cliente.nome}, CPF: {cliente._cpf}, Data de Nascimento: {cliente.data_nascimento}")

              
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
    
    @property
    def idade(self) -> str:
        return self._idade

    @classmethod
    def adicionar_cliente(cls) -> None:
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o Nome do cliente: ")
        while True:
            data_nascimento = input("Digite a Data de Nascimento do cliente (AAAA-MM-DD): ")
            try:
                teste = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
                break  
            except ValueError:
                print("Formato de data incorreto. Certifique-se de usar o formato AAAA-MM-DD.")

        novo_cliente = Clientes(cpf, nome, data_nascimento)
        Clientes.clientes.append(novo_cliente)


    @classmethod
    def busca_cliente_cpf(cls) -> "Clientes":
        cpf = input("Digite o CPF do cliente: ")
        for cliente in Clientes.clientes:
            if cliente._cpf == cpf:
                print(cliente.nome)
                return cliente

class Laboratorios():
    laboratorios = []
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.nome: str = nome
        self.endereco: str = endereco
        self.telefone: str = telefone
        self.cidade: str = cidade
        self.estado: str = estado

    @classmethod
    def cadastrar_labotarorio(cls, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:
        ja_cadastrado = False
        for lab in cls.laboratorios:
            if nome == lab.nome:
                ja_cadastrado = True
                print(f'O laboratório {nome} já é cadastrado.')
                continue
            else:
                pass
        if not ja_cadastrado:
            novo_lab = cls(nome, endereco, telefone, cidade, estado)
            cls.laboratorios.append(novo_lab)
            print(f'O laboratório {nome} foi cadastrado.')

    @classmethod
    def lista_labotarorios(cls) -> None:
        for lab in cls.laboratorios:
            print(lab)
        return
    
    def __str__(self) -> str:
        return f'Laboratório: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, Cidade: {self.cidade}, Estado: {self.estado}'
    


class Medicamentos():
    medicamentos = []
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float):
        self.nome: str = nome
        self.composto_principal: str = composto_principal
        self.laboratorio: Laboratorios = laboratorio
        self.descricao: str = descricao
        self.valor: float = valor
    
    @classmethod
    def adicionar_medicamento(cls) -> None:
        nome = input("Digite o Nome do Medicamento: ")
        composto_principal = input("Digite o Composto Principal do Medicamento: ")
        laboratorio = input("Digite o Laboratório do Medicamento: ")
        descricao = input("Digite a Descrição do Medicamento: ")
        valor = float(input("Digite o valor do Medicamento: "))
        tipo = input("Esse Medicamento é Fitoterápico? (SIM/NÃO) ").upper()
        # Fitoterápico Não Precisa de Receita
        
        controle_tipo = True
        while controle_tipo:
            if tipo == "SIM":
                novo_medicamento = MedicamentosFitoterapicos(nome, composto_principal, laboratorio, descricao, valor)
                Medicamentos.medicamentos.append(novo_medicamento)
                controle_tipo = False
            
            elif tipo == "NÃO":
                receita = input("Esse Medicamento exige Receita? (SIM/NÃO )").upper()

                controle_receita = True
                while controle_receita:
                    if receita == 'SIM':
                        novo_medicamento = MedicamentosQuimioterapicos(nome, composto_principal, laboratorio, descricao, valor, True)
                        Medicamentos.medicamentos.append(novo_medicamento)
                        controle_receita = False

                    elif receita == 'NÃO':
                        novo_medicamento = MedicamentosQuimioterapicos(nome, composto_principal, laboratorio, descricao, valor, False)
                        Medicamentos.medicamentos.append(novo_medicamento)
                        controle_receita = False
                    else:
                        print("Opção Inválida")        
                controle_tipo = False 
            else:
                print("Opção Inválida")

    @classmethod
    def busca_medicamentos_nome() -> "Medicamentos":
        nome = input("Digite o Nome do Medicamento: ")
        for medicamento in Medicamentos.medicamentos:
            if medicamento.nome == nome:
                print(medicamento.nome)
                return medicamento
    
    @classmethod
    def busca_medicamentos_laboratorio() -> "Medicamentos":
        lista_medicamentos_laboratorio = []
        laboratorio = input("Digite o Laboratório do Medicamento: ")
        for medicamento in Medicamentos.medicamentos:
            if medicamento.laboratorio == laboratorio:
                lista_medicamentos_laboratorio.append(medicamento)
                print(medicamento.laboratorio)
                return lista_medicamentos_laboratorio
            
    @classmethod     
    def busca_medicamentos_descricao() -> "Medicamentos":
        lista_medicamentos_descricao = []
        descricao = input("Digite a Descrição do Medicamento: ")
        for medicamento in Medicamentos.medicamentos:
            if descricao in medicamento.descricao:
                lista_medicamentos_descricao.append(medicamento)
                print(medicamento.laboratorio)
                return lista_medicamentos_descricao
    
    @classmethod
    def cadastrar_medicamento(cls, nome: str, composto_principal: str,
                              laboratorio: Laboratorios, descricao: str, valor: float) -> None:
        novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor)
        cls.medicamentos.append(novo_medicamento)
        print(f'O medicamento {nome} foi cadastrado.')
        return 

    @classmethod
    def lista_medicamentos(cls) -> None:
        print('\nLISTA DE MEDICAMENTOS\n')
        for medicamento in cls.medicamentos:
            print(medicamento)

    def __str__(self) -> str:
        return f'Medicamento: {self.nome}, Composto Principal: {self.composto_principal}, ' \
               f'Laboratório: {self.laboratorio.nome}, Descrição: {self.descricao}, Valor: {self.valor}'
          
class MedicamentosFitoterapicos(Medicamentos):
    lista_fito = []
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float):
        super().__init__(nome, composto_principal, laboratorio, descricao, valor)

    

    @classmethod
    def cadastrar_med_fito(cls, nome: str, composto_principal: str,
                              laboratorio: Laboratorios, descricao: str, valor: float) -> None:
        novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor)
        cls.medicamentos.append(novo_medicamento)
        cls.lista_fito.append(novo_medicamento)
        # Medicamentos.medicamentos.append(novo_medicamento)
        print(f'O medicamento {nome} foi cadastrado.')
        return 
    
    @classmethod
    def lista_med_fito(cls) -> None:
        print('\nLISTA DE FITOTERAPICOS\n')
        for fito in cls.lista_fito:
            print(fito)

    def __str__(self) -> str:
        return f'Medicamento: {self.nome}, Composto Principal: {self.composto_principal}, ' \
                f'Laboratório: {self.laboratorio.nome}, Descrição: {self.descricao}, Valor: {self.valor}'

class MedicamentosQuimioterapicos(Medicamentos):
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float, receita: bool):
        super().__init__(nome, composto_principal, laboratorio, descricao, valor )
        self.receita: bool = receita

    @classmethod
    def cadastrar_med_quimio(cls, nome: str, composto_principal: str,
                              laboratorio: Laboratorios, descricao: str, valor: float, receita: bool) -> None:
        novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor, receita)
        cls.medicamentos.append(novo_medicamento)
        cls.lista_quimio.append(novo_medicamento)
        print(f'O medicamento {nome} foi cadastrado.')
        return 
    
    @classmethod
    def lista_med_quimio(cls) -> None:
        print('\nLISTA DE FITOTERAPICOS\n')
        for fito in cls.lista_quimio:
            print(fito)

    def __str__(self) -> str:
        return f'Medicamento: {self.nome}, Composto Principal: {self.composto_principal}, Laboratório: {self.laboratorio.nome}, ' \
                f'Descrição: {self.descricao}, Valor: {self.valor}, Precisa de receita: {"Sim" if self.receita else "Nâo"}'

class Vendas():
    vendas_registradas = [] #lista das vendas registradas
    _produtos_vendidos = []
        # def __init__(self, cliente: Clientes, produto_vendido: Medicamentos, qtd: int):
    def __init__(self, cliente: Clientes):
        self._data: datetime = datetime.now()
        self._cliente: Clientes = cliente
        self._itens_vendidos : list= [] 
        # self._produto_vendido: list[Medicamentos] = []
        self._qtd: list = []
        self._valor_total: float = 0.0
        # Tirei a formula porque estava dando erro usar a função pra ter o valor dessa varável
        ## Se quiserem, podemos tentar colocar self._valor_total: automático com @classmethod

# FUNÇÃO _calculo_valor_total FUNCIONA CORRETAMENTE (TESTEI EM OUTRO ARQUIVO)
# PORÉM NÃO CONSEGUI ENCAIXÁ-LA NO PROJETO, POIS O PROJETO DA DESCONTO NO FINAL DA VENDA
# E A CLASSE VENDA ESTÁ INCLUINDO SOMENTE 1 PRODUTO E NÃO A VENDA COMPLETA 
# VENDA COMPLETA = TODOS OS PRODUTOS DAQUELA VENDA
# FUNÇÃO _calculo_valor_total ESTÁ CALCULANDO O VALOR COM DESCONTO

    @classmethod
    def _calculo_valor_total(self):
        total_sem_desconto = sum(qtd * produto.valor for produto, qtd in self._itens_vendidos)
        desconto_valor = 0.1 if total_sem_desconto > 150.00 else 0.0
        desconto_idade = 0.2 if self._cliente.idade > 65 else 0.0
        desconto_final = max(desconto_valor, desconto_idade)

        total_final = total_sem_desconto - (total_sem_desconto * desconto_final)
        return total_final

    @classmethod
    def adicionar_produto_vendido(self, produto_vendido: Medicamentos, qtd: int):
        self._itens_vendidos.append((produto_vendido, qtd))
        self._valor_total = self._calculo_valor_total()
    # def adicionar_produto_vendido(self, produto_vendido: Medicamentos, qtd: int):
    #         # self._produtos_vendidos.append(produto_vendido)
    #         Vendas._produtos_vendidos.append(produto_vendido)
    #         self.qtd.append(qtd)
    #         self.valor_total = self._calculo_valor_total()
    # @property
    # def valor_total(self) -> float:
    #     return self._valor_total
    # @property
    # def produtos_vendidos(self) -> List[Medicamentos]:
    #     return self._produtos_vendidos
    # @property
    # def qtd(self) -> List[ int ]:
    #     return self._qtd
    
    def registrar_venda(self) -> None:
        Vendas.vendas_registradas.append(self)
        print("Venda registrada!")
        return

def seed():
    # medicamentos_quimioterapicos = [
    #     Medicamentos("Medicamento1", "Composto1", "LaboratorioA", "Descrição do medicamento 1", 10.00),
    #     Medicamentos("Medicamento2", "Composto2", "LaboratorioB", "Descrição do medicamento 2", 20.00),
    #     Medicamentos("Medicamento3", "Composto3", "LaboratorioC", "Descrição do medicamento 3", 30.00),
    #     Medicamentos("Medicamento4", "Composto4", "LaboratorioD", "Descrição do medicamento 4", 40.00),
    #     Medicamentos("Medicamento5", "Composto5", "LaboratorioE", "Descrição do medicamento 5", 50.00)
    # ]
    
    # Medicamentos.medicamentos.extend(medicamentos_quimioterapicos)
    Laboratorios.cadastrar_labotarorio('Lab01', 'Rua 001', '00000000', 'cidade 001', 'estado 001')
    Laboratorios.cadastrar_labotarorio('Lab02', 'Rua 002', '000000002', 'cidade 002', 'estado 002')
    Laboratorios.cadastrar_labotarorio('Lab03', 'Rua 003', '000000003', 'cidade 003', 'estado 003')
    Laboratorios.cadastrar_labotarorio('Lab04', 'Rua 004', '000000004', 'cidade 004', 'estado 004')
    Laboratorios.cadastrar_labotarorio('Lab05', 'Rua 005', '000000005', 'cidade 005', 'estado 005')
    MedicamentosFitoterapicos.cadastrar_med_fito('Med01', 'Composto A', Laboratorios.laboratorios[0], 'Descrição do medicamento 1', 10.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med02', 'Composto B', Laboratorios.laboratorios[1], 'Descrição do medicamento 2', 15.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med03', 'Composto c', Laboratorios.laboratorios[2], 'Descrição do medicamento 3', 10.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med04', 'Composto D', Laboratorios.laboratorios[3], 'Descrição do medicamento 4', 15.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med05', 'Composto E', Laboratorios.laboratorios[4], 'Descrição do medicamento 5', 10.0)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med06', 'Composto F', Laboratorios.laboratorios[0], 'Descrição do medicamento 6', 10.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med07', 'Composto G', Laboratorios.laboratorios[1], 'Descrição do medicamento 7', 15.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med08', 'Composto H', Laboratorios.laboratorios[2], 'Descrição do medicamento 8', 10.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med09', 'Composto I', Laboratorios.laboratorios[3], 'Descrição do medicamento 9', 15.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med010', 'Composto J', Laboratorios.laboratorios[4], 'Descrição do medicamento 10', 10.0, True)

    clientes_padrao=[
    Clientes("111", "Cliente A", "1990-01-01"),
    Clientes("222", "Cliente C", "1985-05-15"),
    Clientes("333", "Cliente B", "1978-08-20")
    ]
    Clientes.clientes.extend(clientes_padrao)
    
def main():
    

# Lista de Medicamentos Fitoterápicos
    # medicamentos_fitoterapicos = [
    #     Medicamentos("Fitoterapico1", "Composto6", "LaboratorioF", "Descrição do fitoterápico 1", False),
    #     Medicamentos("Fitoterapico2", "Composto7", "LaboratorioG", "Descrição do fitoterápico 2", False),
    #     Medicamentos("Fitoterapico3", "Composto8", "LaboratorioH", "Descrição do fitoterápico 3", False),
    #     Medicamentos("Fitoterapico4", "Composto9", "LaboratorioI", "Descrição do fitoterápico 4", False),
    #     Medicamentos("Fitoterapico5", "Composto10", "LaboratorioJ", "Descrição do fitoterápico 5", False)
    # ]
    seed()

    while True:
        menu_str = """
        \nBoas vindas ao nosso sistema:

        1 - Inserir Clientes
        2 - Inserir Medicamento Fitoterápico
        3 - Inserir Medicamento Quimioterápicos
        4 - Realizar Venda
        5 - Relatório de Vendas
        6 - Relatório de Clientes
        7 - Lista de medicamentos
        8 - Lista de medicamentos Fitoterápicos
        9 - Lista de medicamentos Quimioterápicos 
        0 - Sair\n
        """
        print(menu_str)

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            Clientes.adicionar_cliente()
        elif opcao == '2':
            Medicamentos.adicionar_medicamento()
        elif opcao == '3':
            cliente = Clientes.busca_cliente_cpf()
            if cliente:
                    print("Lista de medicamentos disponíveis para venda:")
                    for idx, medicamento in enumerate(Medicamentos.medicamentos, start=1):
                        print(f"{idx}. {medicamento.nome}")

                    venda = Vendas(cliente)
                    while True:
                        try:
                            num_medicamento = int(input("Digite o número do medicamento a ser vendido (ou 0 para finalizar): "))
                            if num_medicamento == 0:
                                break

                            medicamento_selecionado = Medicamentos.medicamentos[num_medicamento - 1]
                            qtd = int(input("Digite a quantidade: "))

                            venda.adicionar_produto_vendido(medicamento_selecionado, qtd)
                            print("Produto adicionado à venda.")

                        except (ValueError, IndexError):
                            print("Opção inválida. Por favor, tente novamente.")

                    venda.registrar_venda()
        elif opcao == '4':
            pass
        elif opcao == '5':
            Clientes.relatorio_cliente()
        elif opcao == '6':
            Medicamentos.lista_medicamentos()
        elif opcao == '7':
            MedicamentosFitoterapicos.lista_med_fito()
        elif opcao == '8':
            MedicamentosQuimioterapicos.lista_med_quimio()
        elif opcao == '0':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()