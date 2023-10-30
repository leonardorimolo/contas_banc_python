class MensagensSucesso:
    
    def sucesso_saque(valor):
        return f'Saque no valor de {valor} Reais realizado com sucesso'
    
    def sucesso_deposito(valor):
        return f'Depósito no valor de {valor} Reais realizado com sucesso'
    
    def sucesso_taxa_fixa(taxa_fixa,saldo):
         return f'A sua conta foi cobrada em R${taxa_fixa} de taxa de manutenção neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    def sucesso_taxa_saque(taxa_rendimento,saldo):
        return f'A sua conta poupança rendeu um total de R${saldo * taxa_rendimento} neste mês! \n Saldo atual: R$ {saldo:2f}'
    
    def sucesso_criacao_conta(nome,email,limite,tipo_conta):
        return f'Conta {tipo_conta} criada com sucesso! \n Nome: {nome} \n Email: {email} \n Limite: {limite}'
    
    

class MensagensErro:

    def erro_saque(valor):
        return f'Não é possível realizar o saque no valor de {valor}, tente novamente mais tarde'
    
    def saldo_insuficiente_saque(valor):
        return f'Não é possível realizar o saque no valor de {valor}, Saldo insuficiente'
    
    def limite_insuficiente_saque(valor):
        return f'Não é possível realizar o saque no valor de {valor}, Limite insuficiente'
    
    def erro_deposito(valor):
        return f'Não é possível realizar o depósito no valor de {valor}, tente novamente mais tarde'
    
    def email_ja_cadastrado(email,tipo_conta):
        return f'Não é possível realizar o cadastro, o email {email} já está vinculado a uma conta {tipo_conta}'
    



    
    