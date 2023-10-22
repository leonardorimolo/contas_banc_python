import main as conta_bancaria

class Corrente(conta_bancaria.Conta_Bancaria):

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
        return f'A sua conta corrente foi cobrada em R${self.taxa_mes_fixa:2f} de taxa de manutenção neste mês! \n Saldo atual: R$ {self.saldo:2f}'
    
    def atualizar_limite(self,novo_limite:float):
        self.limite = novo_limite
        return f'O seu limite foi atualizado para R${self.limite:2f}'