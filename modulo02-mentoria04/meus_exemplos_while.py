def meu_contador():
    print("WHILE básico: ")
    numero = int(input(f"Escolha o número final da contagem: "))
    contador = 1

    while contador <= numero:
        print(f"Contador: {contador}")
        contador += 1

def minha_senha():
    print('While para 3 tentativas de senha: ')
    
    correta = '1234'
    tentativas = 0
    max_tentivas = 3


    while tentativas < max_tentivas:
        digitada = input('Insira a senha: ')
        if tentativas < 3:
            if digitada == correta:
                print('Acertou, miseravi!')
                break
            else:
                tentativas +=1
                tent_rest = max_tentivas - tentativas
                print(f"tentativas restantes: {tent_rest}")

    if tentativas == max_tentivas:
        print('Out of attempts left')

def meu_break():
    print('Exempleo WHILE com BREAK: ')
    
    soma = 0

    while True:
        numero = int(input("Digite números. Para parar, digite 0: "))
        if numero != 0:
            print(f"número: {numero}")
            soma += numero
            print(f"soma: {soma}")
        else:
            print('Digitou 0, saindo...')
            break
    print(f"soma final: {soma}")     
    '''if numero == 0:
            print("Você digitou 0. Parando o programa...")
            break
        soma += numero
        print(f"Soma atual: {soma}")

    print(f"Soma final: {soma}") ''' 

def meu_continue():
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