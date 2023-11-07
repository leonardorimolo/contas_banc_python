from datetime import datetime
from main.contaBancaria import ContaBancaria
from main.mensagens import MensagensErro,MensagensSucesso
from main.historico import Historico


class Cashback(ContaBancaria):

    def __init__(self,saldo:float):
        super().__init__(saldo)
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
            print(MensagensSucesso.sucesso_saque(valor))
            Historico.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")

        else:
            print(MensagensErro.saldo_insuficiente_saque(valor))
    
    def depositar(self,valor:float):
        return super().depositar(valor)
    
    def fechar_mes(self):
        self.saldo = self.saldo + (self.saldo * self._taxa_manu_mes)
        return MensagensSucesso.sucesso_taxa_saque(self._taxa_manu_mes,self.saldo)