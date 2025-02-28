lista = [1000, 600, 500, 2000, 1400]

meta = 1200
percentual_bonus = 0.1


for i in range(3):
    print("qdo se sabe a qtdade de repetições")

for venda in lista:
    if venda > meta:
        bonus = venda * percentual_bonus 
    else:
        bonus=0
    print(bonus)

