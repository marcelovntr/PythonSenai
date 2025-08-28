# Módulo 02 - Mentoria 02

Este projeto contém exemplos práticos de programação em Python, focando em conceitos fundamentais, tratamento de erros e manipulação de dados.

## Conteúdo do Projeto

O projeto inclui vários exemplos práticos:

### Exemplos Básicos
- `exemplo_inteiros.py`: Trabalhando com números inteiros
- `exemplo_decimais.py`: Manipulação de números decimais
- `exemplo_texto.py`: Operações com strings e texto
- `exemplo_boleano.py`: Uso de valores booleanos e operações lógicas

### Exemplos de Tratamento de Erros
- `exemplo_error.py`: Demonstração de tratamento básico de erros com try/except
- `exemplo_error_divisao.py`: Exemplo específico de tratamento de erro em divisão

### Exemplo com Pandas
- `exemplo_panda.py`: Introdução ao pandas com um exemplo simples de notas de alunos
  - Criação de DataFrame
  - Visualização de dados
  - Cálculos básicos (média, máximo, mínimo)

## Requisitos

- Python 3.8 ou superior
- Dependências listadas em `requirements.txt`:
  - pandas==2.2.0
  - numpy==1.26.3
  - requests==2.31.0

## Como Executar

### Usando Make

O projeto inclui um Makefile com comandos simples:

```bash
# Executar exemplos
make run-panda    # Executa o exemplo do pandas
make run-error    # Executa o exemplo de tratamento de erros
make run-texto    # Executa o exemplo de texto
make run-boleano  # Executa o exemplo de booleanos
make run-inteiros # Executa o exemplo de inteiros
make run-decimais # Executa o exemplo de decimais

# Outros comandos
make install     # Instala as dependências
make clean       # Remove arquivos temporários
make help        # Mostra todos os comandos disponíveis
```

### Execução Direta

Alternativamente, você pode executar os exemplos diretamente:

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute os exemplos individualmente:
   ```bash
   python exemplo_error.py
   python exemplo_panda.py
   # etc...
   ```

## Estrutura do Projeto

- `.vscode/`: Configurações do VS Code
  - `launch.json`: Configuração de debug para VS Code
    - Permite executar e debugar os arquivos Python diretamente do VS Code
    - Inclui configurações específicas para cada exemplo
    - Facilita a depuração com breakpoints e inspeção de variáveis
- `Makefile`: Comandos simples para executar os exemplos
- `requirements.txt`: Lista de dependências do projeto
- Arquivos de exemplo: Demonstrações práticas de conceitos Python

## Exemplos Detalhados

### Exemplo com Pandas
O arquivo `exemplo_panda.py` demonstra o uso básico do pandas:
- Criação de um DataFrame simples com notas de alunos
- Visualização dos dados
- Cálculos básicos como média, maior e menor nota

### Exemplos de Tratamento de Erros
Os arquivos `exemplo_error.py` e `exemplo_error_divisao.py` mostram:
- Uso de try/except para capturar erros
- Tratamento de diferentes tipos de erros
- Boas práticas de tratamento de exceções

### Exemplos de Tipos de Dados
Os arquivos `exemplo_inteiros.py`, `exemplo_decimais.py`, `exemplo_texto.py` e `exemplo_boleano.py` demonstram:
- Manipulação de diferentes tipos de dados em Python
- Operações básicas com cada tipo
- Conversões entre tipos

## Configuração do VS Code

O arquivo `.vscode/launch.json` contém configurações para facilitar o desenvolvimento e depuração:

1. **Python: Arquivo Atual**
   - Executa o arquivo Python que está atualmente aberto no editor
   - Útil para testar rapidamente qualquer arquivo

2. **Python: exemplo_panda**
   - Configuração específica para executar o exemplo do pandas
   - Facilita a depuração do código de manipulação de dados

3. **Python: exemplo_error**
   - Configuração específica para executar os exemplos de tratamento de erros
   - Ajuda a debugar o comportamento do código em diferentes cenários de erro

Para usar o debugger:
1. Abra o arquivo Python desejado
2. Defina breakpoints clicando na margem esquerda do editor
3. Pressione F5 ou use o menu de debug do VS Code
4. Selecione a configuração desejada
5. Use os controles de debug para:
   - Executar linha por linha
   - Inspecionar variáveis
   - Ver a pilha de chamadas
   - Avaliar expressões
