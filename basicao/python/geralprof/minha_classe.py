class Pessoa:
    nome = ""
    idade = ""

    def __init__(self, nome, idade) -> None: #anotação que diz que a função na retorna algo
        self.nome = nome
        self.idade = idade

    def andar(self):
        print(f"{self.nome} está andando.")
        # ...

    def correr(self):
        
        print(f"{self.nome} está correndo..")
        # ...
        

#objetos/instâncias
pessoa1 = Pessoa("Dennis", 26)
pessoa2 = Pessoa("Fabio", 16)
"""Essas linhas já estão sendo executadas imediatamente, sem a verificação if __name__ == "__main__" 
— o que funciona, mas não é a melhor prática se o arquivo for importado por outro código."""

pessoa1.andar()
pessoa2.correr()
print(Pessoa)

"""se iniciasse a classe assim:
if __name__ == "__main__":
    p = Pessoa("Ana", 30)
    print(p.nome)
ela não seria acessada em outro arquivo que a importasse como módulo"""