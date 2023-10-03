from ..main.correntista import Correntista


def test_init():
    usuario = Correntista("Lucas Berr", "lucastberr@gmail.com")

    assert usuario.nome == "Lucas Berr"
    assert usuario.email == "lucastberr@gmail.com"

    usuario.nome = "João Pedro"
    usuario.email = "joaopedro@gmail.com"

    assert usuario.nome == "João Pedro"
    assert usuario.email == "joaopedro@gmail.com"
    

