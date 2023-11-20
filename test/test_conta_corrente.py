import sys
import os

# Obtém o diretório do script
script_dir = os.path.dirname(__file__)

# Obtém o diretório do projeto (um nível acima do diretório do script)
project_dir = os.path.abspath(os.path.join(script_dir, '..'))

# Adiciona o diretório do projeto ao PYTHONPATH
sys.path.append(project_dir)

from main.contaCorrente import *


def test_criacao():
    conta_da_pessoa = Corrente(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com", limite=200)

    validadando_conta(conta_da_pessoa, 0,200)

def test_saque_limite():
    conta_da_pessoa = Corrente(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com", limite=200)

    conta_da_pessoa.sacar(200)

    validadando_conta(conta_da_pessoa, saldo=-200, limite=0)

    assert conta_da_pessoa.sacar(20) == "Não é possível realizar o saque no valor de 20, Limite insuficiente"

    validadando_conta(conta_da_pessoa, saldo=-200, limite=0)

def test_saque_saldo():
    conta_da_pessoa = Corrente(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(200)

    validadando_conta(conta_da_pessoa, saldo=200, limite=0)

    # Saque de valor negativo
    conta_da_pessoa.sacar(-23)

    validadando_conta(conta_da_pessoa, saldo=200, limite=0)


    # Saque normal
    conta_da_pessoa.sacar(20)

    validadando_conta(conta_da_pessoa, saldo=180, limite=0)

    # Saque excesso
    conta_da_pessoa.sacar(220)

    validadando_conta(conta_da_pessoa, saldo=180, limite=0)


def test_depositar():
    conta_da_pessoa = Corrente(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(-124)

    validadando_conta(conta_da_pessoa, 0, 0)

    conta_da_pessoa.depositar(124)
    validadando_conta(conta_da_pessoa, 124, 0)



def test_taxa_fixa():
    conta_da_pessoa = Corrente(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(200)

    conta_da_pessoa.fechar_mes()
    validadando_conta(conta_da_pessoa, 180, 0)

    # Testando fechamento de mês com limite
    conta_da_pessoa.sacar(180)
    conta_da_pessoa.atualizar_limite(20)
    conta_da_pessoa.fechar_mes()

    validadando_conta(conta_da_pessoa, -20, 0)


def validadando_conta(conta, saldo, limite):
    assert conta.saldo == saldo
    assert conta.limite == limite

