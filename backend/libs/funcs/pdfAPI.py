import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

def gerar_relatorio_valores(nome_arquivo: str, financas: list, caixa: float, pessoa: str, data: str) -> None:
    caminho_pasta = os.path.join(os.path.dirname(__file__), '../../../arquivos')
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo + ".pdf")

    pdf = SimpleDocTemplate(caminho_arquivo, pagesize=letter)

    style_titulo = getSampleStyleSheet()["Heading1"]
    style_titulo.spaceAfter = 20
    style_nome = getSampleStyleSheet()["Heading2"]
    style_nome.spaceAfter = 10

    table_data = []

    titulo = Paragraph(f"<font size=16>{pessoa}</font><br/><font size=14>Relatório Financeiro</font>", style_titulo)
    data = Paragraph(f"<font size=16>{data}</font>", style_titulo)
    table_data.append([titulo, data])

    for fin in financas:
        if fin[4] == "Despesas":
            caixa -= float(fin[2])
        else:
            caixa += float(fin[2] * fin[3])

        nome = Paragraph(f"<font size=14 color=blue>{fin[1]}</font>", style_nome)
        cargo = Paragraph(f"<font size=14 color=blue>{fin[2] * fin[3]}</font>", style_nome)
        table_data.append([nome, cargo])

        table_data.append(["Item:", fin[1]])
        table_data.append(["Valor:", fin[2]])
        table_data.append(["Quantia:", fin[3]])
        table_data.append(["Tipo:", fin[4]])
        table_data.append(["Data:", fin[5]])

    total_label = Paragraph("<font size=14 color=black>Caixa Final</font>", style_nome)

    if caixa < 0:
        color = "red"
    elif caixa == 0:
        color = "black"
    else:
        color = "green"

    valor_label = Paragraph(f"<font size=14 color={color}>{caixa}</font>", style_nome)

    table_data.append([total_label, valor_label])

    style = TableStyle([('GRID', (0, 0), (-1, -1), 1, '#000000')])
    table = Table(table_data)
    table.setStyle(style)
    pdf.build([table])

if __name__ == "__main__":
    pass