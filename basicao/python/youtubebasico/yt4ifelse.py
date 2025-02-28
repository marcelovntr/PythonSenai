vendas = 1500
meta = 1400
metaPica = 1600


if vendas >= metaPica:
    print('show')
    bonus = 0.13 * vendas
    print('bônus:', bonus)
else:
    if vendas >= meta:
        bonus = 0.1 * vendas
    else:
        bonus = 0
        print('sem mamata pra ti, querido')

print('ISSO AQUI TÁ FORA DO IF!!!')
print('bonus:', bonus)

#OU: *******************************
if vendas >= metaPica:
    print('show')
    bonus = 0.13 * vendas
    print('bônus:', bonus)
elif vendas >= meta:
    bonus = 0.1 * vendas
else: bonus = 0
print('segundo exemplo')


lista = ['rola', 'badalo', 'jiromba', 'piroquinha']
produto_buscado = input('Insira o nome do produto: ')
produto_buscado.lower()

if produto_buscado in lista:
    print(f'{produto_buscado} adicionado ao carrinho')
else:
    print(f'{produto_buscado} não encontrado')
