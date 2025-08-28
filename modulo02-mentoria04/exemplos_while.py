"""
Exemplos de Loops WHILE em Python

Este módulo contém exemplos práticos de diferentes utilizações do loop WHILE em Python,
demonstrando desde casos básicos até usos mais avançados com controle de fluxo.

Exemplos implementados:

1. exemplo_contador():
   - Demonstra o uso básico do WHILE com um contador
   - Implementa uma contagem progressiva até um número definido pelo usuário
   - Mostra como incrementar uma variável dentro do loop
   - Exemplo fundamental de loop controlado por contador

2. exemplo_senha():
   - Ilustra o uso do WHILE para verificação de senha
   - Implementa um sistema de tentativas limitadas (3 tentativas)
   - Demonstra controle de acesso com feedback ao usuário
   - Mostra como usar o break para sair do loop quando a senha é correta
   - Inclui contagem de tentativas restantes

3. exemplo_break():
   - Demonstra o uso do break para interromper um loop
   - Implementa um somador de números com condição de parada
   - Mostra como usar while True com break para controle de fluxo
   - Ilustra o uso de acumulador (soma) dentro do loop
   - Permite ao usuário controlar quando parar o programa

4. exemplo_continue():
   - Ilustra o uso do continue para pular iterações
   - Implementa um somador que aceita apenas números pares
   - Demonstra como filtrar valores durante a iteração
   - Mostra a combinação de break e continue no mesmo loop
   - Inclui feedback sobre números ignorados (ímpares)
"""

def exemplo_contador():
    """Exemplo de while com contador"""
    print("\n=== Exemplo 1: While com contador ===")
    numero = int(input("Digite um número para contar até ele: "))
    contador = 1

    print("Contando de 1 até", numero)
    while contador <= numero:
        print(f"Contador: {contador}")
        contador += 1  # Incrementa o contador em 1

def exemplo_senha():
    """Exemplo de while verificando senha"""
    print("\n=== Exemplo 2: While verificando senha ===")
    senha_correta = "1234"
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        senha = input("Digite a senha (4 dígitos): ")
        if senha == senha_correta:
            print("Senha correta! Acesso permitido.")
            break
        else:
            tentativas += 1
            tentativas_restantes = max_tentativas - tentativas
            print(f"Senha incorreta! Você ainda tem {tentativas_restantes} tentativa(s).")

    if tentativas == max_tentativas:
        print("Número máximo de tentativas excedido!")

def exemplo_break():
    """Exemplo de uso do break"""
    print("\n=== Exemplo 3: Uso do break ===")
    print("Digite números. Para parar, digite 0.")
    soma = 0

    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            print("Você digitou 0. Parando o programa...")
            break
        soma += numero
        print(f"Soma atual: {soma}")

    print(f"Soma final: {soma}")

def exemplo_continue():
    """Exemplo de uso do continue"""
    print("\n=== Exemplo 4: Uso do continue ===")
    print("Vamos somar apenas números pares!")
    print("Digite números. Para parar, digite 0.")
    soma_pares = 0

    while True:
        numero = int(input("Digite um número: "))
        
        if numero == 0:
            print("Você digitou 0. Parando o programa...")
            break
        
        if numero % 2 != 0:  # Se o número for ímpar
            print(f"{numero} é ímpar, pulando...")
            continue  # Pula para a próxima iteração
        
        soma_pares += numero
        print(f"Soma dos números pares: {soma_pares}")

# Se este arquivo for executado diretamente, mostra uma mensagem
if __name__ == "__main__":
    print("Demonstração de diferentes usos do WHILE em Python")
    print("=" * 50)

    exemplo_contador()
    exemplo_senha()
    exemplo_break()
    exemplo_continue()
