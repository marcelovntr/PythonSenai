"""
Menu Principal para Exemplos de Estruturas de Dados em Python
"""

from exemplo_lista import demonstrar_lista
from exemplo_tupla import demonstrar_tupla
from exemplo_conjunto import demonstrar_conjunto
from exemplo_dicionario import demonstrar_dicionario
from exemplo_fila import demonstrar_fila

def exibir_menu():
    print("\n=== Menu de Exemplos de Estruturas de Dados ===")
    print("1. Lista (list)")
    print("2. Tupla (tuple)")
    print("3. Conjunto (set)")
    print("4. Dicionário (dict)")
    print("5. Fila (deque)")
    print("0. Sair")
    return input("\nEscolha uma opção: ")

def main():
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            demonstrar_lista()
        elif opcao == "2":
            demonstrar_tupla()
        elif opcao == "3":
            demonstrar_conjunto()
        elif opcao == "4":
            demonstrar_dicionario()
        elif opcao == "5":
            demonstrar_fila()
        elif opcao == "0":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main() 