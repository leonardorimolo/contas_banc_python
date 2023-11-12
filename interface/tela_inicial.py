from main.contaPoupanca import Poupanca
from main.contaCorrente import Corrente
from main.contaCashback import Cashback
from main.mensagens import MensagensErro, MensagensSucesso

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
    " 9 " - Sair
""")
    usuario = input("R:")

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
            pass

        case "9":
            print("Fechando programa")
            pass

def criar_conta():
    nome = input(str("Digite o nome do dono da conta: "))
    email = input(str("Digite o email do dono da conta: "))

    print("""
               Selecione o tipo de conta que deseja criar:

               " 1 " - Conta Poupança
               " 2 " - Conta Cashback
               " 3 " - Conta Corrente
               " 4 " - Voltar

               """)
    tipo_conta = input("R:")

    if tipo_conta == "1":
        poupanca = Poupanca(nome, email, tipo_conta='Poupanca', limite=None)
        poupanca.criar_conta()
        return poupanca

    elif tipo_conta == "2":
        cashback = Cashback(nome, email, tipo_conta='Cashback', limite=None)
        cashback.criar_conta()
        return cashback

    elif tipo_conta == "3":
        limite = float(input("Digite o limite da conta: "))
        corrente = Corrente(nome, email, tipo_conta='Corrente', limite=limite)
        corrente.criar_conta()
        return corrente

    elif tipo_conta == "4":
        tela_inicial()
        return None

    else:
        print("Opção inválida, tente novamente")
        return None

def buscar_conta():
    print("""
           Selecione o tipo de conta que deseja buscar:

           " 1 " - Conta Poupança
           " 2 " - Conta Cashback
           " 3 " - Conta Corrente
           " 4 " - Voltar

           """)
    tipo_conta = input("R:")
    email = input("Digite o email da conta: ")

    if tipo_conta == "1":
        poupanca = Poupanca(nome=None, email=None, tipo_conta='Poupanca', limite=None)
        poupanca.buscar_conta(email)
        return poupanca

    elif tipo_conta == "2":
        cashback = Cashback(nome=None, email=None, tipo_conta='Cashback', limite=None)
        cashback.buscar_conta(email)
        return cashback

    elif tipo_conta == "3":
        corrente = Corrente(nome=None, email=None, tipo_conta='Corrente', limite=None)
        corrente.buscar_conta(email)
        return corrente

    elif tipo_conta == "4":
        tela_inicial()
        return None

    else:
        print("Opção inválida, tente novamente")
        return None


def atualizar_dados_conta(conta):

    if conta is not None:
        print("""
                   Selecione o tipo de dado que deseja atualizar:

                   " 1 " - Sacar
                   " 2 " - Depositar
                   " 3 " - Limite
                   " 4 " - Voltar

                   """)
        tipo_dado = input("R:")

        if tipo_dado == "1":
            valor = float(input("Digite o valor que deseja sacar: "))
            conta.sacar(valor)

        elif tipo_dado == "2":
            valor = float(input("Digite o valor que deseja depositar: "))
            conta.depositar(valor)

        elif tipo_dado == "3":
            valor = float(input("Digite o novo valor do limite: "))
            conta.atualizar_limite(valor)

        elif tipo_dado == "4":
            buscar_conta()
            return None

        else:
            print("Opção inválida, tente novamente")



if __name__ == "__main__":
    run_app()
