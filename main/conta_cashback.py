from main.contas_bancarias import Conta_Bancaria
from main.mensagens import MensagensErro,MensagensSucesso


class Cashback(Conta_Bancaria):

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
        return super().sacar(valor,'cashback',self.taxa_cashback_sob_saque)
    
    def depositar(self,valor:float):
        return super().depositar(valor)
    
    def fechar_mes(self):
        self.saldo = self.saldo + (self.saldo * self.taxa_rendimento)
        return MensagensSucesso.sucesso_taxa_saque(self.taxa_rendimento,self.saldo)