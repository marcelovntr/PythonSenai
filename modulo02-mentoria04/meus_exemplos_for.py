import time

def meu_exemplo_range():
    print("For tradicional na versão Python:")
    inicio = int(input("\nInsert the first number: "))
    fim = int (input("Insert the final number: "))
    print(f"\n Contando de {inicio} a {fim}")
    for carambola in range(inicio, fim + 1):
        print(f"\nNúmero atual: {carambola}")

def minha_comparacao():
    print('Insira um brasileiro no mundial de clubes: ')
    chute = input('Ponha sua resposta: ').strip().lower()
    lista_previa = ['Flamengo', 'Fluminense', 'Palmeiras', 'Botafogo']
    
    time.sleep(1.5)
    controle = False
    for indice in lista_previa:
        if indice.lower() == chute:
            print(f"\n {indice.capitalize()} encontrado")
            controle = True
            break
    if controle == False:
        print(f"\n{chute} não foi encontrado")

def contagem_dois_valores():
    print('Contagem do menor para o maior: ')
    primeiro = int(input("Insira o primeiro: "))
    segundo = int(input("Agora insira o segundo: "))

    alfa = primeiro
    beta = segundo
    if segundo < primeiro:
        beta = primeiro
        alfa = segundo

    '''if valor_a > valor_b:
          valor_a, valor_b = valor_b, valor_a
    '''
    print(f"\n Imprimindo do {alfa} para o {beta}")
    for oxala in range(alfa, beta + 1):
        print(oxala)

    


