import os
from uteis import formata_tamanho

# caminho_procura = r"C:\Users\Derick\Desktop\CV Novo" # no windows precisa utilizar o 'r' antes.
# resolução do erro acima:
# https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')

conta = 0
# raiz = pasta //  diretorios = lista de arquivos/subpastas // arquivos = lista de arquivos
for raiz, diretorios, arquivos in os.walk(caminho_procura):  # walk vasculha dentro do caminho informado.
    for arquivo in arquivos:  # quero ver um arquivo por vez em arquivos (conjunto).
        if termo_procura in arquivo:  # se o termo estiver no arquivo.
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)  # mostra o caminho completo
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)  # separa o nome da extenção
                tamanho = os.path.getsize(caminho_completo)  # tamanho do arquivo em bits
                print()
                print(f'Encontrei o arquivo: {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho: {formata_tamanho(tamanho)}')
            except PermissionError as permissao:
                print(f'Sem permissão de acesso.')
            except FileNotFoundError as notfound:
                print(f'Arquivo não encontrado')
            except Exception as e:
                print(f'Erro desconhecido: {e}')

print()
plural = 's' if conta > 1 else ''
print(f'Total de {conta} arquivo{plural} encontrado{plural}.')
