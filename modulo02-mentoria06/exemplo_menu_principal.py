"""
Menu Principal - Exemplos de Programação Orientada a Objetos

Este módulo demonstra os principais conceitos de Programação Orientada a Objetos (POO) através
de exemplos práticos e interativos. Os conceitos demonstrados incluem:

1. Classes e Objetos: Demonstração básica de como criar e usar classes/objetos
2. Encapsulamento: Proteção de dados e métodos através de modificadores de acesso
3. Herança: Reutilização de código e hierarquia de classes
4. Abstração e Polimorfismo: Interfaces comuns e comportamentos específicos

Cada exemplo é implementado em seu próprio módulo e demonstrado através deste menu interativo.
"""

from exemplo_basico import Bolo
from exemplo_encapsulamento_simples import ContaPoupanca
from exemplo_heranca_simples import Veiculo, Carro, Moto
from exemplo_abstracao_controle import ControleRemoto, ControleTV, ControleAr

class MenuPrincipal:
    """
    Classe principal que gerencia o menu interativo e demonstração dos exemplos de POO.
    
    Esta classe implementa um padrão de menu interativo que permite ao usuário:
    - Navegar entre diferentes exemplos de POO
    - Criar e manipular objetos de diferentes classes
    - Visualizar os resultados das operações em tempo real
    
    Atributos:
        bolos (list): Lista para armazenar instâncias de Bolo
        contas (list): Lista para armazenar instâncias de ContaPoupanca
        veiculos (list): Lista para armazenar instâncias de Veiculo (Carro/Moto)
        formas (list): Lista para armazenar instâncias de ControleRemoto (TV/Ar)
    """
    
    def __init__(self):
        """Inicializa as listas que armazenarão as instâncias dos objetos criados."""
        self.bolos = []
        self.contas = []
        self.veiculos = []
        self.formas = []
    
    def limpar_tela(self):
        """Limpa a tela do terminal para melhor visualização do menu."""
        print("\n" * 50)
    
    def mostrar_menu(self):
        """
        Exibe o menu principal e gerencia a navegação entre os exemplos.
        
        Implementa um loop infinito que:
        1. Limpa a tela
        2. Mostra as opções disponíveis
        3. Processa a escolha do usuário
        4. Executa o exemplo selecionado
        5. Aguarda confirmação antes de continuar
        
        O loop só é interrompido quando o usuário escolhe sair (opção 0).
        """
        while True:
            self.limpar_tela()
            print("=== Menu Principal - Exemplos de POO ===")
            print("\nEscolha um exemplo para executar:")
            print("1. Classe e Objeto (Bolo)")
            print("2. Encapsulamento (Conta Poupança)")
            print("3. Herança (Veículos)")
            print("4. Abstração e Polimorfismo (Controles Remotos)")
            print("0. Sair")
            
            opcao = input("\nDigite sua opção: ")
            
            if opcao == "1":
                self.exemplo_bolo()
            elif opcao == "2":
                self.exemplo_conta_poupanca()
            elif opcao == "3":
                self.exemplo_veiculos()
            elif opcao == "4":
                self.exemplo_formas()
            elif opcao == "0":
                print("\nSaindo do programa...")
                break
            else:
                print("\nOpção inválida!")
            
            input("\nPressione Enter para continuar...")
    
    def exemplo_bolo(self):
        """
        Demonstra o conceito básico de Classes e Objetos.
        
        Este exemplo mostra:
        - Criação de um objeto (instância de classe)
        - Acesso a atributos
        - Chamada de métodos
        - Armazenamento de objetos em uma lista
        
        Complexidade: Baixa - Demonstração introdutória de POO
        """
        self.limpar_tela()
        print("=== Exemplo de Classe e Objeto ===")
        
        sabor = input("\nDigite o sabor do bolo: ")
        tamanho = input("Digite o tamanho (pequeno/médio/grande): ")
        
        bolo = Bolo(sabor, tamanho)
        self.bolos.append(bolo)
        
        print(f"\nBolo criado: {bolo.servir()}")
        print(f"Temperatura inicial: {bolo.temperatura}")
        print(bolo.esquentar())
        print(bolo.esfriar())
        print(f"\nTotal de bolos criados: {len(self.bolos)}")
    
    def exemplo_conta_poupanca(self):
        """
        Demonstra o conceito de Encapsulamento.
        
        Este exemplo ilustra:
        - Proteção de dados através de atributos privados
        - Validação de operações através de métodos
        - Controle de acesso usando senha
        - Modificação segura de atributos
        
        Complexidade: Média - Implementa segurança e validação de dados
        """
        self.limpar_tela()
        print("=== Exemplo de Encapsulamento ===")
        
        nome = input("\nDigite o nome do titular: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        
        conta = ContaPoupanca(nome, saldo_inicial)
        self.contas.append(conta)
        
        print("\nOperações disponíveis:")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Mudar senha")
        
        opcao = input("\nDigite sua opção: ")
        
        if opcao == "1":
            print(conta.ver_saldo())
        elif opcao == "2":
            valor = float(input("Digite o valor para depositar: "))
            senha = input("Digite a senha: ")
            print(conta.depositar(valor, senha))
        elif opcao == "3":
            valor = float(input("Digite o valor para sacar: "))
            senha = input("Digite a senha: ")
            print(conta.sacar(valor, senha))
        elif opcao == "4":
            senha_atual = input("Digite a senha atual: ")
            nova_senha = input("Digite a nova senha: ")
            print(conta.mudar_senha(senha_atual, nova_senha))
    
    def exemplo_veiculos(self):
        """
        Demonstra o conceito de Herança.
        
        Este exemplo mostra:
        - Hierarquia de classes (Veiculo -> Carro/Moto)
        - Reutilização de código através de herança
        - Sobrescrita de métodos (polimorfismo)
        - Atributos e métodos específicos de cada subclasse
        
        Complexidade: Média - Implementa herança e polimorfismo básico
        """
        self.limpar_tela()
        print("=== Exemplo de Herança ===")
        
        print("\nEscolha o tipo de veículo:")
        print("1. Carro")
        print("2. Moto")
        
        opcao = input("\nDigite sua opção: ")
        
        marca = input("Digite a marca: ")
        modelo = input("Digite o modelo: ")
        ano = int(input("Digite o ano: "))
        
        if opcao == "1":
            num_portas = int(input("Digite o número de portas: "))
            veiculo = Carro(marca, modelo, ano, num_portas)
            print(f"\nCarro criado: {veiculo.mostrar_info()}")
            print(veiculo.acelerar())
            print(veiculo.abrir_porta(1))
        elif opcao == "2":
            cilindradas = int(input("Digite as cilindradas: "))
            veiculo = Moto(marca, modelo, ano, cilindradas)
            print(f"\nMoto criada: {veiculo.mostrar_info()}")
            print(veiculo.acelerar())
            print(veiculo.empinar())
        else:
            print("Opção inválida!")
            return
        
        self.veiculos.append(veiculo)
        print(f"\nTotal de veículos criados: {len(self.veiculos)}")
    
    def exemplo_formas(self):
        """
        Demonstra os conceitos de Abstração e Polimorfismo.
        
        Este exemplo ilustra:
        - Classes abstratas (ControleRemoto)
        - Implementação de interfaces comuns
        - Polimorfismo através de métodos comuns
        - Comportamentos específicos para cada tipo de controle
        
        Complexidade: Alta - Implementa abstração e polimorfismo avançado
        """
        self.limpar_tela()
        print("=== Exemplo de Abstração e Polimorfismo ===")
        
        print("\nEscolha o tipo de controle:")
        print("1. Controle de TV")
        print("2. Controle de Ar Condicionado")
        
        opcao = input("\nDigite sua opção: ")
        
        if opcao == "1":
            controle = ControleTV()
            print("\nControle de TV criado!")
            print(controle.ligar())
            valor = int(input("Digite o volume (0-100): "))
            print(controle.ajustar(valor))
            print(controle.desligar())
        elif opcao == "2":
            controle = ControleAr()
            print("\nControle de Ar Condicionado criado!")
            print(controle.ligar())
            valor = int(input("Digite a temperatura (16-30): "))
            print(controle.ajustar(valor))
            print(controle.desligar())
        else:
            print("Opção inválida!")
            return
        
        self.formas.append(controle)
        print(f"\nTotal de controles criados: {len(self.formas)}")

if __name__ == "__main__":
    # Ponto de entrada do programa
    # Cria uma instância do menu e inicia a interface interativa
    menu = MenuPrincipal()
    menu.mostrar_menu() 