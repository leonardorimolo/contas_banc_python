from main.contas_bancarias import Conta_Bancaria
from main.mensagens import MensagensErro,MensagensSucesso


class Corrente(Conta_Bancaria):

    def init(self,saldo:float):
        super().init(saldo)
        self._taxa_mes_fixa = 20.00 #20 Reais

    @property
    def taxa_mes_fixa(self):
        return self._taxa_mes_fixa
    
    @taxa_mes_fixa.setter
    def taxa_mes_fixa(self, nova_taxa_mes_fixa):
        self._taxa_mes_fixa = nova_taxa_mes_fixa

    


    def sacar(self,valor:float):
        return super().sacar(valor,'corrente')
    
    def depositar(self,valor:float):
        return super().depositar(valor)
    
    def fechar_mes(self):
        self.saldo = self.saldo - self.taxa_mes_fixa
        return MensagensSucesso.sucesso_taxa(self.taxa_mes_fixa,self.saldo)
    
    def atualizar_limite(self,novo_limite:float):
        self.limite = novo_limite
        return f'O seu limite foi atualizado para R${self.limite:2f}'