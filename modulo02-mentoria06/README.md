# Módulo 02 - Mentoria 06

Este projeto contém exemplos práticos de Programação Orientada a Objetos (POO) em Python, focando em classes, métodos, atributos e os quatro pilares da POO.

## Introdução à Programação Orientada a Objetos (POO)

### O que é POO?
Imagine que você está construindo uma casa. Antes de começar, você precisa de um projeto (planta) que mostra como a casa será. Na programação, é a mesma coisa! POO é uma forma de organizar seu código como se fossem "projetos" de coisas reais.

### Por que usar POO?
- **Organização**: Mantém seu código organizado e fácil de entender
- **Reutilização**: Você pode reutilizar código sem precisar copiar e colar
- **Manutenção**: É mais fácil fazer mudanças e corrigir problemas
- **Escalabilidade**: Facilita o crescimento do seu programa

### Analogia com o Mundo Real
Vamos usar uma analogia com um restaurante:
- **Classe** é como a receita de um prato
- **Objeto** é o prato pronto que você faz seguindo a receita
- **Atributos** são as características (como temperatura, sabor)
- **Métodos** são as ações (como servir, aquecer)

### Exemplo Simples: Uma Lanchonete
```python
class Lanche:
    def __init__(self, nome, preco):
        self.nome = nome    # atributo: nome do lanche
        self.preco = preco  # atributo: preço do lanche
        self.quente = False # atributo: estado do lanche
    
    def esquentar(self):    # método: ação de esquentar
        self.quente = True
        print(f"{self.nome} está quentinho!")
    
    def servir(self):       # método: ação de servir
        if self.quente:
            print(f"Aqui está seu {self.nome} quentinho!")
        else:
            print(f"Aqui está seu {self.nome}!")

# Criando lanches (objetos)
x_burger = Lanche("X-Burger", 15.90)
x_salada = Lanche("X-Salada", 17.90)

# Usando os lanches
x_burger.esquentar()  # X-Burger está quentinho!
x_burger.servir()     # Aqui está seu X-Burger quentinho!
x_salada.servir()     # Aqui está seu X-Salada!
```

### Os 4 Pilares da POO (Explicação Simplificada)

1. **Encapsulamento** (Proteção)
   - É como uma cápsula de remédio: protege o que está dentro
   - Exemplo: Sua conta bancária tem senha para proteger seu dinheiro
   ```python
   class ContaSegura:
       def __init__(self, senha):
           self.__senha = senha  # privado: ninguém pode ver
           self.__saldo = 0      # privado: ninguém pode mudar diretamente
       
       def depositar(self, valor, senha):
           if senha == self.__senha:  # verifica a senha
               self.__saldo += valor
               print("Depósito realizado!")
           else:
               print("Senha errada!")
   ```

2. **Herança** (Reutilização)
   - É como herdar características dos pais
   - Exemplo: Um cachorro é um animal, então herda características de animal
   ```python
   class Animal:
       def __init__(self, nome):
           self.nome = nome
       
       def dormir(self):
           print(f"{self.nome} está dormindo...")

   class Cachorro(Animal):  # Cachorro herda de Animal
       def latir(self):
           print(f"{self.nome} está latindo: Au au!")

   # Uso
   rex = Cachorro("Rex")
   rex.dormir()  # Rex está dormindo... (herdado de Animal)
   rex.latir()   # Rex está latindo: Au au! (específico de Cachorro)
   ```

3. **Polimorfismo** (Múltiplas Formas)
   - É como diferentes animais fazendo sons diferentes
   - Exemplo: Cada animal faz seu próprio som
   ```python
   class Animal:
       def fazer_som(self):
           pass

   class Cachorro(Animal):
       def fazer_som(self):
           return "Au au!"

   class Gato(Animal):
       def fazer_som(self):
           return "Miau!"

   # Uso
   animais = [Cachorro(), Gato()]
   for animal in animais:
       print(animal.fazer_som())  # Cada um faz seu próprio som
   ```

4. **Abstração** (Simplificação)
   - É como um controle remoto: você só precisa saber os botões
   - Exemplo: Você não precisa saber como a TV funciona por dentro
   ```python
   from abc import ABC, abstractmethod

   class ControleRemoto(ABC):
       @abstractmethod
       def ligar(self):
           pass
       
       @abstractmethod
       def desligar(self):
           pass

   class ControleTV(ControleRemoto):
       def ligar(self):
           return "TV ligando..."
       
       def desligar(self):
           return "TV desligando..."

   # Uso
   controle = ControleTV()
   print(controle.ligar())    # TV ligando...
   print(controle.desligar()) # TV desligando...
   ```

### Dicas para Iniciantes em POO

1. **Comece Pequeno**
   - Comece com classes simples
   - Adicione funcionalidades gradualmente
   - Teste cada nova funcionalidade

2. **Use Nomes Descritivos**
   - Nomeie classes como substantivos (Carro, Pessoa)
   - Nomeie métodos como verbos (acelerar, frear)
   - Use nomes que façam sentido

