"""
Menu de Exemplos de Loops em Python

Este programa demonstra diferentes exemplos de loops FOR e WHILE em Python através de um menu interativo.

Exemplos com FOR:
1. For com range usando input: Demonstra como usar um loop for com range baseado em input do usuário
2. Percorrer lista com comparação: Mostra como iterar sobre uma lista e fazer comparações
3. Contagem entre dois valores: Ilustra como fazer uma contagem entre dois números usando for

Exemplos com WHILE:
4. While com contador: Demonstra o uso básico de while com um contador
5. While verificando senha: Exemplo de while com verificação de senha
6. While com break: Mostra como usar o break para interromper um loop while
7. While com continue: Ilustra o uso do continue para pular iterações em um loop while
"""

# Importando as funções que vamos usar
from exemplos_for import (
    exemplo_range_input,
    exemplo_lista_comparacao,
    exemplo_contagem_valores
)

from exemplos_while import (
    exemplo_contador,
    exemplo_senha,
    exemplo_break,
    exemplo_continue
)

def exibir_menu():
    print("\nMenu Principal:")
    print("\nExemplos com FOR:")
    print("1 - For com range usando input")
    print("2 - Percorrer lista com comparação")
    print("3 - Contagem entre dois valores")
    print("\nExemplos com WHILE:")
    print("4 - While com contador")
    print("5 - While verificando senha")
    print("6 - While com break")
    print("7 - While com continue")
    print("\n0 - Sair")
    escolha = input("\nDigite o número da opção desejada: ")
    return escolha

def main():
    while True:
        opcao = exibir_menu()
        
        match opcao:
            case '1':
                print("\n=== For com range usando input ===")
                exemplo_range_input()
            case '2':
                print("\n=== Percorrer lista com comparação ===")
                exemplo_lista_comparacao()
            case '3':
                print("\n=== Contagem entre dois valores ===")
                exemplo_contagem_valores()
            case '4':
                exemplo_contador()
            case '5':
                exemplo_senha()
            case '6':
                exemplo_break()
            case '7':
                exemplo_continue()
            case '0':
                print("\nPrograma finalizado!")
                break
            case _:
                print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    print("Bem-vindo ao Menu de Exemplos!")
    print("Aqui você encontrará exemplos de loops FOR e WHILE em Python.")
    main() 