Melhores Práticas para Funções e Objetos em Python
Para escrever código Python de alta qualidade, é fundamental seguir convenções que tornam o código mais legível, manutenível e escalável.

Melhores Práticas para Funções 💡
Funções são os blocos de construção do código Python. Usá-las de maneira eficaz é crucial para a clareza do seu projeto.

Princípio da Responsabilidade Única (SRP): Uma função deve fazer uma única coisa. Se você consegue descrever o que a função faz com uma única frase, ela provavelmente segue o SRP. Funções pequenas e focadas são mais fáceis de testar e depurar.

Nomes Descritivos: Os nomes das funções devem ser claros e em snake_case, descrevendo sua finalidade. Evite abreviações e nomes genéricos como processar_dados ou fazer_coisa. Prefira nomes como calcular_desconto_total ou validar_email_usuario.

Argumentos e Retorno Claros: Use dicas de tipo (type hints) para especificar os tipos de dados esperados para os argumentos e o valor de retorno. Isso melhora a legibilidade e permite que ferramentas de análise estática encontrem erros.

Evite Efeitos Colaterais (Side Effects): Se possível, crie funções puras que não modificam variáveis globais, imprimem na tela ou interagem com o mundo exterior. Funções puras são mais fáceis de prever e testar.

Melhores Práticas para Objetos (Classes) 🏛️
Classes são usadas para agrupar dados e funcionalidades relacionadas, seguindo o paradigma da Programação Orientada a Objetos (POO).

Princípio da Responsabilidade Única (SRP): Assim como as funções, uma classe também deve ter uma única razão para mudar. Se uma classe lida com banco de dados, lógica de negócio e interface de usuário, ela está fazendo coisas demais.

Encapsulamento: Use a convenção do sublinhado (_ ou __) para indicar que um atributo ou método é "privado" e não deve ser acessado diretamente de fora da classe. Isso protege os dados e a lógica interna da classe.

Prefira Composição à Herança: Use a herança ("é um") apenas quando uma classe é realmente uma especialização de outra (ex: um Carro "é um" Veiculo). Em vez disso, use a composição ("tem um"), onde uma classe contém uma instância de outra classe para utilizar sua funcionalidade (ex: uma classe Motor dentro de uma classe Carro).

Métodos Mágicos (__dunder__): Use os métodos "dunder" (__init__, __str__, __repr__, etc.) para dar ao seu objeto um comportamento padrão e consistente, como a inicialização ou a representação em string.

O que são Testes de Mock? 🐒
Mocking é uma técnica de teste onde você substitui objetos reais e suas dependências por "objetos falsos" ou "mocks" durante a execução do teste. A palavra mock significa "imitador" ou "simulacro" em inglês.

Imagine que você está testando uma função que interage com uma API externa para buscar dados. Se você executar o teste de verdade, ele fará uma requisição de rede real, o que pode ser lento, instável (se a internet cair), ou até mesmo custar dinheiro. Em vez disso, você pode "mockar" (ou simular) a chamada à API.

Como Funciona: Você cria um objeto mock que se comporta exatamente como o objeto real que ele substitui. Quando sua função de teste chama o objeto mock, ele retorna um valor pré-definido, sem a necessidade de interagir com a dependência real.

Benefícios:

Isolamento: Permite testar uma "unidade" de código isoladamente, sem que suas dependências externas afetem o resultado.

Velocidade: Evita operações lentas como chamadas de rede, acesso a bancos de dados ou leitura de arquivos.

Controle: Permite simular cenários difíceis de reproduzir, como falhas de rede, erros de API ou valores de retorno específicos.

Em Python, a biblioteca padrão unittest.mock e o plugin pytest-mock (que usa a mesma biblioteca por baixo dos panos) são as ferramentas mais comuns para realizar mocking.

Programa Completo: Gerenciador de Usuários e Testes
A seguir, apresento um programa que aplica todos os conceitos discutidos. O código simula um serviço que busca informações de usuários de uma API externa. Para o teste, usamos mocking para simular a resposta da API, garantindo que o teste seja rápido e confiável.

O projeto é dividido em quatro arquivos para demonstrar boas práticas de modularização.

Estrutura do Projeto:
Programa Python Completo com Melhores Práticas e Testes
23 de ago., 15:30

.
├── src/
│   ├── api_client.py
│   └── user_service.py
├── tests/
│   └── test_user_service.py
├── main.py
└── requirements.txt
Este programa demonstra como os conceitos de modularidade, tipagem, manuseio de exceções e, principalmente, a prática de testes com mocking se integram para criar um código robusto e de fácil manutenção. O arquivo de testes (test_user_service.py) mostra como é possível testar a lógica do UserService de forma isolada, sem depender de uma conexão de rede real.