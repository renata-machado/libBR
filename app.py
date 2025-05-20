from libbr.core import Janela
from libbr.widgets import Texto, Botao

def ao_clicar():
    print("Você clicou no botão!")

layout = [
    [Texto("Bem-vindo à LibBR!")],
    [Botao("Clique aqui", ao_clicar)]
]

janela = Janela(titulo="Minha Primeira Janela", layout=layout)
janela.iniciar()
