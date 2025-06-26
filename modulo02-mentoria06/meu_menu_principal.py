from meu_exemplo_basico import Vape
from meu_exemplo_herenca_simples import Veiculo, Carro, Moto
from meu_exemplo_encapsulamento import Poupanca
from meu_exemplo_abstracao import ControleAbstrato, ControleAc, ControleTv
class MeuMenu:
    def __init__(self):
        self.vapes = []
        self.dividas = []
        self.veiculos = []
        self.formas = []

    def limpar_tela(self):
        print("\n" *20)
    
    def mostrar_menu(self):
        while True:
            self.limpar_tela()
            print("=== Menu Principal - Exemplos de POO ===")
            print("\nEscolha um exemplo para executar:")
            print("1. Classe e Objeto (Vape)")
            print("2. Encapsulamento (Conta Poupança)")
            print("3. Herança (Veículos)")
            print("4. Abstração e Polimorfismo (Controles Remotos)")
            print("0. Sair")

            opcao = input("\nDigite a opção:")

            match opcao:
                case "1":
                    self.exemplo_vape()
                case "2":
                    self.exemplo_conta_poupanca()
                case "3":
                    self.exemplo_veiculo()
                case "4":
                    self.exemplo_formas()
                case "0":
                    print("\nSaindo do programa...")
                    break
                case _:
                    print("\nOpção inválida!")
            
            input("\nPressione Enter para continuar...")

        
    def exemplo_vape(self):
        self.limpar_tela()
        print("=== Exemplo de Classe e Objeto ===")
        sabor = input("Digite o sabor do vape:")
        puffs = input("Digite a quantidade de puffs:")

        vapezinho = Vape(sabor,puffs)
        self.vapes.append(vapezinho)
        print(f"{vapezinho.entrega()}")
        print(f"Aquela tragada gostosa e {vapezinho.puffar()}")
        print(f"{vapezinho.respirar()}")

    def exemplo_veiculo(self):
        self.limpar_tela()
        print("=== Exemplo de Herança ===")
        print("\nEscolha o tipo de veículo:")
        print("1. Carro")
        print("2. Moto")
        opcao = input("\n Digite sua escolha: ")

        marca = input("digite a marca: ")
        modelo = input("digite o modelo: ")
        ano = int(input("digite o ano: "))

        if opcao == "1":
            num_portas = int(input("Digite o número de portas: "))
            veiculo = Carro(marca, modelo, ano, num_portas)
            print(f"\nCarro criado: {veiculo.mostrar_info()}")
            print(veiculo.acelerar())
        elif opcao == "2":
            cilindradas = int(input("Digite as cilindradas: "))
            veiculo = Moto(marca, modelo, ano, cilindradas)
            print(f"\nMoto criada: {veiculo.mostrar_info()}")
            print(veiculo.acelerar())
        else:
            print("\nOpção inválida!")
            return

    def exemplo_conta_poupanca(self):
        self.limpar_tela()
        print("=== Exemplo de Encapsulamento ===")
        nome = input("\nDigite o nome do titular: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))

        nova_conta = Poupanca(nome, saldo_inicial)
        self.dividas.append(nova_conta)

        print("\nOperações disponíveis:")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Mudar senha")
        opcao = input("\nDigite sua opção: ")

        if opcao == '1':
            print(nova_conta.ver_saldo())
        elif opcao == '2':
            valor = float(input("Digite o valor para depositar: "))
            senha = input("Digite a senha: ")
            print(nova_conta.deposito(valor, senha))
        elif opcao == '3':
            valor = float(input("Digite o valor para sacar: "))
            senha = input("Digite sua senha para confirmar: ")
            print(nova_conta.saque(valor, senha))
        elif opcao == "4":
            atual = input("Digite sua senha ATUAL: ")
            nova = input("Digite sua NOVA senha: ")
            print(nova_conta.mudar_senha(atual, nova))

    def exemplo_formas(self):
        self.limpar_tela()
        print("=== Exemplo de Abstração e Polimorfismo ===")
        print("\nEscolha o tipo de controle:")
        print("1. Controle de TV")
        print("2. Controle de Ar Condicionado")

        opcao = input("\nDigite sua opção: ").lower().strip()

        if opcao == "tv":
            controle = ControleTv()
            print("\nControle de TV criado!")
            print(controle.on())
            valor = int(input("Digite o volume (0-100): "))
            print(controle.adjust(valor))
            print(controle.off())
            
        elif opcao == "ar":
            controle_ar = ControleAc()
            print("\nControle de Ar Condicionado criado!")
            print(controle.on())
            temp = int(input("Digite a temperatura (16-30): "))
            print(controle_ar.adjust(temp))
            print(controle_ar.off())

        else:
            print("Opção inválida!")
            return
        self.formas.append(controle)
        print(f"\nTotal de controles criados: {len(self.formas)}")


if __name__ == "__main__":
    menu = MeuMenu()
    menu.mostrar_menu()