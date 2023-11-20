from datetime import datetime


class Historico():
    def __init__(self, historico:list = []):
        self.data_atual = datetime.today()
        self.historico = historico



    def gravar_operacao(self,data,operacao):
        self.historico.append(f'{data} - {operacao}')



    def __str__(self):
        print(f'Histórico de operações da conta: {self.historico}')

    def guarda_historico(self):
        return self.historico

    def __str__(self) -> str:
        return f"{self.historico}"