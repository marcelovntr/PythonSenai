#AULA 3***********************************
#INPUTS E LISTAS
# email = input('qual seu email? ' 'Insira: ')
# nome = input('insira seu nome: ')
# #sempre recebe como string......precisa ser parseado

# print(f"{nome}, você é um feião! e sei email: {email} uma vergonha")

#LISTAS*************************
lista_X = [10, 5, 8, 99, 75]
total_lista = sum(lista_X)
print(total_lista)
quantidade_lista = len(lista_X)
print(quantidade_lista)
print(max(lista_X))
print(min(lista_X))
print(lista_X[-1])

produtos = ['rola', 'jamanta', 'maçã', 'playstation', 'jamanta']
# produto_buscado = input("insira o produto desejado: ")
# produto_buscado = produto_buscado.lower()

# print(produto_buscado  in produtos)#retorna booleano

produtos.append('mama')
produtos.remove('rola')
produtos.pop(2)
print(produtos)

preco = [33, 44, 5, 4000]
preco[3] = 99
preco[0] = preco * 2

print(produtos.count('jamanta'))
produtos.sort()
print(produtos)
produtos.sort(reverse=True)
print(produtos)