import abc
from correntista import Correntista
from mensagens import MensagensErro, MensagensSucesso
from historico import Historico
from datetime import datetime

class Conta_Bancaria(abc.ABC):

    def __init__(self):
        self._dono = Correntista(nome='', email='')
        self._saldo = 0
        self._id_conta = 0
        self._historico_da_conta = Historico()
        self._limite = 0
        self._limite_gasto = 0
    
    @property
    def dono(self):
        return self._dono
    
    @dono.setter
    def dono(self, novo_dono):
        self._dono = novo_dono

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    @property
    def id_conta(self):
        return self._id_conta
    
    @id_conta.setter
    def id_conta(self, novo_id_conta):
        self._id_conta = novo_id_conta

    @property
    def historico_da_conta(self):
        return self._historico_da_conta
    
    @historico_da_conta.setter
    def historico_da_conta(self, novo_historico_da_conta):
        self._historico_da_conta = novo_historico_da_conta
    
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        self._limite = novo_limite

    @property
    def limite_gasto(self):
        return self._limite_gasto
    
    @limite_gasto.setter
    def limite_gasto(self, novo_limite_gasto):
        self._limite_gasto = novo_limite_gasto

    @abc.abstractmethod
    def criar_conta(self, nome, email, limite, lista_de_contas, tipo_conta):
        self._dono = Correntista(nome, email)
        self.limite = limite
        self.id_conta = len(lista_de_contas) + 1
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Criação de conta {tipo_conta} para {self.dono.email}")
        print(MensagensSucesso.sucesso_criacao_conta(self.dono.nome, self.dono.email, limite, tipo_conta))

    @abc.abstractmethod
    def depositar(self, valor: float):
        self.saldo = self.saldo + valor
        print(MensagensSucesso.sucesso_deposito(valor) + f' \n Saldo atual: {self.saldo}')
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Depósito de R$ {valor}")



