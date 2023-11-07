from main.correntista import Correntista
from main.contaCorrente import *

pessoa = Correntista("Lucas Tabelli Berr", "Lucastberr@gmail.com")


def test_criacao():
    conta_da_pessoa = Corrente(pessoa)

    validadando_conta(conta_da_pessoa, pessoa, 0, 0, 0)


def test_limite():
    conta_da_pessoa = Corrente(pessoa)
    # Modificando limite
    conta_da_pessoa.limite = 200

    validadando_conta(conta_da_pessoa, pessoa, 0, 200, 0)

    conta_da_pessoa.limite -= 20

    validadando_conta(conta_da_pessoa, pessoa, 0, 180, 0)

    conta_da_pessoa.limite += 20

    validadando_conta(conta_da_pessoa, pessoa, 0, 200, 0)


def test_saldo():
    conta_da_pessoa = Corrente(pessoa)
    # Depositar
    conta_da_pessoa.saldo += 200

    validadando_conta(conta_da_pessoa, pessoa, 200, 0, 0)

    # Sacar
    conta_da_pessoa.saldo += -99
    validadando_conta(conta_da_pessoa, pessoa, 200, 0, 0)



def validadando_conta(conta, correntista, saldo, limite, limite_gasto):
    assert conta.dono == correntista
    assert conta.saldo == saldo
    assert conta.limite == limite
    assert conta.limite_gasto == limite_gasto