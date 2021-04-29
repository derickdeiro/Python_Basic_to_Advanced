"""
Documentação:
https://pythonhosted.org/PyPDF2/
Mais exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

pip install pypdf2 # virtualenv
pipenv install pypdf2 # pipenv
"""
import PyPDF2
import os

# JUNTAR PDFs
caminho_dos_pdfs = 'pdf'

novo_pdf = PyPDF2.PdfFileMerger()  # Merger uni os PDFs
for root, dirs, files in os.walk(caminho_dos_pdfs):  # raiz, diretórios e arquivos
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')  # leitura em modo de bits
        novo_pdf.append(arquivo_pdf)  # inclui no PdfFileMerger o arquivo.

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:  # escreve em bites
    novo_pdf.write(meu_novo_pdf)  # escreve os bites lidos na variável "novo_pdf"



# SEPARA PDFs
with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)  # lê os arquivos
    num_paginas = leitor.getNumPages()  # pega o número de páginas

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()  # Escreve as páginas
        pagina_atual = leitor.getPage(num_pagina)  # Seleciona o número da página
        escritor.addPage(pagina_atual)  # adiciona uma pagina em um novo

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)  # gera o novo arquivo compilado.
