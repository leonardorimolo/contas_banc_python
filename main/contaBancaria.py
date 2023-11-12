import abc
import json

from main.correntista import Correntista
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
        self._lista_de_contas = []
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
    def lista_de_contas(self):
        return self._lista_de_contas

    @lista_de_contas.setter
    def lista_de_contas(self, nova_lista_de_contas):
        self._lista_de_contas = nova_lista_de_contas

    @property
    def tipo_conta(self):
        return self._tipo_conta

    @tipo_conta.setter
    def tipo_conta(self, novo_tipo_conta):
        self._tipo_conta = novo_tipo_conta

    def lendo_arquivo_json(self):
        with open('contas.json', 'r') as arquivo:
            self.lista_de_contas = json.load(arquivo)


    def salvando_arquivo_json(self):
        with open('contas.json', 'w') as arquivo:
            json.dump(self.lista_de_contas, arquivo, indent=4)


    def atualizando_arquivo_json(self, tipo):
        for conta in self.lista_de_contas:
            if conta['Email'] == self.email:
                if tipo == 'sacar' or tipo == 'depositar' or tipo == 'fechar_mes':
                    conta['Saldo'] = str(self.saldo)

                elif tipo == 'limite':
                    conta['Limite'] = str(self.limite)

                self.salvando_arquivo_json()

    @abc.abstractmethod
    def depositar(self, valor: float):
        self.saldo = self.saldo + valor
        print(mensagem_sucesso.sucesso_deposito(valor) + f' \n Saldo atual: {self.saldo}')
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Depósito de R$ {valor}")
        self.atualizando_arquivo_json(tipo='depositar')


    def criar_conta(self):
        self.lendo_arquivo_json()
        tam = len(self.lista_de_contas) + 1
        nova_conta = {
            "ID": str(tam),
            "Correntista": str(self.correntista),
            "Email": str(self.email),
            "Saldo": str(self.saldo),
            "Limite": str(self.limite),
            "Tipo": str(self.tipo_conta)
        }
        self.lista_de_contas.append(nova_conta)
        print(mensagem_sucesso.sucesso_criacao_conta(self.correntista, self.email, self.tipo_conta))
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Criação da conta do {self.email}")

    def buscar_conta(self, email):
        self.lendo_arquivo_json()
        for conta in self.lista_de_contas:
            if conta["Email"] == email:
                print(
                    f'Conta encontrada: \n Correntista: {conta["Correntista"]} \n Email: {conta["Email"]} \n Saldo: {conta["Saldo"]} \n Limite: {conta["Limite"]}')
                self.email = conta["Email"]
                self.saldo = float(conta["Saldo"])
                self.limite = float(conta["Limite"])
                self.correntista = conta["Correntista"]
                self.tipo_conta = conta["Tipo"]
                return conta
        else:
            print(mensagem_erro.conta_nao_encontrada(email,tipo=self.tipo_conta))
            return None
