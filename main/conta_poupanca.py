from datetime import datetime
from main.conta_bancaria import Conta_Bancaria
from mensagens import MensagensErro,MensagensSucesso
from historico import Historico

class Poupanca(Conta_Bancaria):
    
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
        if self.saldo >= valor:
            self.saldo = self.saldo - (valor + (valor * self.taxa_sob_saque)) #taxa de 10%
            self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")
            print(MensagensSucesso.sucesso_saque(valor))

        else:
            print(MensagensErro.saldo_insuficiente_saque(valor))
    

    def depositar(self,valor:float):
        return super().depositar(valor)
    
    def fechar_mes(self):
        self.saldo = self.saldo + (self.saldo * self.taxa_rendimento)
        return MensagensSucesso.sucesso_taxa_saque(self.taxa_rendimento,self.saldo)