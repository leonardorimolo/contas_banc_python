class MensagensSucesso:
    
    def sucesso_saque(self,valor):
        return f'Saque no valor de {valor} Reais realizado com sucesso'
    
    def sucesso_deposito(self,valor):
        return f'Depósito no valor de {valor} Reais realizado com sucesso'
    
    def sucesso_taxa_fixa(self,taxa_fixa,saldo):
         return f'A sua conta foi cobrada em R${taxa_fixa} de taxa de manutenção neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    def sucesso_taxa_saque(self,taxa_rendimento,saldo):
        return f'A sua conta poupança rendeu um total de R${saldo * taxa_rendimento} neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    def sucesso_criacao_conta(self,nome,email,tipo_conta):
        return f'Conta {tipo_conta} criada com sucesso! \n Nome: {nome} \n Email: {email}'



class MensagensErro:

    def erro_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor}, tente novamente mais tarde'
    
    def saldo_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor}, Saldo insuficiente'
    
    def limite_insuficiente_saque(self,valor):
        return f'Não é possível realizar o saque no valor de {valor}, Limite insuficiente'
    
    def erro_deposito(self,valor):
        return f'Não é possível realizar o depósito no valor de {valor}, tente novamente mais tarde'
    
    def email_ja_cadastrado(self,email,tipo_conta):
        return f'Não é possível realizar o cadastro, o email {email} já está vinculado a uma conta {tipo_conta}'

    def conta_nao_encontrada(self, email,tipo):
        return f'Não foi possível localizar uma conta {tipo} vinculada ao email {email}, tente novamente mais tarde'





    
    