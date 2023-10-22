class MensagensSucesso:
    
    def sucesso_saque(self,valor):
        return f'Saque no valor de {valor:2f} Reais realizado com sucesso'
    
    def sucesso_deposito(self,valor):
        return f'Depósito no valor de {valor:2f} Reais realizado com sucesso'
    
    def sucesso_taxa_fixa(self,taxa_fixa,saldo):
         return f'A sua conta foi cobrada em R${taxa_fixa:2f} de taxa de manutenção neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    def sucesso_taxa_saque(self,taxa_rendimento,saldo):
        return f'A sua conta poupança rendeu um total de R${saldo * taxa_rendimento:2f} neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    

class MensagensErro:

    def erro_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, tente novamente mais tarde'
    
    def saldo_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, Saldo insuficiente'
    
    def limite_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, Limite insuficiente'
    
    def erro_deposito(self,valor):
        return f'Não é possível realizar o depósito no valor de {valor:2f}, tente novamente mais tarde'
    



    
    