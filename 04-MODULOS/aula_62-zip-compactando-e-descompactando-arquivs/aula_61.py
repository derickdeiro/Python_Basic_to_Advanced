from zipfile import ZipFile
import os

caminho = r'C:\Users\Derick\Desktop\CV Novo'

with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):  # não varre muitas pastas. Apenas na que foi selecionada.
        caminho_completo = os.path.join(caminho, arquivo)  # caminho completo do arquivo
        zip.write(caminho_completo, arquivo)  # inclui no arquivo zip os arquivos da pasta. Renomeando apenas com o nome

with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():  # lê em forma de lista os arquivos criados na função acima.
        print(arquivo)

with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')  # Cria uma pasta com esse nome e extrai os arquivos nela
