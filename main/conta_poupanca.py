import main.conta_bancaria as conta_bancaria

class Poupanca(conta_bancaria.Conta_Bancaria):
    
    def __init__(self,saldo:float):
        super().__init__(saldo)
        self._taxa_sob_saque = 0.10 #10%
        self.taxa_rendimento = 0.10 #10%

    
    @property
    def taxa_sob_saque(self):
        return self._taxa_sob_saque
    
    @taxa_sob_saque.setter
    def taxa_sob_saque(self, nova_taxa_sob_saque):
        self._taxa_sob_saque = nova_taxa_sob_saque
    

        
    def sacar(self,valor:float):
        return super().sacar(valor,'poupanca',self.taxa_sob_saque)
    

    def depositar(self,valor:float):
        return super().depositar(valor)
    
    def fechar_mes(self):
        self.saldo = self.saldo + (self.saldo * self.taxa_rendimento)
        return f'A sua conta poupança rendeu um total de R${self.saldo * self.taxa_rendimento:2f} neste mês! \n Saldo atual: R$ {self.saldo:2f}'