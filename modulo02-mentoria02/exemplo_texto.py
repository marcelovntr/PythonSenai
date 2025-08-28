"""
Exemplo simples de operações com textos

Este código demonstra operações básicas com strings (textos) em Python:
1. Usa input() para receber texto do usuário
2. Demonstra métodos de string:
   - upper(): converte para maiúsculas
   - lower(): converte para minúsculas
   - len(): conta quantidade de caracteres
3. Mostra como acessar caracteres:
   - texto[0]: primeiro caractere
   - texto[-1]: último caractere
4. Trata erros inesperados com try/except

Como usar:
1. Execute o programa
2. Digite qualquer texto quando solicitado
3. O programa mostrará:
   - O texto original
   - O texto em maiúsculas
   - O texto em minúsculas
   - Quantidade de caracteres
   - Primeira e última letra
"""

def main():
    try:
        # Pedindo um texto ao usuário
        texto = input("Digite um texto: ")
        
        # Realizando operações com o texto
        print(f"\nOperações com o texto:")
        print(f"Texto original: {texto}")
        print(f"Texto em maiúsculas: {texto.upper()}")
        print(f"Texto em minúsculas: {texto.lower()}")
        print(f"Quantidade de caracteres: {len(texto)}")
        print(f"Primeira letra: {texto[0]}")
        print(f"Última letra: {texto[-1]}")
        print(f"Tentando replaces: {texto.replace(' ','*')}")
        print(f"Tentando split: {texto.split(' ')}")
        print(f"Tentando strip: {texto.strip()}")
        print(f"Tentando capitalize: {texto.capitalize()}")
        print(f"Tentando title: {texto.title()}")
    
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main() 