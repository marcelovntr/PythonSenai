from meus_exemplos_for import (meu_exemplo_range, minha_comparacao, contagem_dois_valores)
from meus_exemplos_while import (meu_contador, minha_senha, meu_break, meu_continue)
def meu_menu():
    print("\nMENU PRINCIPAL:")
    print("\nExemplos com FOR:")
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
        opcao = meu_menu()
        match opcao:
            case '1':
                print("\n=== For com range usando input ===")
                meu_exemplo_range()
            case '2':
                print("\n=== Percorrer lista com comparação ===")
                minha_comparacao()
            case '3':
                print("\n=== Contagem entre dois valores ===")
                contagem_dois_valores()
            case '4':
                print("\n=== While com contador ===")
                meu_contador()
            case '5':
                print("\n=== While verificando senha ===")
                minha_senha()
            case '6':
                print("\n=== While com break ===")
                meu_break()
            case '7':
                print("\n=== While com continue ===")
                meu_continue()
            case '0':
                print("\nPrograma finalizado!")
            case _:
                print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    print("Bem-vindo ao Menu de Exemplos!")
    print("Aqui você encontrará exemplos de loops FOR e WHILE em Python.")
    main()
