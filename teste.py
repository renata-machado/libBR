from libbr.layout import Layout
from libbr.widgets import Texto, Entrada, Botao, CaixaSelecao, JanelaPopup


def ao_enviar():
    valores = layout.obter_valores()

    nome = valores.get("nome", "").strip()
    aceitou = valores.get("termos", False)

    if not nome:
        JanelaPopup("Erro", "Por favor, preencha o nome.")
        return

    if not aceitou:
        JanelaPopup("Aviso", "Você deve aceitar os termos para continuar.")
        return

    mensagem = f"Nome: {nome}\nAceitou os termos: {'Sim' if aceitou else 'Não'}"
    JanelaPopup("Dados Recebidos", mensagem)


layout = Layout(
    titulo="Janela de Exemplo",
    tamanho=(400, 200),
    cor_fundo="#DFF6FF",  
    elementos=[
        [Texto("Nome completo:"), Entrada(chave="nome")],
        [CaixaSelecao("Aceito os termos de uso", chave="termos")],
        [Botao("Enviar", ao_enviar)],
    ]
)

layout.rodar()