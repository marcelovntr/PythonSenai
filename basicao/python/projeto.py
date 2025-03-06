#janela para selecionar pasta
import os
#import tkinter.filedialog #abrir janelas no pc
#depois:
#tkinter.filedialog.askdirectory()
from tkinter.filedialog import askdirectory #para importar somente a função desejada
import shutil

pasta_selecionada = askdirectory()
#salva o nome completo/path
print(pasta_selecionada)

lista_arquivos = os.listdir(pasta_selecionada)
print(lista_arquivos)
#backup de arquivos contidos

#1º passo: percorrer todos os arquivos
for arquivo in lista_arquivos:
    print(arquivo)
    nome_completo_arquivo = f"{pasta_selecionada}/{arquivo}"
    print(nome_completo_arquivo)

#º criar a pasta de backup

pasta_backup = 'backup'
pasta_backup_completa = f'{pasta_selecionada}/{pasta_backup}'

if not os.path.exists(pasta_backup_completa):
    os.mkdir(pasta_backup_completa)

for arquivo in lista_arquivos:
    print(arquivo)
    nome_completo_arquivo = f"{pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f'{pasta_backup_completa}/{arquivo}'
   
    if '.' in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
        print(nome_completo_arquivo)
    elif 'backup' != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)