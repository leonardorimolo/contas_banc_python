import sys
import os

# Obtém o diretório do script
script_dir = os.path.dirname(__file__)

# Obtém o diretório do projeto (um nível acima do diretório do script)
project_dir = os.path.abspath(os.path.join(script_dir, '..'))

# Adiciona o diretório do projeto ao PYTHONPATH
sys.path.append(project_dir)

from main.contaCashback import Cashback

def test_criar_conta():
    conta_da_pessoa = Cashback(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    validadando_conta(conta_da_pessoa, 0)

def test_depositar():
    conta_da_pessoa = Cashback(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(2100)

    validadando_conta(conta_da_pessoa, 2100)

    conta_da_pessoa.depositar(-2100213)

    validadando_conta(conta_da_pessoa, 2100)


def test_saque():
    conta_da_pessoa = Cashback(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(200)

    conta_da_pessoa.sacar(200)

    validadando_conta(conta_da_pessoa, 10)

def test_fechamento_mes():
    conta_da_pessoa = Cashback(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(200)

    conta_da_pessoa.fechar_mes()

    validadando_conta(conta_da_pessoa, 198)





def validadando_conta(conta, saldo):
    assert conta.saldo == saldo

