print("meu pau de oculos")
print(33 + 4)
faturamento = 343
lucro = 211
custo = 90
margem_lucro = 32

numero = 99 #"int"
quebrado = 5.6 #"float"
texto = "qualquer" # "str"
logico = True #ou False


print(numero + 2)

print('o lucro foi de', 999)
lucro = 666
print("lucramos", round(lucro, 2))#segundo argumento é o número de casas

#------------STRINGS

email = 'meupau@deoculos.com'
nome= "feião mazanza"
cpf = "99955533388"
print('dados pessoais: email - {}, nome - {}, cpf - {}'.format(email, nome, cpf)) #um jeito!
#ou:
print(f'dados pessoais: email - {email}, nome - {nome}, cpf - {cpf}') #mais legal!!!

email_user = 'bengalamajor@itau.com.us'.upper()
print(email_user)
email_user = 'bengalamajor@itau.com.us'.lower()
print(email_user)

arrouba = email_user.find('@')
print(arrouba) #se nao achar apresenta -1
print(len(email_user))
print(email_user[17]) #se colocar índice inexistente: "OUT OF RANGE" no error
print(email_user[-1]) #começa a contar de trás p´ra frente
print(email_user[:8])#até o índice apontado, não o inclui
print(email_user[0:9])#do 1º até o 8º, exclui o nono
print(email_user[0:])#até o final

novo_email = email_user.replace('itau.com.us', 'gmail.com')
print(novo_email)
print(nome.capitalize())
print(nome.title()) #todas iniciais tornam-se maiúsculas

posicao_arroba = email_user.find('@') + 1
print(email_user[posicao_arroba:])
servidor = email_user[posicao_arroba:]
print(servidor)

posicao_espaco = nome.find(" ")
print(nome[:posicao_espaco])
print(nome[posicao_espaco:]) #+1 para escluir o esáço em branco


#casos especiais
print(f'dados pessoais: faturamente - {faturamento: .2f}, custo - {custo:.2f}, lucro - {lucro:.2f}, margem - {margem_lucro:.0%}') #mais legal!!!
