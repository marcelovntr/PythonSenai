# Exemplo de comentário de uma linha
"""Exemplo de
Comentário de
muitas linhas"""

# Atribuição de váriavel primitiva
nome = "João"
cargo = 'Programador'
idade = 30
peso = 75.5
esta_ligado = True
VARIAVEL_CONSTANTE = "Exemplo de variavel constante"

# Atribuição de váriavel composta
# Dict {chave : valor}
endereco = {
    "rua": "Rua das Flores",
    "numero": 123,
    "cidade": "São Paulo",
    "estado": "SP",
    "possui_morador": True
}

endereco["complemento"] = "Apto 101"

compras = ['maçã', 'banana', 'pão', 'leite']  #Lista mutável
exemplo_tupla = ('maçã', 'banana', 'pão', 'leite')  #Tupla imutável

compras.append("macarrão") # add item
compras.append("arroz") # add item
compras.pop() # remove item

conjunto_a = {1, 2, 3, 4, 5}  #Set
conjunto_b = {3, 4, 5, 6, 7}  #Set

# Saída de dados
print(compras)
print(endereco)

print(endereco["rua"])

print(nome)


# Entrada de dados
nome = input("Digite seu nome: ")
print(nome)

# Operadores aritméticos
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
divisao_inteira = 10 // 5
modulo = 10 % 5
exponenciacao = 10**5

# Operadores relacionais
maior_que = 10 > 5
menor_que = 10 < 5
maior_ou_igual = 10 >= 5
menor_ou_igual = 10 <= 5
igual = 10 == 5
diferente = 10 != 5

# Operadores lógicos
and_operador = True and False
or_operador = True or False
not_operador = not True

# Operadores de atribuição
x = 5
x += 3  # x = x + 3
x -= 3  # x = x - 3
x *= 3  # x = x * 3
x /= 3  # x = x / 3
x %= 3  # x = x % 3
x //= 3  # x = x // 3
x **= 3  # x = x ** 3

# Operadores de pertencimento
in_operador = 'banana' in compras
not_in_operador = 'banana' not in compras

# Condicionais simples
if idade >= 0:
    print("Idade válida")

# Condicionais compostas
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Condicionais aninhadas
if idade >= 0:
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")
else:
    print("Idade inválida")

# Condicionais encadeadas
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Você é adolecente")
else:
    print("Você é criança")

# Condicionais encadeadas com operadores lógicos
if (idade >= 18) and (peso >= 60):
    print("Maior de idade e peso ideal")
elif idade >= 18 and peso < 60:
    print("Maior de idade e peso abaixo do ideal")
elif idade < 18 and peso >= 60:
    print("Menor de idade e peso ideal")
else:
    print("Menor de idade e peso abaixo do ideal")

# Repetição com for
for item in compras:
    print(item)

# Repetição com while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#############################


# Função sem parâmetros
def saudacao():
    print("Olá, mundo!")


# Função com parâmetros
def soma(a, b):
    print(a + b)


# Função com retorno e parâmetros
def multiplicacao(a, b):
    return a * b


# Função com retorno e sem parâmetros
def divisao():
    numero = int(input("Digite um número: "))
    return numero / 2


# Função recursiva
def fibonacci(n1, n2=0):
    resultado = n1 + n2
    print(resultado)
    if resultado > 300:
        return resultado
    else:
        fibonacci(n2, resultado)


# Chamando as funções
saudacao()

soma(10, 5)

resultado = multiplicacao(10, 5)

print(resultado)

resultado = divisao()

print(resultado)

fibonacci(1)

#############################
""" Esse bloco gera um erro, tire o comentário e teste, após insira o comentário
novamente
# Isso gera um erro de semantica
texto = "Python é legal!"
resultado = texto/2 #TypeError: unsupported operand type(s) for /: 'str' and 'int'

# Erro de sintaxe
if len(texto) > 10   # Falta o ':' no final da linha
    print("Texto grande!")

# Isso está correto
if len(texto) > 10:
    print("Texto grande!")
"""

# Conversão de tipos

# Conversão de inteiro para texto
numero = 10
texto = str(numero)

# Conversão de texto para inteiro
texto = "10"
numero = int(texto)

# Conversão de inteiro para booleano
numero = 10
booleano = bool(numero)

# Conversão de booleano para inteiro
booleano = True
numero = int(booleano)

# Conversão de texto para booleano
texto = "True"
booleano = bool(texto)

# Conversão de booleano para texto
booleano = True
texto = str(booleano)

# Conversão de texto para float
texto = "10.5"
numero = float(texto)

# Conversão de float para inteiro
numero = 10.5
inteiro = int(numero)

# Conversão de inteiro para float
numero = 10
float = float(numero)

# Conversão de float para texto
numero = 10.5
texto = str(numero)
"""
IMPORTANTE SABER COMO FUNCIONA O CONVERSOR DE TIPOS!
Podemos converter de inteiro para texto, texto para inteiro, 
inteiro para booleano, booleano para inteiro, etc.

É importante compreender que ao realizar uma conversão de tipo,
precisa analizar o dado que está sendo convertido, perceba que
ao converter um texto para inteiro, o texto precisa ser um número. 
Caso contrário, ocorrerá um erro de execução!
O mesmo vale de um texto para float!

Em casos onde precisa observar se um texto é um numero é possivel
usar uma função que verifica isso, por exemplo:
"Esse texto não é um numero, mesmo se tiver um numero 10 no meio do texto".isnumeric() -> False

"100".isnumeric() -> True

Dessa forma conseguimos verificar se um texto é um numero ou não. 

Vale ressaltar que ao converter um numero para texto, 
não ocorrerá um erro como str -> int, pois o numero 
pode ser convertido facilmente para um tipo de texto.
"""

numero_par = 26
if numero_par % 2 == 0:
    print("Esse numero é par")

# Erro e tratamento de erros
idade = input("Informe sua idade para calcular o ano do seu nascimento: ")

try:
    ano_nascimento = 2024 - idade

except:
    print("Aconteceu um erro")

else:
    print("O ano do seu nascimento é:", ano_nascimento)

finally:
    print("Saindo app!")


# Funções com mais um retorno
def multiplicação(n1, n2):
    resultado = n1 * n2
    return resultado, n1, n2


# Classes e Objetos
class Pessoa:
    nome = ""
    idade = ""

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def andar():
        ...

    def correr():
        ...


pessoa1 = Pessoa("Dennis", 26)
pessoa2 = Pessoa("Fabio", 16)
