from libbr.core import Janela
from libbr.widgets import Texto, Botao

def clique():
    print("Você clicou!")

layout = [
    [Texto("Olá, LibBR!")],
    [Botao("Clique aqui", clique)]
]

janela = Janela(titulo="Exemplo LibBR", layout=layout)
janela.iniciar()
