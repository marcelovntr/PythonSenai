"""
Exemplo simples de operações com números inteiros

Este código demonstra operações básicas com números inteiros:
- Pede dois números inteiros ao usuário
- Faz operações básicas (soma, subtração, multiplicação, divisão)
- Mostra os resultados
"""

def main():
    try:
        # Pedindo dois números inteiros
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        
        # Operações básicas
        print(f"\nResultados:")
        print(f"Soma: {num1 + num2}")
        print(f"Subtração: {num1 - num2}")
        print(f"Multiplicação: {num1 * num2}")
        print(f"Divisão: {num1 / num2}")
    
    except ValueError:
        print("Erro: Digite apenas números inteiros!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main() 