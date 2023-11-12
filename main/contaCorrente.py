from main.contaBancaria import ContaBancaria
from main.mensagens import MensagensSucesso, MensagensErro
from datetime import datetime

mensagem_sucesso = MensagensSucesso()
mensagem_erro = MensagensErro()
class Corrente(ContaBancaria):
    
    TAXA_MES_FIXA = 20.00

    def __init__(self, nome, email, tipo_conta, limite):
        super().__init__( nome, email, tipo_conta, limite)
        self._taxa_mes_fixa = Corrente.TAXA_MES_FIXA #20 Reais


    @property
    def taxa_mes_fixa(self):
        return self._taxa_mes_fixa

    @taxa_mes_fixa.setter
    def taxa_mes_fixa(self, nova_taxa_mes_fixa):
        self._taxa_mes_fixa = nova_taxa_mes_fixa

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            print(mensagem_sucesso.sucesso_saque(valor))
            self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")
            self.atualizando_arquivo_json(tipo='sacar')

        else:
            if self.limite >= valor:
                self.saldo = self.saldo - valor
                self.limite = self.limite - valor
                print(mensagem_sucesso.sucesso_saque(valor) + f', Foi utilizado {valor} Reais do seu limite \n Saldo atual: {self.saldo}')
                self.historico_da_conta.gravar_operacao(data=datetime.now(), operacao=f"Saque de R$ {valor}")
                self.atualizando_arquivo_json(tipo='sacar')
                self.atualizando_arquivo_json(tipo='limite')

            else:
                print(mensagem_erro.limite_insuficiente_saque(valor))

    def depositar(self, valor):
        return super().depositar(valor)



    def fechar_mes(self):
        self.saldo = self.saldo - self.taxa_mes_fixa
        self.atualizando_arquivo_json(tipo='fechar_mes')
        return mensagem_sucesso.sucesso_taxa_fixa(self.taxa_mes_fixa, self.saldo)




    def atualizar_limite(self,novo_limite:float):
        self.limite = novo_limite
        self.atualizando_arquivo_json(tipo='limite')
        return f'O seu limite foi atualizado para R${self.limite}'


