"""
Exemplo simples de tratamento de erro com input

Este código demonstra o tratamento básico de erros em Python:
1. Usa try/except para capturar erros
2. Pede um número ao usuário usando input()
3. Converte a entrada para inteiro usando int()
4. Trata dois tipos de erros:
   - ValueError: quando o usuário digita algo que não é número
   - Exception: para qualquer outro erro inesperado

Como usar:
1. Execute o programa
2. Digite um número quando solicitado
3. Se digitar algo que não é número, verá uma mensagem de erro
4. Se digitar um número válido, verá o número digitado
"""

def main():
    try:
        # Pedindo um número ao usuário
        numero = int(input("Digite um número: "))
        print(f"Você digitou: {numero}")
    
    except ValueError:
        print("Erro: Por favor, digite um número válido!")
    
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main() 