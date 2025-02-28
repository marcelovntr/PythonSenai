lista_precos = [1500, 1000, 800, 3000]
#calculando imposto

print('Imposto total calculado para o ')

def calcula_imposto(preco):
    if preco <= 200:
        ir = 0.2 * preco
    else:
        ir = 0.3 * preco
    iss = 0.15 * preco
    csll = 0.05 * preco
    imposto_full = ir + iss + csll
    return imposto_full

for preco in lista_precos:
    imposto_full = calcula_imposto(preco)
    print(f'produto de preço R${preco}: R${imposto_full}')
