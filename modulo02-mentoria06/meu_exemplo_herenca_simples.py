class Veiculo:
    def __init__(self, marca, modelo, ano):
       self.marca = marca
       self.modelo = modelo
       self.ano = ano
       self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        return f"{self.marca} {self.modelo} acelerou até {self.velocidade} km/h"
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade = 0
        return f"{self.marca} {self.modelo} freou!"
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo}, {self.ano}"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def abrir_portas(self, num_porta):
        if 1 <= num_porta <= self.portas:
            return f"Porta {num_porta} do {self.marca} {self.modelo} aberta"
        return f"O {self.marca} {self.modelo} não tem porta {num_porta}"
    
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica}, {self.portas} portas"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas  = cilindradas
    
    def empinar(self):
        return f"A {self.marca} {self.modelo} empinou!!!"
    
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica}, {self.cilindradas}cc"

def main():
    print("=== Introdução à Herança ===")
    print("\nHerança: uma classe herda caract.(atributos) de uma super.")

    print("Criando (instanciando) um carro: ")

    carrinho = Carro('Chevrolet', 'Chevete', 1990, 4)
    print(carrinho.abrir_portas(3))
    print(carrinho.mostrar_info())
    print(carrinho.acelerar())

    motona = Moto('Suzuki', 'Samurai', 2055, 999)
    motona.mostrar_info()
    motona.acelerar()
    motona.empinar()

    print("\n3. O que todos os veículos podem fazer:")
    veiculos = [carrinho, motona]
    for veiculo in veiculos:
        print(f"{veiculo.marca} {veiculo.modelo}")
        print(veiculo.acelerar())
        print(veiculo.frear())
    
    print("\n4. Verificando a herança:")
    print(f"Carro é um Veículo? {isinstance(carrinho, Veiculo)}")
    print(f"Moto é um Veículo? {isinstance(motona, Veiculo)}")

if __name__ == "__main__":
    main() 