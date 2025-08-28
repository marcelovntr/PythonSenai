"""
Exemplos de Loops FOR em Python

Este módulo contém exemplos práticos de diferentes utilizações do loop FOR em Python.

Exemplos implementados:

1. exemplo_range_input():
   - Demonstra o uso do FOR com range() dinâmico
   - Permite ao usuário definir o início e fim da contagem
   - Mostra como usar input() para controlar o range do loop
   - Útil para contagens personalizadas

2. exemplo_lista_comparacao():
   - Ilustra como percorrer uma lista usando FOR
   - Demonstra busca case-insensitive em uma lista
   - Mostra o uso do break para interromper o loop quando encontra o elemento
   - Implementa uma busca simples com feedback de sucesso/falha

3. exemplo_contagem_valores():
   - Mostra como fazer uma contagem entre dois valores
   - Implementa lógica para garantir que a contagem seja sempre crescente
   - Demonstra o uso de variáveis de controle no FOR
   - Inclui tratamento para valores invertidos (troca A e B se necessário)
"""
import time
# Exemplo 1: For simples com range usando input
def exemplo_range_input():
    print("\n=== Exemplo 1: For com range usando input ===")
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: "))
    
    print(f"\nContando de {inicio} até {fim}:")
    for numero in range(inicio, fim + 1):
        print(f"Número: {numero}")

# Exemplo 2: Percorrendo lista com comparação
def exemplo_lista_comparacao():
    print("\n=== Exemplo 2: Percorrendo lista com comparação ===")
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]
    nome_busca = input("Digite um nome para buscar na lista: ").strip()
    nome_busca.capitalize()
    
    print(f"\nBuscando '{nome_busca}' na lista:")
    time.sleep(2)
    encontrado = False
    for nome in nomes:
        if nome.lower() == nome_busca.lower():
            print(f"Nome encontrado: {nome.capitalize()}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Nome '{nome_busca}' não encontrado na lista")

# Exemplo 3: Contagem entre dois valores
def exemplo_contagem_valores():
    print("\n=== Exemplo 3: Contagem entre dois valores ===")
    valor_a = int(input("Digite o primeiro valor (A): "))
    valor_b = int(input("Digite o segundo valor (B): "))
    
    # Garantindo que valor_a seja menor que valor_b
    if valor_a > valor_b:
        valor_a, valor_b = valor_b, valor_a
    
    print(f"\nContando de {valor_a} até {valor_b}:")
    time.sleep(1)
    tempo_inicial = time.time()
    for i in range(valor_a, valor_b + 1):
        print(f"Valor atual: {i}")
    tempo_final = time.time()
    print(f"\nTempo total de execução: {tempo_final - tempo_inicial:.2f} segundos")
# Se este arquivo for executado diretamente, mostra uma mensagem
if __name__ == "__main__":
    print("Demonstração de diferentes usos do FOR em Python")
    print("=" * 50)
    
    exemplo_range_input()
    exemplo_lista_comparacao()
    exemplo_contagem_valores()
