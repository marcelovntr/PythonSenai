class Vape:

    def __init__(self, sabor, puffs):
        self.sabor = sabor
        self.puffs = puffs
        self.pressao = "normal"

    def puffar(self):
        self.pressao = "cair"
        return f"o vape de {self.sabor} fez a pressão {self.pressao}"
    
    def respirar(self):
        self.pressao = "estabilizar"
        return f"A respiração fez a pressão {self.pressao}"
    
    def entrega(self):
        return f"Entrega premium de vape {self.sabor} e com {self.puffs} cargas efetuada no centro"

def main():
    print("=== Introdução à Programação Orientada a Objetos ===")
    print("\nPense em uma classe como um pedido de vape:")
    print("- O pedido (classe) diz qual vape desejado")
    print("- O vape (objeto) é o que recebe segundo as opções")
    print("- As características (atributos) são coisas como sabor e carga")
    print("- As ações (métodos) são coisas que o vape pode fazer\n")

    print('Pedindo dois vapes distintos:')
    vape_mamae = Vape('morango', 1800)
    vape_pica = Vape('gudang', 5000)

    print(f"Vape fofo: sabor {vape_mamae.sabor} e {vape_mamae.puffs} puffs")
    print(f"Vape macho: sabor {vape_pica.sabor} e {vape_pica.puffs} puffs")

    print("\n2. O que podemos fazer com os vapes?")
    print(vape_pica.entrega())
    print(vape_pica.puffar())
    print(vape_pica.respirar())

    print("\n3. Cada vape é independente:")
    print(f"vape de mamãe faz a pressão {vape_mamae.pressao}")
    print(f"vape de macho faz a pressão {vape_pica.pressao}")

if __name__ == "__main__":
    main() 