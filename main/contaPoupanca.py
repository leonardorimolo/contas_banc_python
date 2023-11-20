from main.contaBancaria import ContaBancaria
from main.mensagens import MensagensSucesso, MensagensErro
from datetime import datetime

mensagens_erro = MensagensErro()
mensagens_sucesso = MensagensSucesso()
class Poupanca(ContaBancaria):

    def __init__(self, nome, email, tipo_conta="Poupança", limite=None):
        super().__init__(nome, email, tipo_conta, limite)
        self._taxa_sob_saque = 0.10  # 10%
        self.taxa_rendimento = 0.10  # 10%

    @property
    def taxa_sob_saque(self):
        return self._taxa_sob_saque

    @taxa_sob_saque.setter
    def taxa_sob_saque(self, nova_taxa_sob_saque):
        self._taxa_sob_saque = nova_taxa_sob_saque

    def sacar(self, valor: float):
        # Checa valor negativo
        if valor < 0:
            return mensagens_erro.erro_saque(valor)

        if self.saldo >= valor:
            self.saldo = self.saldo - (valor + (valor * self.taxa_sob_saque))  # taxa de 10%
            self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")
            return mensagens_sucesso.sucesso_saque(valor)

        else:
            return mensagens_erro.saldo_insuficiente_saque(valor)

    def depositar(self, valor: float):
        return super().depositar(valor)

    def fechar_mes(self):
        self.saldo = self.saldo + (self.saldo * self.taxa_rendimento)
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Fechamento de Mês Saldo atual = {self.saldo}")
        return mensagens_sucesso.sucesso_taxa_saque(self.taxa_rendimento, self.saldo)





