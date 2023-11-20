import abc
import json

from main.historico import Historico
from datetime import datetime
from main.mensagens import MensagensSucesso, MensagensErro

historico = Historico()
mensagem_sucesso = MensagensSucesso()
mensagem_erro = MensagensErro()


class ContaBancaria(abc.ABC):

    def __init__(self, nome, email, tipo_conta, limite: float = None):
        self._correntista = nome
        self._email = email
        self._saldo = 0.0
        self._limite = limite
        self._historico_da_conta = Historico()
        self._tipo_conta = tipo_conta

    @property
    def correntista(self):
        return self._correntista

    @correntista.setter
    def correntista(self, novo_correntista):
        self._correntista = novo_correntista

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

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
    def tipo_conta(self):
        return self._tipo_conta

    @tipo_conta.setter
    def tipo_conta(self, novo_tipo_conta):
        self._tipo_conta = novo_tipo_conta

    def lendo_arquivo_json(self):
        with open('contas.json', 'r') as arquivo:
            return json.load(arquivo)
        

    @abc.abstractmethod
    def depositar(self, valor: float):
        # Checa se valor é maior que zero
        if valor < 0:
            return mensagem_erro.erro_deposito(valor)
        self.saldo = self.saldo + valor
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Depósito de R$ {valor}")
        return mensagem_sucesso.sucesso_deposito(valor) + f' \n Saldo atual: {self.saldo}'

    @abc.abstractmethod
    def criar_conta(self):
        ...

    def buscar_conta(self, email, tipo_conta):
        dados = self.lendo_arquivo_json()
        for conta in dados:
            #print(conta)
            if conta["Email"] == email and conta["Tipo Conta"] == tipo_conta:
                print("\n\nConta encontrada: ")
                print(conta)
                self.email = conta["Email"]
                self.saldo = float(conta["Saldo"])
                if not (conta["Limite"] == None):
                    self.limite = float(conta["Limite"])
                else:
                    self.limite = None
                self.correntista = conta["Nome"]
                self.tipo_conta = conta["Tipo Conta"]
                self.historico_da_conta = Historico(conta["Historico"])
                return conta
            else:
                print(conta)

        else:
            return mensagem_erro.conta_nao_encontrada(email,tipo=tipo_conta)
           

    def __str__(self):
        return f"""\nConta encontrada:   
        Correntista: {self.correntista}
        Email: {self.email}
        Saldo: {self.saldo}
        Limite: {self.limite}
        """

    def dicionario(self):
        return {
            "Nome": self.correntista,
            "Email": self.email,
            "Tipo Conta": self.tipo_conta,
            "Saldo": self.saldo,
            "Limite": self.limite,
            "Historico": self.historico_da_conta.guarda_historico()
        }