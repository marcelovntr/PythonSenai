"""
Exemplo Simples de Abstração em Python

Este exemplo demonstra o conceito de abstração usando uma analogia do mundo real: controles remotos.
A abstração é implementada através de uma classe abstrata que define um "contrato" que todas as classes concretas devem seguir.

Estrutura do Código:
-------------------
1. Classe Abstrata (Contrato):
   - ControleRemoto(ABC): Define a interface que todos os controles devem implementar
   - Usa @abstractmethod para forçar implementação dos métodos nas classes filhas
   - Não pode ser instanciada diretamente, servindo como template

2. Classes Concretas:
   - ControleTV: Implementa o contrato para controle de TV
     * Mantém estado: ligada (bool) e volume (int)
     * Validação de volume entre 0 e 100
   - ControleAr: Implementa o contrato para controle de Ar Condicionado
     * Mantém estado: ligado (bool) e temperatura (int)
     * Validação de temperatura entre 16°C e 30°C

Pontos de Complexidade:
----------------------
1. ABC (Abstract Base Class):
   - Classe especial do Python para criar classes abstratas
   - Fornece mecanismo para definir interfaces

2. @abstractmethod:
   - Decorador que força implementação nas classes filhas
   - Garante que todas as classes concretas implementem o contrato

3. Polimorfismo:
   - Mesmo código funciona para diferentes tipos de controle
   - Cada controle mantém seu comportamento específico
   - Demonstrado no loop de controles na função main()

4. Tratamento de Erros:
   - Proteção contra instanciação direta da classe abstrata
   - Validações específicas em cada implementação

Benefícios Demonstrados:
-----------------------
1. Encapsulamento: Cada controle esconde sua implementação interna
2. Reutilização: Mesmo contrato para diferentes tipos de controles
3. Manutenibilidade: Fácil adição de novos tipos de controles
4. Consistência: Padrão de interface uniforme
5. Segurança: Garantia de implementação completa do contrato

Aplicações Práticas:
-------------------
- Sistemas de controle de dispositivos IoT
- Interfaces de usuário com diferentes implementações
- Plugins e extensões de software
- Sistemas de autenticação
- Processadores de pagamento

Este exemplo ilustra o princípio "programe para uma interface, não para uma implementação",
demonstrando como a abstração ajuda a criar código mais organizado, reutilizável e manutenível.
"""

from abc import ABC, abstractmethod

# Classe abstrata (contrato) que define o que um controle remoto deve fazer
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        """Todo controle deve saber ligar o aparelho"""
        pass
    
    @abstractmethod
    def desligar(self):
        """Todo controle deve saber desligar o aparelho"""
        pass
    
    @abstractmethod
    def ajustar(self, valor):
        """Todo controle deve saber ajustar algo (volume, temperatura, etc)"""
        pass

# Classe concreta que implementa o contrato para TV
class ControleTV(ControleRemoto):
    def __init__(self):
        self.ligada = False
        self.volume = 0
    
    def ligar(self):
        self.ligada = True
        return "TV ligada!"
    
    def desligar(self):
        self.ligada = False
        return "TV desligada!"
    
    def ajustar(self, valor):
        if not self.ligada:
            return "TV está desligada!"
        self.volume = max(0, min(100, valor))
        return f"Volume ajustado para {self.volume}"

# Classe concreta que implementa o mesmo contrato para Ar Condicionado
class ControleAr(ControleRemoto):
    def __init__(self):
        self.ligado = False
        self.temperatura = 25
    
    def ligar(self):
        self.ligado = True
        return "Ar condicionado ligado!"
    
    def desligar(self):
        self.ligado = False
        return "Ar condicionado desligado!"
    
    def ajustar(self, valor):
        if not self.ligado:
            return "Ar condicionado está desligado!"
        self.temperatura = max(16, min(30, valor))
        return f"Temperatura ajustada para {self.temperatura}°C"

def main():
    print("=== Exemplo Simples de Abstração ===")
    print("\nAbstração é como um contrato que define o que algo deve fazer.")
    print("É como dizer que todos os controles remotos devem saber:")
    print("- Ligar o aparelho")
    print("- Desligar o aparelho")
    print("- Ajustar algo (volume, temperatura, etc)")
    print("\nComo cada controle faz isso, não importa. O importante é que ele faça!\n")
    
    # Criando um controle de TV
    print("1. Usando o controle da TV:")
    tv = ControleTV()
    print(tv.ligar())
    print(tv.ajustar(50))
    print(tv.desligar())
    
    # Criando um controle de Ar Condicionado
    print("\n2. Usando o controle do Ar Condicionado:")
    ar = ControleAr()
    print(ar.ligar())
    print(ar.ajustar(22))
    print(ar.desligar())
    
    # Mostrando que todos os controles seguem o mesmo contrato
    print("\n3. Todos os controles seguem o mesmo contrato:")
    controles = [tv, ar]
    for controle in controles:
        print(f"\n{controle.__class__.__name__}:")
        print(controle.ligar())
        print(controle.ajustar(30))
        print(controle.desligar())
    
    # Tentando criar um controle sem implementar o contrato
    print("\n4. Tentando criar um controle sem implementar o contrato:")
    try:
        controle = ControleRemoto()  # Isso vai gerar um erro
    except TypeError as e:
        print(f"Erro: {e}")
        print("Não podemos criar um controle sem implementar o contrato!")

if __name__ == "__main__":
    main() 