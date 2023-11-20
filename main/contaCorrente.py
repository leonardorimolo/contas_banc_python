from main.contaBancaria import ContaBancaria
from main.mensagens import MensagensSucesso, MensagensErro
from datetime import datetime

mensagem_sucesso = MensagensSucesso()
mensagem_erro = MensagensErro()


class Corrente(ContaBancaria):
    TAXA_MES_FIXA = 20.00

    def __init__(self, nome, email, tipo_conta="Corrente", limite=0):
        super().__init__(nome, email, tipo_conta, limite)
        self._taxa_mes_fixa = Corrente.TAXA_MES_FIXA  # 20 Reais

    @property
    def taxa_mes_fixa(self):
        return self._taxa_mes_fixa

    @taxa_mes_fixa.setter
    def taxa_mes_fixa(self, nova_taxa_mes_fixa):
        self._taxa_mes_fixa = nova_taxa_mes_fixa

    def sacar(self, valor: float):
        # Checa valor negativo
        if valor < 0:
            return mensagem_erro.erro_saque(valor)
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")
            return mensagem_sucesso.sucesso_saque(valor)
        else:
            if self.limite >= valor:
                self.saldo = self.saldo - valor
                self.limite = self.limite - valor
                self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")
                return (mensagem_sucesso.sucesso_saque(
                    valor) + f', Foi utilizado {valor} Reais do seu limite \n Saldo atual: {self.saldo}')

            else:
                return mensagem_erro.limite_insuficiente_saque(valor)

    def depositar(self, valor):
        return super().depositar(valor)

    def fechar_mes(self):
        self.sacar(self.taxa_mes_fixa)
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Fechamento de Mês Saldo atual = {self.saldo}")
        return mensagem_sucesso.sucesso_taxa_fixa(self.taxa_mes_fixa, self.saldo)

    def atualizar_limite(self, novo_limite: float):
        self.limite = novo_limite
        self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Atualização de Limite =  {self.limite}")
        return f'O seu limite foi atualizado para R${self.limite}'
