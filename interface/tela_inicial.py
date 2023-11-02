

def run_app():
    tela_inicial()
    
def tela_inicial():
    print("""
    BEM VINDO AO BANCO DA CC
          
    " 1 " - Criar nova conta
    " 2 " - Buscar conta
    " 3 " - Atualizar os dados da conta
    " 4 " - Deletar conta
""")
    usuario = input("R:")
    