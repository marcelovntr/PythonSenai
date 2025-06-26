"""
Introdução à Herança em Python

Este exemplo demonstra o conceito de herança usando uma analogia com veículos.
A herança é um dos pilares da Programação Orientada a Objetos (POO) que permite
que uma classe herde características e comportamentos de outra classe.

SUMÁRIO:
1. Estrutura do Código
   - Classe Base (Veiculo): Define características e comportamentos comuns
   - Classes Derivadas (Carro, Moto): Herdam da classe base e adicionam funcionalidades específicas

2. Conceitos Demonstrados
   - Herança Simples: Uma classe herda de uma única classe base
   - Método super(): Permite acessar métodos da classe pai
   - Sobrescrita de Métodos: Classes filhas podem redefinir métodos da classe pai
   - Polimorfismo: Diferentes classes podem responder ao mesmo método de formas distintas

3. Partes Complexas Explicadas
   a) Uso do super():
      - super().__init__(marca, modelo, ano) chama o construtor da classe pai
      - Isso evita duplicação de código e garante inicialização correta
   
   b) Sobrescrita de Métodos:
      - Classes filhas redefinem mostrar_info() para incluir informações específicas
      - Usam super().mostrar_info() para reutilizar o código da classe pai
   
   c) Polimorfismo:
      - A lista veiculos contém objetos de diferentes classes (Carro e Moto)
      - Todos respondem aos mesmos métodos (acelerar, frear) de forma polimórfica

4. Benefícios Demonstrados
   - Reutilização de código através da herança
   - Extensibilidade: Fácil adicionar novos tipos de veículos
   - Manutenibilidade: Código organizado e modular
"""

class Veiculo:
    """
    Classe base que define características e comportamentos comuns a todos os veículos.
    Serve como template para classes mais específicas como Carro e Moto.
    """
    def __init__(self, marca, modelo, ano):
        # Características que todos os veículos têm
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 10
        return f"{self.marca} {self.modelo} acelerou para {self.velocidade} km/h"
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
        return f"{self.marca} {self.modelo} freou para {self.velocidade} km/h"
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Carro(Veiculo):
    """
    Classe derivada que herda de Veiculo e adiciona funcionalidades específicas de carros.
    Demonstra como estender uma classe base com novas características (num_portas)
    e comportamentos (abrir_porta).
    """
    def __init__(self, marca, modelo, ano, num_portas):
        # Chama o construtor da classe pai (Veiculo)
        super().__init__(marca, modelo, ano)
        # Adiciona uma característica especial do carro
        self.num_portas = num_portas
    
    # Método especial do carro
    def abrir_porta(self, numero_porta):
        if 1 <= numero_porta <= self.num_portas:
          #(1 <= numero_porta) and (numero_porta <= self.num_portas)
            return f"Porta {numero_porta} do {self.marca} {self.modelo} aberta"
        return f"O {self.marca} {self.modelo} não tem porta {numero_porta}"
    
    # Sobrescreve o método mostrar_info
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - {self.num_portas} portas"

class Moto(Veiculo):
    """
    Classe derivada que herda de Veiculo e adiciona funcionalidades específicas de motos.
    Demonstra como uma classe derivada pode ter comportamentos únicos (empinar)
    e características próprias (cilindradas).
    """
    def __init__(self, marca, modelo, ano, cilindradas):
        # Chama o construtor da classe pai (Veiculo)
        super().__init__(marca, modelo, ano)
        # Adiciona uma característica especial da moto
        self.cilindradas = cilindradas
    
    # Método especial da moto
    def empinar(self):
        return f"{self.marca} {self.modelo} está empinando!"
    
    # Sobrescreve o método mostrar_info
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - {self.cilindradas}cc"

def main():
    """
    Função principal que demonstra os conceitos de herança na prática.
    Mostra:
    1. Criação de objetos das classes derivadas
    2. Uso de métodos herdados e específicos
    3. Polimorfismo com uma lista de veículos
    4. Verificação de tipos usando isinstance()
    """
    print("=== Introdução à Herança ===")
    print("\nHerança é quando uma classe herda características de outra classe.")
    print("É como dizer que um carro é um tipo de veículo, então ele tem todas")
    print("as características de um veículo, mas também tem características próprias.\n")
    
    # Criando um carro e uma moto
    print("1. Criando um carro:")
    carro = Carro("Fiat", "Uno", 2020, 4)
    print(carro.mostrar_info())
    print(carro.acelerar())
    print(carro.abrir_porta(2))
    
    print("\n2. Criando uma moto:")
    moto = Moto("Honda", "CG", 2021, 160)
    print(moto.mostrar_info())
    print(moto.acelerar())
    print(moto.empinar())
    
    print("\n3. O que todos os veículos podem fazer:")
    veiculos = [carro, moto]
    for veiculo in veiculos:
        print(f"\n{veiculo.marca} {veiculo.modelo}:")
        print(veiculo.acelerar())
        print(veiculo.frear())
    
    print("\n4. Verificando a herança:")
    print(f"Carro é um Veículo? {isinstance(carro, Veiculo)}")
    print(f"Moto é um Veículo? {isinstance(moto, Veiculo)}")

if __name__ == "__main__":
    main() 