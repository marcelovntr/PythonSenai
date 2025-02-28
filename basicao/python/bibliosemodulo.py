import os
import datetime
#import pyautogui

print(os.listdir('python'))

print(datetime.date.today())

#pip install "pyautogui"
# se não estão "nativo" no python

lista_arquivos = os.listdir('python')
print(lista_arquivos)

for arquivo in lista_arquivos:
    if '.py' in arquivo:
        if 'yt' in arquivo:
            os.rename(f"python/{arquivo}", f"python/youtubebasico/{arquivo}")
        elif 'dennis' in arquivo:
            os.rename(f"python/{arquivo}", f"python/geralprof/{arquivo}")

#CHATGPT PASSOU ISSO::::::::::::::::::::::::::::::::::::::::::::::::::::
# Criar as pastas de destino se não existirem
os.makedirs('python/youtubebasico', exist_ok=True)
os.makedirs('python/geralprof', exist_ok=True)
        
        
      
os.makedirs('python/pastinha', exist_ok=True)
