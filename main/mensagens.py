class MensagensSucesso:
    
    def sucesso_saque(self,valor):
        return f'Saque no valor de {valor:2f} Reais realizado com sucesso'
    
    def sucesso_deposito(self,valor):
        return f'Depósito no valor de {valor:2f} Reais realizado com sucesso'
    
    def sucesso_taxa_fixa(self,taxa_fixa,saldo):
         return f'A sua conta foi cobrada em R${taxa_fixa:2f} de taxa de manutenção neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    def sucesso_taxa_saque(self,taxa_rendimento,saldo):
        return f'A sua conta poupança rendeu um total de R${saldo * taxa_rendimento:2f} neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    def sucesso_criacao_conta(self,nome,email,limite,tipo_conta):
        return f'Conta {tipo_conta} criada com sucesso! \n Nome: {nome} \n Email: {email} \n Limite: {limite}'
    
    

class MensagensErro:

    def erro_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, tente novamente mais tarde'
    
    def saldo_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, Saldo insuficiente'
    
    def limite_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor:2f}, Limite insuficiente'
    
    def erro_deposito(self,valor):
        return f'Não é possível realizar o depósito no valor de {valor:2f}, tente novamente mais tarde'
    
    def email_ja_cadastrado(self,email,tipo_conta):
        return f'Não é possível realizar o cadastro, o email {email} já está vinculado a uma conta {tipo_conta}'
    



    
    