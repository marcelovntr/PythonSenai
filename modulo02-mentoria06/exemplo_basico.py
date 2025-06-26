"""
Introdução Básica à Programação Orientada a Objetos

Este exemplo usa uma analogia simples: uma receita de bolo.
- Uma classe é como uma receita de bolo
- Um objeto é como um bolo que você faz seguindo a receita
- Atributos são as características do bolo (sabor, tamanho, etc.)
- Métodos são as ações que o bolo pode fazer (esquentar, esfriar, etc.)
"""

"""
SUMÁRIO DO CÓDIGO
-----------------
1. Classe Bolo
   - Atributos:
     * sabor: define o sabor do bolo (ex: chocolate, morango)
     * tamanho: define o tamanho do bolo (ex: pequeno, médio, grande)
     * temperatura: estado atual do bolo (frio/quente)
   - Métodos:
     * __init__: construtor que inicializa um novo bolo
     * esquentar: muda a temperatura do bolo para quente
     * esfriar: muda a temperatura do bolo para frio
     * servir: retorna uma mensagem de serviço do bolo

2. Função main()
   - Demonstração prática dos conceitos de POO:
     * Criação de objetos (instâncias da classe Bolo)
     * Manipulação de atributos
     * Chamada de métodos
     * Independência entre objetos

3. Conceitos de POO Demonstrados:
   - Encapsulamento: atributos e métodos agrupados na classe
   - Instanciação: criação de objetos a partir da classe
   - Estado do objeto: cada bolo mantém seu próprio estado
   - Métodos: ações que podem ser realizadas com o objeto

4. Fluxo do Programa:
   - Inicialização de dois bolos diferentes
   - Demonstração de métodos em cada bolo
   - Exibição do estado independente de cada bolo
"""

class Bolo:
    def __init__(self, sabor, tamanho):
        # Atributos são as características do bolo
        self.sabor = sabor      # Exemplo: "chocolate", "morango"
        self.tamanho = tamanho  # Exemplo: "pequeno", "médio", "grande"
        self.temperatura = "frio"  # Começa frio
    
    # Métodos são as ações que o bolo pode fazer
    def esquentar(self):
        self.temperatura = "quente"
        return f"O bolo de {self.sabor} está {self.temperatura}"
    
    def esfriar(self):
        self.temperatura = "frio"
        return f"O bolo de {self.sabor} está {self.temperatura}"
    
    def servir(self):
        return f"Servindo um bolo de {self.sabor} {self.tamanho}"

def main():
    print("=== Introdução à Programação Orientada a Objetos ===")
    print("\nPense em uma classe como uma receita de bolo:")
    print("- A receita (classe) diz como fazer o bolo")
    print("- O bolo (objeto) é o que você faz seguindo a receita")
    print("- As características (atributos) são coisas como sabor e tamanho")
    print("- As ações (métodos) são coisas que o bolo pode fazer\n")
    
    # Criando dois bolos diferentes (objetos)
    print("1. Criando dois bolos diferentes:")
    bolo_chocolate = Bolo("chocolate", "médio")
    bolo_morango = Bolo("morango", "pequeno")
    
    print(f"\nBolo 1: {bolo_chocolate.sabor} {bolo_chocolate.tamanho}")
    print(f"Bolo 2: {bolo_morango.sabor} {bolo_morango.tamanho}")
    
    # Usando os métodos dos bolos
    print("\n2. O que podemos fazer com os bolos?")
    print(bolo_chocolate.esquentar())
    print(bolo_morango.servir())
    print(bolo_chocolate.esfriar())
    
    print("\n3. Cada bolo é independente:")
    print(f"Bolo de chocolate está {bolo_chocolate.temperatura}")
    print(f"Bolo de morango está {bolo_morango.temperatura}")

if __name__ == "__main__":
    main() 