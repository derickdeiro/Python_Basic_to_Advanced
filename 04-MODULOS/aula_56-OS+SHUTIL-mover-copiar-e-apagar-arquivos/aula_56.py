import os
import shutil  # responsável por mover e apagar arquivos.

caminho_original = r"C:\Users\Derick\Desktop\CV Novo"
caminho_novo = r'C:\Users\Derick\Desktop\CV Novo2'  # Novo2 é a nova pasta.

try:
    os.mkdir(caminho_novo)  # cria a pasta caso ela não existe ainda.
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_original):  # varrendo na pasta original
# for root, dirs, files in os.walk(caminho_novo):  # criado apenas para apagar os arquivos copiados.
    for file in files:
        old_file_path = os.path.join(root, file)  # o caminho original do arquivo.
        new_file_path = os.path.join(caminho_novo, file)

        shutil.move(old_file_path, new_file_path)  # move os arquivos de um caminho para outro.
        print(f'Arquivo {file} movido com sucesso.')

        # if '.pdf' in file:  # copiando apenas o que tem extensão '.pdf'
        #     shutil.copy(old_file_path, new_file_path)  # copia o arquivo.
        #     print(f'Arquivo {file} copiado com sucesso.')

        # if '.pdf' in file:
        #     os.remove(new_file_path)  # apaga o arquivo selecionado.
        #     print(f'Arquivo {file} apagado com sucesso!')
