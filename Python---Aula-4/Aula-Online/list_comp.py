# List Comprehension
# x é a variavel que representa cada valor na lista
# for para cada x em um range de 0 a 9
# para cada item x vamos fazer um if, onde x/2 e o resto deve ser 0
numeros_pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares: {numeros_pares}")


# Dictionary Comprehension
# 1: 1*1 -> 1: 1
# 2: 4
# 3: 9
quadrados = {x: x*x for x in range(10)}
print(f"Quadrados: {quadrados}")

# Generator Expression 
# Gera valores grandes quando consultado
# Não ocupa espaço na memória
numeros_grandes = (x*2 for x in range(1000000))
# Você pode iterar sobre ele, mas ele não consome toda a memória
print(f"Ultimos 5 números do gerador: {list(numeros_grandes)[0:100]}")