3. **Pense em Objetos do Mundo Real**
   - Identifique objetos ao seu redor
   - Pense nas suas características (atributos)
   - Pense nas suas ações (métodos)

4. **Mantenha a Simplicidade**
   - Uma classe deve ter uma responsabilidade
   - Evite classes muito grandes
   - Divida problemas complexos em partes menores

## Conteúdo do Projeto

O projeto inclui exemplos práticos dos principais conceitos de POO:

### Exemplos de POO
- Classes e Objetos
- Encapsulamento
- Herança
- Polimorfismo
- Abstração

## Requisitos

- Python 3.10 ou superior
- Nenhuma dependência externa necessária

## Como Executar

### Usando Make

O projeto inclui um Makefile com comandos simples:

```bash
# Executar o menu principal
make run

# Limpar arquivos temporários
make clean
```

### Execução Direta

Alternativamente, você pode copiar e executar os exemplos diretamente do README:

1. Clone o repositório
2. Copie os exemplos de código do README
3. Execute em seu ambiente Python

## Estrutura do Projeto

- `README.md`: Documentação e exemplos de código
- `Makefile`: Comandos para executar o projeto

## Exemplos Detalhados

### Classes e Objetos
Demonstração de uma classe simples:
```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 10
        print(f"Velocidade atual: {self.velocidade} km/h")
    
    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Velocidade atual: {self.velocidade} km/h")

# Uso
meu_carro = Carro("Toyota", "Corolla", 2023)
meu_carro.acelerar()  # Velocidade atual: 10 km/h
meu_carro.frear()     # Velocidade atual: 0 km/h
```

### Encapsulamento
Exemplo de proteção de dados:
```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular  # Atributo protegido
        self.__saldo = saldo     # Atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado.")
    
    def get_saldo(self):
        return self.__saldo

# Uso
conta = ContaBancaria("João", 1000)
conta.depositar(500)
print(f"Saldo: R${conta.get_saldo()}")
```

### Herança
Exemplo de reutilização de código:
```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} faz: Au au!"

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} faz: Miau!"

# Uso
cachorro = Cachorro("Rex")
gato = Gato("Mimi")
print(cachorro.fazer_som())  # Rex faz: Au au!
print(gato.fazer_som())      # Mimi faz: Miau!
```

### Polimorfismo
Exemplo de diferentes comportamentos:
```python
class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * self.raio ** 2

# Uso
formas = [Retangulo(5, 3), Circulo(2)]
for forma in formas:
    print(f"Área: {forma.calcular_area()}")
```

### Abstração
Exemplo de interface abstrata:
```python
from abc import ABC, abstractmethod

class DispositivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Smartphone(DispositivoEletronico):
    def ligar(self):
        return "Smartphone ligando..."
    
    def desligar(self):
        return "Smartphone desligando..."

# Uso
smartphone = Smartphone()
print(smartphone.ligar())    # Smartphone ligando...
print(smartphone.desligar()) # Smartphone desligando...
```

## Debugging (Depuração)

### O que é Debugging?
Debugging é o processo de encontrar e corrigir erros (bugs) no seu programa. Com POO, é importante verificar:
- Inicialização correta dos objetos
- Estado dos atributos
- Chamadas de métodos
- Hierarquia de classes

### Como Fazer Debug no VS Code/Cursor

1. **Configurar o Debug**
   - O arquivo `.vscode/launch.json` já está configurado
   - Você pode adicionar mais configurações para outros arquivos

2. **Iniciar o Debug**
   - Pressione F5 ou clique no ícone de "Play" com o inseto (🐞)
   - Selecione a configuração desejada

3. **Pontos de Interrupção (Breakpoints)**
   - Clique na linha onde quer parar (aparece um ponto vermelho)
   - O programa vai parar nessa linha durante a execução

4. **Controles do Debug**
   - ▶️ Continue (F5): Continua a execução
   - ⤵️ Step Over (F10): Executa a linha atual
   - ⤵️ Step Into (F11): Entra dentro do método
   - ⤴️ Step Out (Shift+F11): Sai do método atual
   - ⏹️ Stop (Shift+F5): Para a execução

5. **Painel de Debug**
   - VARIABLES: Mostra todos os objetos e seus atributos
   - WATCH: Adicione variáveis para monitorar
   - CALL STACK: Mostra onde você está no código
   - BREAKPOINTS: Lista todos os pontos de parada

6. **Dicas para Debug de POO**
   - Monitore o estado dos objetos
   - Verifique a hierarquia de classes
   - Observe as chamadas de métodos
   - Use o console de debug para testar expressões
   - Os valores são atualizados em tempo real

## Padrão de Código
Todos os exemplos seguem o mesmo padrão:
1. Definição da classe
2. Método __init__ para inicialização
3. Métodos públicos para interação
4. Exemplo de uso com instanciação
5. Demonstração de funcionalidades

