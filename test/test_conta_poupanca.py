from main.contaPoupanca import Poupanca

def test_criacao():
    conta_da_pessoa = Poupanca(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    assert conta_da_pessoa.saldo == 0

def test_depositar():
    conta_da_pessoa = Poupanca(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(200)
    assert conta_da_pessoa.saldo == 200

    conta_da_pessoa.depositar(-200)
    assert conta_da_pessoa.saldo == 200

def test_sacar():
    conta_da_pessoa = Poupanca(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(200)

    conta_da_pessoa.sacar(20)

    assert conta_da_pessoa.saldo == 178

    # Sacando valor negativo
    conta_da_pessoa.sacar(-20)
    assert conta_da_pessoa.saldo == 178

    conta_da_pessoa.depositar(20)
    assert conta_da_pessoa.saldo == 198

def test_fechar_mes():
    conta_da_pessoa = Poupanca(nome="Lucas Tabelli Berr", email="lucastberr@gmail.com")

    conta_da_pessoa.depositar(2000)

    conta_da_pessoa.fechar_mes()

    assert conta_da_pessoa.saldo == 2200