"""
Exemplo simples de operações com números decimais

Este código demonstra operações básicas com números decimais:
- Pede dois números decimais ao usuário
- Faz operações básicas (soma, subtração, multiplicação, divisão)
- Mostra os resultados
"""
import locale

def main():
    try:
        locale.setlocale( locale.LC_ALL, 'pt_BR.UTF-8' )
        # Pedindo dois números decimais
        num1 = float(input("Digite o primeiro número decimal: "))
        valor_formatado = locale.currency(num1, grouping=True, symbol=True)
        print(f"Valor formatado: {valor_formatado}")
        num2 = float(input("Digite o segundo número decimal: "))
        
        # Operações básicas
        print(f"\nResultados:")
        print(f"Soma: {num1 + num2}")
        print(f"Subtração: {num1 - num2}")
        print(f"Multiplicação: {num1 * num2}")
        print(f"Divisão: {num1 / num2}")
        print(f"Quadrado: {num1 ** 2}")
        print(f"Raiz quadrada: {num1 ** 0.5}")
    
    except ValueError:
        print("Erro: Digite números válidos!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main() 