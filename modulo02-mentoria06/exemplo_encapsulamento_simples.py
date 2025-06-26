"""
Introdução ao Encapsulamento em Python

Este exemplo usa uma analogia simples: uma conta poupança.
- Encapsulamento é como proteger o dinheiro em um cofre
- Só podemos acessar o dinheiro de formas seguras (depositar, sacar)
- Não podemos mexer no dinheiro diretamente

SUMÁRIO:
--------
1. Conceitos Principais:
   - Encapsulamento: Proteção de dados usando atributos privados (__atributo)
   - Getters: Métodos para acessar dados protegidos (ver_saldo)
   - Setters: Métodos para modificar dados protegidos (depositar, sacar)
   - Validação: Verificações de segurança (senha, valores)

2. Partes Complexas Explicadas:
   a) Atributos Privados:
      - Uso de __ (duplo underscore) torna atributos privados
      - Exemplo: self.__saldo não pode ser acessado diretamente
      - Força o uso de métodos controlados para acesso

   b) Sistema de Senha:
      - Implementa uma camada extra de segurança
      - Validação em todas as operações sensíveis
      - Permite mudança segura de senha

   c) Validações:
      - Verifica senha antes de qualquer operação
      - Valida valores de depósito e saque
      - Previne operações inválidas

3. Boas Práticas Demonstradas:
   - Separação clara entre interface pública e implementação
   - Validações de segurança em todas as operações
   - Mensagens de erro claras e informativas
   - Código organizado e bem documentado
"""

class ContaPoupanca:
    def __init__(self, nome, saldo_inicial=0):
        # Atributos privados (protegidos) - Note o uso de __
        self.__nome = nome # Estes atributos só podem ser acessados através dos métodos da classe
        self.__saldo = saldo_inicial
        self.__senha = "1234"  # Senha padrão - Em um sistema real, seria criptografada
    
    # Getter - Método para acessar o saldo de forma segura
    # Não permite modificação direta, apenas leitura
    def ver_saldo(self):
        return f"Saldo atual: R$ {self.__saldo:.2f}"
    
    # Setter com validação - Método para modificar o saldo de forma segura
    def depositar(self, valor, senha):
        if senha != self.__senha: # Inclui validação de senha e valor
            return "Senha incorreta!"
        
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
        return "Valor inválido para depósito"
    
    # Setter com validação - Método para saque com múltiplas verificações
    # 1. Verifica senha
    # 2. Valida valor do saque
    # 3. Verifica saldo suficiente
    def sacar(self, valor, senha):
        if senha != self.__senha:
            return "Senha incorreta!"
        
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso!"
        return "Valor inválido para saque ou saldo insuficiente"
    
    # Método de segurança - Permite alteração segura da senha
    # Inclui validação da senha atual e requisitos para nova senha
    def mudar_senha(self, senha_atual, nova_senha):
        if senha_atual != self.__senha:
            return "Senha atual incorreta!"
        
        if len(nova_senha) >= 4:
            self.__senha = nova_senha
            return "Senha alterada com sucesso!"
        return "A nova senha deve ter pelo menos 4 caracteres"

def main():
    print("=== Introdução ao Encapsulamento ===")
    print("\nEncapsulamento é como proteger o dinheiro em um cofre:")
    print("- O dinheiro (saldo) está protegido dentro do cofre")
    print("- Só podemos acessar o dinheiro de formas seguras")
    print("- Não podemos mexer no dinheiro diretamente\n")
    
    # Criando uma conta
    print("1. Criando uma conta poupança:")
    conta = ContaPoupanca("João")
    print(conta.ver_saldo())
    
    # Tentando acessar o saldo diretamente (não vai funcionar)
    print("\n2. Tentando acessar o saldo diretamente:")
    try:
        print(conta.__saldo)  # Isso vai gerar um erro
    except AttributeError as e:
        print(f"Erro: {e}")
        print("Não podemos acessar o saldo diretamente!")
    
    # Usando os métodos corretos
    print("\n3. Usando os métodos corretos:")
    print(conta.depositar(100, "1234"))  # Senha correta
    print(conta.ver_saldo())
    
    print("\nTentando depositar com senha errada:")
    print(conta.depositar(50, "0000"))  # Senha errada
    
    print("\nSacando dinheiro:")
    print(conta.sacar(30, "1234"))  # Senha correta
    print(conta.ver_saldo())
    
    print("\n4. Mudando a senha:")
    print(conta.mudar_senha("1234", "4321"))  # Senha correta
    print(conta.depositar(50, "4321"))  # Nova senha
    print(conta.ver_saldo())

if __name__ == "__main__":
    main() 