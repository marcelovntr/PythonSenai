from abc import ABC, abstractmethod

class ControleAbstrato(ABC):#abstrata (contrato) dita "obrigações" das concretas
    @abstractmethod #força implementação dos métodos nas classes filhas
    def on(self):
        pass
    @abstractmethod
    def off(self):
        pass
    
    @abstractmethod
    def adjust(self, valor):
        pass

class ControleTv(ControleAbstrato):
    def __init__(self):
        self.ligada = False
        self.volume = 0
    
    def on(self):
        self.ligada = True
        return "TV on!"
    
    def off(self):
        self.ligada = False
        return "TV off!"
    
    def adjust(self, valor):
        if not self.ligada:
            return "TV is off"
        self.volume = max(0, min(100, valor))#menor entre 100 e valor.
                     #maior entre 0 e 100
        return f"Volume ajustado para {self.volume}"

class ControleAc(ControleAbstrato):
    def __init__(self):
        self.ligado = False
        self.temperatura = 25
    
    def on(self):
        self.ligado = True
        return "Ar ligado, neam!"
    
    def off(self):
        self.ligado = False
        return "ar desligado!"
    
    def adjust(self, valor):
        if not self.ligado:
            return "Pi, pi! Ar ainda desligado"
        self.temperatura = max(16, min(30, valor))
        return f"Temperatura ajustada para {self.temperatura}°C"

def main():
    print("=== Exemplo Simples de Abstração ===")
    print("\nAbstração: 'contrato' que define obrigações.")
    print("- Ligar; - Desligar; - Ajustar(vol., temp., etc)")

    print("1. Usando o controle da TV:")
    tv_controle = ControleTv()
    print(tv_controle.on())
    print(tv_controle.adjust(30))
    print(tv_controle.off())

    print("\n2. Usando o controle do Ar Condicionado:")
    ar_controle = ControleAc()
    print(ar_controle.on())
    print(ar_controle.adjust(18))
    print(ar_controle.off())

    print("\n3. Todos os controles seguem o mesmo contrato:")
    controles = [tv_controle, ar_controle]
    for controle in controles:
        print(f"\n{controle.__class__.__name__}:")
        print(controle.ligar())
        print(controle.ajustar(30))
        print(controle.desligar())
    
        print("\n4. Tentando criar um controle sem implementar o contrato:")
    try:
        controle = ControleAbstrato()  # Isso vai gerar um erro
    except TypeError as e:
        print(f"Erro: {e}")
        print("Não podemos criar um controle sem implementar o contrato!")

if __name__ == "__main__":
    main() 