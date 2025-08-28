"""
Exemplo simples de operações com booleanos

Este código demonstra operações básicas com valores booleanos em Python:
1. Usa input() para receber uma resposta sim/não
2. Converte a resposta em valor booleano (True/False)
3. Demonstra operações lógicas:
   - not: inverte o valor (True -> False, False -> True)
   - and: retorna True se ambos valores forem True
   - or: retorna True se pelo menos um valor for True
4. Trata entrada inválida e outros erros

Como usar:
1. Execute o programa
2. Digite 'sim' ou 'não' quando solicitado
3. O programa mostrará:
   - O valor booleano original
   - O valor negado (not)
   - O resultado de AND com True
   - O resultado de OR com False
4. Se digitar algo diferente de 'sim' ou 'não', verá uma mensagem de erro
"""

def main():#apenas uma convenção
    respondeu = False
    while(respondeu is False):
        try:
            # Pedindo uma resposta sim/não ao usuário
            resposta = input("Digite 'sim' ou 'não': ").lower()
            
            # Convertendo para booleano
            if resposta == 'sim':
                valor = True
                respondeu = True
            elif resposta == 'não' or resposta == 'nao':
                valor = False
                respondeu = True
            else:
                print("Erro: Digite 'sim' ou 'não'!")
                # return
            
            # Mostrando operações com booleanos
            print(f"\nOperações com o valor booleano:")
            print(f"Valor original: {valor}")
            print(f"Valor negado: {not valor}")
            print(f"Valor AND com True: {valor and True}")
            print(f"Valor OR com False: {valor or False}")
        
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main() 