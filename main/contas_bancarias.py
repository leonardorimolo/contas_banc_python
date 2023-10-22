import abc
from main.correntista import Correntista
from main.mensagens import MensagensErro,MensagensSucesso
#from main.historico import Historico

class Conta_Bancaria(abc.ABC):

    def __init__(self,saldo:float,limite:None):
        self._dono = Correntista()
        self._saldo = saldo
        self._id_conta = None # len(lista_de_contas)
        self._historico_da_conta = None #Historico()
        self.limite = limite
    
    @property
    def dono(self):
        return self._dono
    
    @dono.setter
    def dono(self, novo_dono):
        self._dono = novo_dono

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    @property

    def id_conta(self):
        return self._id_conta
    
    @id_conta.setter
    def id_conta(self, novo_id_conta):
        self._id_conta = novo_id_conta

    @property
    def historico_da_conta(self):
        return self._historico_da_conta
    
    @historico_da_conta.setter
    def historico_da_conta(self, novo_historico_da_conta):
        self._historico_da_conta = novo_historico_da_conta
    
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        self._limite = novo_limite



    @abc.abstractmethod
    def sacar(self,valor:float,tipo:str,taxa:None):

        if tipo == 'poupanca':
            if self.saldo >= valor:
                self.saldo = self.saldo - (valor + (valor * taxa)) #taxa de 10%
                return MensagensSucesso.sucesso_saque(valor)

            else:
                return MensagensErro.saldo_insuficiente_saque(valor)
            
        elif tipo == 'cashback':
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo = self.saldo + (valor * taxa) #cashback de 5%
                return MensagensSucesso.sucesso_saque(valor)

            else:
                return MensagensErro.saldo_insuficiente_saque(valor)
        
        elif tipo == 'corrente':
             if self.saldo >= valor:
                self.saldo = self.saldo - valor
                return MensagensSucesso.sucesso_saque(valor)
             
             else:
                 if self.limite >= valor:
                    self.saldo = self.saldo - valor
                    return MensagensSucesso.sucesso_saque(valor) + f'Foi utilizado {valor - self.saldo} Reais do seu limite'
                 
                 else:
                     return MensagensErro.limite_insuficiente_saque
        
    @abc.abstractmethod
    def depositar(self,valor:float):
        self.saldo = self.saldo + valor
        return MensagensSucesso.sucesso_deposito(valor)
        


   
       
