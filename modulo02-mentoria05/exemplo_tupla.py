"""
Este módulo demonstra operações básicas com tuplas em Python:
- Criação e manipulação;- Acesso por índice;- Desempacotamento de tuplas;
- Iteração usando for e enumerate;- Demonstração de imutabilidade
- Tratamento de erros
"""
def demonstrar_tupla():
    """
    Esta função:
    1. Cria tuplas de coordenadas; 2. Cria novo ponto via input; 3. Demonstra acesso e desempacotamento; 
    4. Mostra iteração sobre tuplas; 5. Demonstra a imutabilidade das tuplas
    Returns:
        None
    """
    print("\n=== Demonstração de Tuplas ===")
    # Inicialização de tuplas de coordenadas (x, y)
    # Tuplas são criadas usando parênteses ()
    ponto_a = (3, 4)  # Ponto A com x=3, y=4
    ponto_b = (5, 2)  # Ponto B com x=5, y=2
    ponto_c = (1, 6)  # Ponto C com x=1, y=6
    
    print("\nCoordenadas dos pontos:")
    print("Ponto A:", ponto_a)
    print("Ponto B:", ponto_b)
    print("Ponto C:", ponto_c)
    
    # Criação de um novo ponto com input do usuário
    try: # Usa try/except para tratar erros de conversão
        print("\nCriando um novo ponto:")
        x = int(input("Digite a coordenada X: ")) # Solicita e converte as coordenadas
        y = int(input("Digite a coordenada Y: ")) # int() pode gerar ValueError se a entrada não for um número
        ponto_d = (x, y) # Cria uma nova tupla com as coordenadas
        print("Novo ponto criado:", ponto_d)
        
        # Cria uma tupla contendo todas as tuplas de pontos
        pontos = (ponto_a, ponto_b, ponto_c, ponto_d) # Tuplas podem conter outras tuplas
    except ValueError: # Tratamento de erro para entradas inválidas
        print("Entrada inválida! Digite números.")
        pontos = (ponto_a, ponto_b, ponto_c) # Se houver erro, cria a tupla sem o ponto D <------ !!!!!!!!!
    
    # Demonstração de acesso a elementos
    # Tuplas são indexadas começando do 0
    print("\nCoordenada X do Ponto A:", ponto_a[0])  # Primeiro elemento
    print("Coordenada Y do Ponto A:", ponto_a[1])    # Segundo elemento
    
    # Demonstração de desempacotamento
    # Atribui os valores da tupla a variáveis separadas
    x, y = ponto_b
    print("\nDesempacotando Ponto B:")
    print(f"X: {x}, Y: {y}")
    
    # Iteração sobre a tupla usando for
    # enumerate() retorna pares de (índice, valor)
    print("\nPercorrendo a tupla de pontos:")
    for i, ponto in enumerate(pontos, 1):
        print(f"Ponto {i}: {ponto}")
    
    # Iteração com desempacotamento aninhado
    # Desempacota tanto o enumerate quanto a tupla de coordenadas
    print("\nPercorrendo com desempacotamento:")
    for i, (x, y) in enumerate(pontos, 1):
        print(f"Ponto {i}: X={x}, Y={y}")
    
    # Demonstração de métodos úteis
    print("\nNúmero de pontos:", len(pontos))  # Tamanho da tupla
    print("Ponto A aparece", pontos.count(ponto_a), "vezes")  # Contagem de ocorrências
    print("Índice do Ponto B:", pontos.index(ponto_b))  # Posição do elemento
    
    # Demonstração da imutabilidade das tuplas
    # Tentativa de modificar um elemento (gerará erro)
    print("\nTentando modificar a tupla (isso gerará um erro):")
    try:
        pontos[0] = (2, 2)  # Tentativa de alterar o primeiro elemento
    except TypeError as e:
        # Tratamento do erro de imutabilidade
        print("Erro:", e)
        print("Tuplas são imutáveis!")  # Explicação do erro

# Ponto de entrada do programa
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    demonstrar_tupla() 