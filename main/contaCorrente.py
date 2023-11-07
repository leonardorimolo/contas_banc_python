from datetime import datetime
from main.contaBancaria import ContaBancaria
from main.mensagens import MensagensErro, MensagensSucesso
from main.historico import Historico


class Corrente(ContaBancaria):
    
    TAXA_MES_FIXA = 20.00

    def __init__(self, correntista):
        super().__init__(correntista)
        self._taxa_mes_fixa = Corrente.TAXA_MES_FIXA #20 Reais
        self._tipo_conta = 'corrente'

    @property
    def tipo_conta(self):
        return self._tipo_conta

    @tipo_conta.setter
    def tipo_conta(self, novo_tipo_conta):
        self._tipo_conta = novo_tipo_conta

    @property
    def taxa_mes_fixa(self):
        return self._taxa_mes_fixa

    @taxa_mes_fixa.setter
    def taxa_mes_fixa(self, nova_taxa_mes_fixa):
        self._taxa_mes_fixa = nova_taxa_mes_fixa

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            print(MensagensSucesso.sucesso_saque(valor))
            self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")

        else:
            if self.limite >= valor:
                self.saldo = self.saldo - valor
                self.limite_gasto = self.limite - valor
                print(MensagensSucesso.sucesso_saque(valor) + f', Foi utilizado {valor} Reais do seu limite \n Saldo atual: {self.saldo}')
                self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")

            else:
                print(MensagensErro.limite_insuficiente_saque)

    def depositar(self, valor):
        return super().depositar(valor)

    def fechar_mes(self):
        self.saldo = self.saldo - self.taxa_mes_fixa
        return MensagensSucesso.sucesso_taxa(self.taxa_mes_fixa,self.saldo)

    def atualizar_limite(self,novo_limite:float):
        self.limite = novo_limite
        return f'O seu limite foi atualizado para R${self.limite}'

    def __str__(self):
        return f'Conta Corrente: \n ID: {self.id_conta} \n Dono: {self.dono.nome} {self.dono.email} \n Saldo: {self.saldo} \n Limite da conta: {self.limite} \n Limite gasto: {self.limite_gasto}'

