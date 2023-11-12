from main.contaBancaria import ContaBancaria
from main.mensagens import MensagensSucesso, MensagensErro
from datetime import datetime

mensagens_erro = MensagensErro()
mensagens_sucesso = MensagensSucesso()


class Cashback(ContaBancaria):

    def __init__(self, nome, email, tipo_conta, limite):
        super().__init__(nome, email, tipo_conta, limite)
        self._taxa_cashback_sob_saque = 0.05 #5%
        self._taxa_manu_mes = 0.01 #1%


    
    @property
    def taxa_cashback_sob_saque(self):
        return self._taxa_cashback_sob_saque
    
    @taxa_cashback_sob_saque.setter
    def taxa_cashback_sob_saque(self, nova_taxa_cashback_sob_saque):
        self._taxa_cashback_sob_saque = nova_taxa_cashback_sob_saque

        
    def sacar(self,valor:float):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            self.saldo = self.saldo + (valor * self.taxa_cashback_sob_saque) #cashback de 5%
            print(mensagens_sucesso.sucesso_saque(valor))
            self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")
            self.atualizando_arquivo_json(tipo='sacar')

        else:
            print(mensagens_erro.saldo_insuficiente_saque(valor))
    
    def depositar(self,valor:float):
        return super().depositar(valor)


    def fechar_mes(self):
        self.saldo = self.saldo + (self.saldo * self._taxa_manu_mes)
        self.atualizando_arquivo_json(tipo='fechar_mes')
        return mensagens_sucesso.sucesso_taxa_saque(self._taxa_manu_mes,self.saldo)
