"""
Este módulo demonstra operações básicas com listas em Python:
- Criação e manipulação;- Entrada de dados com validação; - Iteração usando for;- Tratamento de erros

"""

def demonstrar_lista():
    """    
    1. Cria lista vazia -2. adicionar via input -3. lista completa -4. média -5. números maiores que a média
    Returns:
        None
    """
    print("\n=== Demonstração de Listas ===")
    print("Uma lista é como uma coleção de itens em ordem")
    
    # numeros: Inicializa uma lista vazia ([]) e será preenchida durante a execução do programa
    numeros = []
    
    print("\nVamos adicionar alguns números à lista:")
    
    while True:
        try:
            # a) Solicita entrada do usuário; b) lower() para aceitar 'S' ou 's' para sair
            numero = input("\nDigite um número (ou 's' para sair): ")
            if numero.lower() == 's':
                break
            # Cada novo número digitado é convertido para float e adicionado sequencialmente
            numero = float(numero) # Converte a entrada para float 
            numeros.append(numero) # Adiciona o novo número ao final da lista numeros
            print(f"Número {numero} adicionado à lista")
            
        except ValueError: # Tratamento de erro para entradas inválidas
            print("Por favor, digite um número válido!")
    
    # Remove todos os números maiores que 10
    controle = 0
    while controle < len(numeros):
        if numeros[controle] > 10:
            numeros.remove(numeros[controle])
        else:
            controle += 1
    '''  for num in numeros: <--- assim pode pular elementos na remoção!!!
        if num > 10:
            numeros.remove(num) '''
    '''for i, num in enumerate(numeros[:]):  <--- faz uma cópia da lista original, forma mais segura, mas ideal é for de trás pra frente
        if num > 10:
            numeros.remove(num)'''
   
    print("\nNúmeros maiores que 10 foram removidos da lista.")
    # Exibição da lista numeros completa
    print("\nNúmeros na lista:")
    # numeros é iterada c/ enumerate p/ mostrar c/ número c/ seu índice
    for i, num in enumerate(numeros, 1): # enumerate(numeros, 1): Gera pares de (índice, valor) começando do 1 para cada elemento em numeros
        print(f"{i}º: {num}")
    
    # Cálculos e análise da lista numeros
    if numeros:
        # sum(numeros): Soma todos os elementos da lista
        media = sum(numeros) / len(numeros) # len(numeros): Retorna o tamanho total da lista
        print(f"\nMédia dos números: {media:.2f}")
     
        print("\nNúmeros maiores que a média:")
        for num in numeros:
            if num > media:
                print(f"- {num}")
    else:
        print("\nNenhum número foi adicionado à lista!")

# Ponto de entrada do programa
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    demonstrar_lista() 