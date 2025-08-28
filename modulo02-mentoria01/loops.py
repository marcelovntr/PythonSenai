contador = 0
print("\n-----------------------")
print("while: ")
while contador < 10:
    print(contador)
    contador += 1
#---------------------------------------
print("for in RANGE: ")
for contador in range(1,): #range(1,30)
    print(contador)
#---------------------------------------
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0
print("for in LISTA: ")
for numeral in listaNumeros:
    print(f"número: {numeral} e índice: {indice}")
    indice += 1
#---------------------------------------
print("for in STRING: ")
for letra in "python":
    print(letra)

print("FOR tradicional não existe")

print("\n ======== estruturas de decisão: ==========")


maiorIdade = 18
idade = 16
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print("\n ======== try e except: ==========")

try:
    1 / 0
except ZeroDivisionError:
    print("Divisão por zero")