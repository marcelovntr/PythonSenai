dic_produto = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

print(dic_produto['b'])

dic_produto['c'] = 600

dic_produto['d'] = dic_produto['d'] * 1.5
print(dic_produto)

print(len(dic_produto))

dic_produto.pop('c')

dic_produto['w'] = 400 #se não existe, é criado desta forma, OU SUBSTITUI se já houver
print(dic_produto)

if 'b' in dic_produto:
    print('confere!')
else:
    print('não consta!')

if 100 in dic_produto.values():
    print('o valor existe')
else:
    print('não existe')

novo_produto = input('insira o produto desejado: ')
novo_produto.lower()

novo_preco = input('Insira o valor: ')
novo_preco = float(novo_preco)
if novo_produto in dic_produto:
    dic_produto[novo_produto] = novo_preco #substitui
else:
    dic_produto[novo_produto] = novo_preco #aqui cria novo no ultimo índice (na real DÁ NA MESMA)

produto = 'a'
novo_preco = dic_produto[produto] * 1.1
dic_produto[produto] = novo_preco
print(dic_produto)

for bagulho in dic_produto: #assim imprime só a chave
    print(bagulho)

for produto in dic_produto:
    novo_preco = dic_produto[produto] * 1.1 #multiplicando o valor da chave produto
    dic_produto[produto] = novo_preco
print(dic_produto)
print(dic_produto.values())