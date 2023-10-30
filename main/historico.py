from datetime import datetime


class Historico():
    def __init__(self):
        self.data_atual = datetime.today()
        self.historico = []



    def gravar_operacao(self,data,operacao):
        self.historico.append(f'{data} - {operacao}')



    def __str__(self):
        print(f'Histórico de operações da conta: {self.historico}')

