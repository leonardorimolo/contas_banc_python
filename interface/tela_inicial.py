import sys
import os

# Obtém o diretório do script
script_dir = os.path.dirname(__file__)

# Obtém o diretório do projeto (um nível acima do diretório do script)
project_dir = os.path.abspath(os.path.join(script_dir, '..'))

# Adiciona o diretório do projeto ao PYTHONPATH
sys.path.append(project_dir)

from main.contaPoupanca import Poupanca
from main.contaCorrente import Corrente
from main.contaCashback import Cashback
from main.contaBancaria import ContaBancaria
from main.mensagens import MensagensErro, MensagensSucesso
from main.historico import Historico
from interface.dados import atualiza_arquivo_json
from interface.dados import deletar_conta_json
from interface.dados import lendo_arquivo_json
from interface.dados import fechar_todas_contas

mensagem_erro = MensagensErro()
mensagem_sucesso = MensagensSucesso()



def run_app():
    tela_inicial()

def tela_inicial():
    print("""
    BEM VINDO AO BANCO DA CC

    " 1 " - Criar nova conta
    " 2 " - Buscar conta
    " 3 " - Atualizar os dados da conta
    " 4 " - Deletar conta
    " 5 " - Fechar mês
    " 9 " - Sair
""")
    usuario = opcoes(["1", "2", "3", "4", "5","9"])

    match usuario:
        case "1":
            criar_conta()
            tela_inicial()

        case "2":
            buscar_conta()
            tela_inicial()

        case "3":
            conta = buscar_conta()
            atualizar_dados_conta(conta)
            tela_inicial()

        case "4":
            conta = buscar_conta()
            deletar_conta(conta)
            tela_inicial()

        case "5":
            fechar_mes()
            tela_inicial()

        case "9":
            print("Fechando programa")
            pass

def criar_conta():
    conta = None
    nome = input(str("Digite o nome do dono da conta: "))
    email = input(str("Digite o email do dono da conta: "))

    print("""
               Selecione o tipo de conta que deseja criar:

               " 1 " - Conta Poupança
               " 2 " - Conta Cashback
               " 3 " - Conta Corrente
               " 9 " - Voltar

               """)
    tipo_conta = opcoes(["1", "2", "3", "9"])

    if tipo_conta == "1":
        if verificar_se_conta_existe(email, "Poupança"):
            print(mensagem_erro.email_ja_cadastrado(email=email, tipo_conta= "Poupança"))
            tela_inicial()
        else: 
            conta = Poupanca(nome, email)

    elif tipo_conta == "2":
        if verificar_se_conta_existe(email, "Cashback"):
            print(mensagem_erro.email_ja_cadastrado(email=email, tipo_conta="Cashback"))
            tela_inicial()
        else: 
            conta = Cashback(nome, email)

    elif tipo_conta == "3":
        if verificar_se_conta_existe(email, "Corrente"):
            print(mensagem_erro.email_ja_cadastrado(email=email, tipo_conta="Corrente"))
            tela_inicial()
        else: 
            conta = Corrente(nome, email)

    elif tipo_conta == "9":
        tela_inicial()

    conta.historico_da_conta = Historico([])
    print(conta.criar_conta())

    atualiza_arquivo_json(conta.dicionario())

def verificar_se_conta_existe(email, tipo):
    conta = Corrente(nome="Verificação", email="Verificação")

    if conta.buscar_conta(email, tipo) == mensagem_erro.conta_nao_encontrada(email,tipo=tipo):
        return False 
    else:
        return True

def buscar_conta():
    print("""
           Selecione o tipo de conta que deseja buscar:

           " 1 " - Conta Poupança
           " 2 " - Conta Cashback
           " 3 " - Conta Corrente
           " 9 " - Voltar

           """)
    tipo_conta = opcoes(["1", "2", "3", "9"])

    if tipo_conta == "9":
        tela_inicial()
        return None

    email = input("Digite o email da conta: ")


    if tipo_conta == "1":
        conta = Poupanca(nome=None, email=None)
        conta.buscar_conta(email)

    elif tipo_conta == "2":
        conta = Cashback(nome=None, email=None)
        conta.buscar_conta(email)

    elif tipo_conta == "3":
        conta = Corrente(nome=None, email=None)
        conta.buscar_conta(email)

    elif tipo_conta == "9":
        tela_inicial()
        return None

    # Verifica se a conta existe
    if conta.email != None:
        print(conta)
        print('Essa era a conta desejada: \n " 1 " Sim \n " 2 " Não')
        continuar = opcoes(["1", "2"])
        if continuar == "1":
            return conta
        elif continuar == "2":
            buscar_conta()
    else:
        print("Conta não econtrada, tente novamente")
        buscar_conta()



def atualizar_dados_conta(conta):
    if conta is not None:
        # Se a conta possuir limite
        if conta.tipo_conta == "Corrente":
            atualizar_dados_conta_corrente(conta)

        else:
            print("""
                   Selecione o tipo de dado que deseja atualizar:

                   " 1 " - Sacar
                   " 2 " - Depositar
                   " 9 " - Voltar

                                       """)
            tipo_dado = opcoes(["1", "2", "9"])

            if tipo_dado == "1":
                valor = float(input("Digite o valor que deseja sacar: "))
                print(conta.sacar(valor))

            elif tipo_dado == "2":
                valor = float(input("Digite o valor que deseja depositar: "))
                print(conta.depositar(valor))

            elif tipo_dado == "9":
                buscar_conta()
                return None

        atualiza_arquivo_json(conta.dicionario())


def atualizar_dados_conta_corrente(conta):
    print("""
                           Selecione o tipo de dado que deseja atualizar:

                           " 1 " - Sacar
                           " 2 " - Depositar
                           " 3 " - Limite
                           " 9 " - Voltar

                           """)
    tipo_dado = opcoes(["1", "2", "3", "9"])

    if tipo_dado == "1":
        valor = float(input("Digite o valor que deseja sacar: "))
        print(conta.sacar(valor))

    elif tipo_dado == "2":
        valor = float(input("Digite o valor que deseja depositar: "))
        print(conta.depositar(valor))

    elif tipo_dado == "3":
        valor = float(input("Digite o novo valor do limite: "))
        print(conta.atualizar_limite(valor))

    elif tipo_dado == "9":
        buscar_conta()
        return None

    return conta

def deletar_conta(conta):
    print(f'''Você tem certeza que desejar deletar a conta
{conta}
    " 1 " Sim
    " 2 " Não
    ''')

    resp = opcoes(["1", "2"])

    if resp == "1":
        deletar_conta_json(conta)
    else:
        return


def fechar_mes():
    contas = fechar_todas_contas()
    


def opcoes(list):
    resp = input("R: ")
    while resp not in list:
        print("Resposta inválida, tente novamente")
        resp = input("R: ")

    return resp

if __name__ == "__main__":
    run_app()
    
