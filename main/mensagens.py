class MensagensSucesso:
    
    def sucesso_saque(self,valor):
        return f'Saque no valor de {valor:2f} Reais realizado com sucesso'
    
    def sucesso_deposito(self,valor):
        return f'Depósito no valor de {valor:2f} Reais realizado com sucesso'
    
    



class MensagensErro:

    def erro_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, tente novamente mais tarde'
    
    def saldo_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, Saldo insuficiente'
    
    def limite_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, Limite insuficiente'
    
    def erro_deposito(self,valor):
        return f'Não é possível realizar o depósito no valor de {valor:2f}, tente novamente mais tarde'
    



    
    