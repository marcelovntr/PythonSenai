class Poupanca:
    def __init__(self, nome, saldo_inicial=0):
       self.__nome = nome
       self.__saldo = saldo_inicial
       self.__senha = '1234'
    
    def ver_saldo(self):
        return f"Saldo now: R$ {self.__saldo:.2f}"
    
    def deposito(self, valor, senha):
        if senha != self.__senha:
            return "Senha incorreta!"
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R$ {valor} realizado, fera!"
        return "Valor inválido para depósito!"
    
    def saque(self, valor, senha):
        if senha != self.__senha:
            return "Senha incorreta!"
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        #if valor > 0 and valor <= self.__saldo:
            return f"Saque de {valor} efetuado de boas!"
        return "Valor inválido para saque!"

    def mudar_senha(self, senha_atual, nova_senha):
        if senha_atual != self.__senha:
            return "Senha incorreta!"
        if len(nova_senha) >= 4:
            self.__senha = nova_senha
            return "Senha alterada com sucesso!"
        return "A nova senha deve ter pelo menos 4 caracteres"

def main():
    print("=== Introdução ao Encapsulamento ===")
    print("- Só podemos acessar atributos de formas seguras")
    print("- Não podemos alterar atributos diretamente\n")

    print("1. Criando uma conta poupança:")
    conta = Poupanca("João")
    print(conta.ver_saldo())

    print("\n2. Tentando acessar o saldo diretamente:")
    try:
        print(conta.__saldo)  # Isso vai gerar um erro
    except AttributeError as e:
        print(f"Erro: {e}")
        print("Não podemos acessar o saldo diretamente!")
    
    print("\n3. Usando os métodos corretos:")
    print(conta.deposito(100, "1234"))
    print(conta.ver_saldo())

    print("\nTentando depositar com senha errada:")
    print(conta.deposito(50, "0000"))

    print("\nSacando dinheiro:")
    print(conta.saque(30, "1234")) 
    print(conta.ver_saldo())

    print("\n4. Mudando a senha:")
    print(conta.mudar_senha("1234", "4321"))  # Senha correta
    print(conta.deposito(50, "4321"))  # Nova senha
    print(conta.ver_saldo())

if __name__ == "__main__":
    main() 