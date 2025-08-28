from minha_verificar_idade import verificar_idade
import meu_imc
from minha_estacao import verificar_estacao
def menu():
    print("Escolha uma opção:")
    print("1 - Opção 1: Verificar idade")
    print("2 - Opção 2: Calcular IMC")
    print("3 - Opção 3: Verificar estação do ano")
    print("0 - Sair")
    return input("Digite a opção desejada: ")
   
def main():
    
    while True:
        opcao = menu()
        match opcao:
                case '1':
                    print('\n verificar idade:')
                    idade_inputada = verificar_idade()
                    print(f"\nResultado: {idade_inputada}")
                case '2':
                    print('\n IMC:')
                    valor_imc = meu_imc.calcular_imc()
                    print(f"Resutaldo do IMC: {valor_imc}")

                case '3':
                    print( '\n estação:')
                    estacao = verificar_estacao()
                    print(f"Estação: {estacao}")

                case '0':
                    print('\n saindo...')
                    break
                case _:
                    print('\n dígito inválido')
        input("\nPressione Enter para continuar...")

    

if __name__ == "__main__":
    main()