"""
Exemplo de uso de Conjuntos (Sets) em Python
Demonstração básica para iniciantes
"""

def demonstrar_conjunto():
    print("\n=== Demonstração de Conjuntos ===")
    print("Conjuntos são coleções de itens únicos (sem repetições)")
    
    # Criando um conjunto simples de números
    numeros = {1, 2, 3, 4, 5}
    print("\nConjunto inicial de números:", numeros)
    controle = True
    while controle: #WHILE foi minha adição!!!
        try:
            novo_numero = int(input("\nDigite um número para adicionar ao conjunto: "))
            if novo_numero in numeros:
                print(f"O número {novo_numero} já existe no conjunto!")
            else:
                numeros.add(novo_numero) #<--- ADD p/ conjuntos!!!
                print(f"Após adicionar {novo_numero}:", numeros)
                controle = False
        except ValueError:
            print("Por favor, digite apenas números!")
    
    # Removendo número
    try:
        numero_remover = int(input("\nDigite um número para remover do conjunto: "))
        if numero_remover in numeros:
            numeros.remove(numero_remover)
            print(f"Após remover {numero_remover}:", numeros)
        else:
            print(f"O número {numero_remover} não está no conjunto!")
    except ValueError:
        print("Por favor, digite apenas números!")
    
    # Verificando se um número está no conjunto
    try:
        numero_verificar = int(input("\nDigite um número para verificar se está no conjunto: "))
        if numero_verificar in numeros:
            print(f"Sim! O número {numero_verificar} está no conjunto.")
        else:
            print(f"Não! O número {numero_verificar} não está no conjunto.")
    except ValueError:
        print("Por favor, digite apenas números!")
    
    # Mostrando o conjunto final
    print("\nConjunto final:", numeros)
    print("Quantidade de números no conjunto:", len(numeros))
    
    # Exemplo de como conjuntos removem duplicatas
    print("\nExemplo de como conjuntos removem duplicatas:")
    lista_com_duplicatas = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    conjunto_sem_duplicatas = set(lista_com_duplicatas)
    print("Lista com números repetidos:", lista_com_duplicatas)
    print("Convertendo para conjunto (remove duplicatas):", conjunto_sem_duplicatas)

if __name__ == "__main__":
    demonstrar_conjunto() 