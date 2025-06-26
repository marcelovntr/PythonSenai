
def demonstrar_dicionario():
    """
    Esta função Demonstra operações básicas com dicionários:
    1. Cria nome e idade; 2. Permite modificar via input
    3. Antes e depois das modificações; 4. Trata erros de entrada inválida
    Returns: None
    """
    print("\n=== Demonstração de Dicionários ===")
    print("Um dicionário guarda informações com um nome (chave) e um valor")
    print("Exemplo: nome = 'João', idade = 20")
    
    pessoa = { # Usamos {} para criar um dicionário com valores iniciais
        "nome": "João",  # chave "nome" com valor "João"
        "idade": 20      # Cada par chave-valor é separado por vírgula
    }
    
    print("\nDicionário inicial:")
    print("Nome:", pessoa["nome"])  # chave['valor']
    print("Idade:", pessoa["idade"])
    
    print("\nVamos mudar o nome:") # Solicita e valida a entrada do usuário
    novo_nome = input("Digite um novo nome: ")
    
    pessoa["nome"] = novo_nome # Atualiza o valor da chave "nome"
    print("Nome atualizado para:", pessoa["nome"])
    
    # Modificação da idade
    print("\nVamos mudar a idade:")
    try: # Usa try/except para tratar erros de conversão
        # int() pode gerar ValueError se a entrada não for um número
        nova_idade = int(input("Digite uma nova idade: ")) # Converte a entrada para inteiro
        # Atualiza o valor da chave "idade"
        pessoa["idade"] = nova_idade
        print("Idade atualizada para:", pessoa["idade"])
    except ValueError: # Tratamento de erro para entradas inválidas
        print("Por favor, digite um número para a idade!")
    except Exception as e: # Tratamento de erro geral
        print(f"Erro inesperado: {e}")

    pessoa["funcao"] = "Programador" # Adiciona uma nova chave

    print("\nDicionário final:")
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("Função:", pessoa["funcao"])

# Ponto de entrada do programa
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    demonstrar_dicionario() 