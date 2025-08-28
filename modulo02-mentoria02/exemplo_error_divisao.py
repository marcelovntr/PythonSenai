"""
Exemplo simplificado de warnings com try/catch no main
Focado apenas em mostrar mensagens de erro
Usando input para receber o número

EXPLICAÇÃO DETALHADA:

1. O que é 'def'?
   - 'def' é uma palavra-chave em Python que usamos para criar funções
   - É como criar uma caixa que guarda um conjunto de instruções
   - No nosso código, 'def main():' cria uma função chamada 'main'
   - Tudo que está indentado dentro do 'def' faz parte da função
   - Funções são úteis para organizar e reutilizar código

2. O que é 'if __name__ == "__main__":' ?
   - Esta linha verifica se o arquivo está sendo executado diretamente
   - '__name__' é uma variável especial do Python
   - Quando executamos o arquivo diretamente, '__name__' vale "__main__"
   - Quando o arquivo é importado por outro programa, '__name__' vale o nome do arquivo
   - Isso evita que o código seja executado quando o arquivo é importado
   - É uma boa prática de programação em Python

Exemplo prático:
- Se você executar: python exemplo_error_divisao.py
  → __name__ será "__main__" e o código será executado
- Se você importar: import exemplo_error_divisao
  → __name__ será "exemplo_error_divisao" e o código não será executado
"""

import warnings

def main():
    try:
        # Recebendo o número do usuário
        numero = int(input("Digite um número para dividir por zero: "))
        
        # Tentando dividir o número por zero
        resultado = numero / 0
        print(f"Resultado: {resultado}")
    
    except ValueError:
        warnings.warn("Erro: Digite um número válido!")
    
    except ZeroDivisionError:
        warnings.warn("Erro: Divisão por zero!")
        # warnings.warn_explicit("Erro: Divisão por zero!", category=ZeroDivisionError)
        #warn_explicit permite emitir warnings com mais controle, como definir o arquivo, linha, etc.
        #abre caixa de texto na tela
        # warnings.catch_warnings
        #catch_warnings é usado para capturar ou suprimir warnings (normalmente em testes ou contextos específicos).
    
    #genérico que aponta o que há de exceção
    except Exception as e:
        warnings.warn(f"Erro inesperado: {e}")

# Executando o programa
if __name__ == "__main__":
    # Configurando para mostrar todos os warnings
    warnings.filterwarnings('always')#'default', 'ignore', 'error', 'module' ...
    #Garante que todos os warnings sejam sempre mostrados.
    main() 