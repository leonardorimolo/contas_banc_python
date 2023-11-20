import os
import json


def lendo_arquivo_json():
    caminho_do_arquivo = 'contas.json'

    # Verifica se o arquivo existe
    if not os.path.exists(caminho_do_arquivo):
        print(f"O arquivo {caminho_do_arquivo} não existe. Criando o arquivo.")
        with open(caminho_do_arquivo, 'w') as novo_arquivo:
            json.dump([], novo_arquivo)  # Cria um arquivo JSON vazio
        return []

    # Verifica o tamanho do arquivo para determinar se está vazio
    elif os.path.getsize(caminho_do_arquivo) == 0:
        print("O arquivo está vazio.")
        return []

    else:
        with open(caminho_do_arquivo, 'r') as arquivo:
            return json.load(arquivo)



def salvando_arquivo_json(dados):
    with open('contas.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def atualiza_arquivo_json(conta):
    dados = lendo_arquivo_json()
    conta_econtrada = False
    for conta_dos_dados in dados:
        if conta_dos_dados["Email"] == conta["Email"]:
            conta_econtrada = True
            conta_dos_dados.update(conta)
            break

    if conta_econtrada == False:
        dados.append(conta)

    salvando_arquivo_json(dados)

def deletar_conta_json(conta):
    dados = lendo_arquivo_json()

    # Verifica se a conta existe nos dados
    if any(item["Email"] == conta.email for item in dados):
        # Remove a conta da lista
        dados = [item for item in dados if item["Email"] != conta.email]
        print(f"Conta removida com sucesso.")
        salvando_arquivo_json(dados)
    else:
        print("Conta não encontrada.")


