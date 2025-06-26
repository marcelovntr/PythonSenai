"""
Este módulo demonstra operações básicas com filas (deque) em Python:
- Criação e manipulação;- Adição e remoção de elementos
- Verificação de fila vazia usando match;
- Atendimento sequencial com delay;- Tratamento de erros
Exemplo de uso:
    python exemplo_fila.py
"""
from collections import deque
import time

def atender_fila(fila):
    """
    Atende todas as pessoas na fila com um intervalo entre atendimentos.
    Esta função:
    1. Verifica se a fila está vazia usando match
    2. Atende cada pessoa sequencialmente
    3. Adiciona um delay entre atendimentos
    4. Mostra o progresso do atendimento 
    Args:
        fila (deque): A fila de pessoas a ser atendida  
    Returns:
        None
    """
    # Usa match para verificar o estado da fila
    # case 0: fila vazia
    # case _: qualquer outro tamanho (tem pessoas na fila)
    match len(fila):
        case 0:
            print("\nNenhuma pessoa foi adicionada à fila!")
        case _:
            print("\nIniciando atendimento:")
            # Loop de atendimento
            # Continua até que a fila esteja vazia
            while fila:
                # Remove e retorna a primeira pessoa da fila
                pessoa_atendida = fila.popleft() # popleft() é mais eficiente que pop(0) para filas
                print(f"\n{pessoa_atendida} foi atendido(a)")
                print("Pessoas restantes na fila:", len(fila))
                # time.sleep() pausa a execução do programa
                time.sleep(2) # delay de 2 segundos
            print("\nTodas as pessoas foram atendidas!")

def demonstrar_fila():
    """
    Esta função:
    1. Cria uma fila vazia;  2. Permite adicionar pessoas via input;
    3. Mostra a fila completa;  4. Atende todas as pessoas
    Returns:
        None
    """
    # Título e explicação inicial
    print("\n=== Demonstração de Fila ===")
    print("Uma fila é como uma fila de pessoas: o primeiro que chega é o primeiro a sair")
    print("Digite '0' para parar de adicionar pessoas")
    
    # deque():estrutura de dados otimizada para operações nas extremidades
    fila = deque()  # Inicialização da fila vazia
    print("\nVamos adicionar pessoas à fila:")
    
    while True: # Loop infinito p/ add pessoas
        nome = input("\nDigite o nome da pessoa (ou '0' para sair): ")
        if nome == '0':
            break
        # Verifica se o nome não está vazio
        # listas vazias são False e c/ itens são True
        if nome.strip():# strip() remove espaços no início e fim
        #nome != '' <-- rola se for string 
        #nome == True <-- só se for boleano
            
            fila.append(nome)# Adiciona a pessoa ao final da fila
            print(f"{nome} foi adicionado à fila")
        else: # ou if not nome ou whatever
            print("Nome inválido! O nome não pode estar vazio.")
    
    # Exibição da fila completa
    print("\nPessoas na fila:")
    for i, pessoa in enumerate(fila, 1): # enumerate() retorna pares de (índice, valor) começando de 1
        print(f"{i}: {pessoa}")

    atender_fila(fila) # Chama o método para atender a fila

if __name__ == "__main__": # Ponto de entrada do programa
    demonstrar_fila() 