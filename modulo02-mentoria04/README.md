# Módulo 02 - Mentoria 04

Este projeto contém exemplos práticos de estruturas de repetição em Python, focando em loops for, while, break e continue.

## Conteúdo do Projeto

O projeto inclui vários exemplos práticos de estruturas de repetição:

### Exemplos de Loops
- `exemplos_for.py`: Demonstrações de diferentes usos do loop for
- `exemplos_while.py`: Exemplos de loops while com diferentes controles
- `exemplo_menu_principal.py`: Menu integrado com todos os exemplos

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

Alternativamente, você pode executar os exemplos diretamente:

1. Clone o repositório
2. Execute o menu principal:
   ```bash
   python exemplo_menu_principal.py
   ```
3. Ou execute exemplos individuais:
   ```bash
   python exemplos_for.py
   python exemplos_while.py
   ```

## Estrutura do Projeto

- `Makefile`: Comandos para executar o projeto
- `exemplos_for.py`: Demonstrações de loops for
- `exemplos_while.py`: Demonstrações de loops while
- `exemplo_menu_principal.py`: Menu interativo com todos os exemplos

## Exemplos Detalhados

### Loops FOR
O arquivo `exemplos_for.py` demonstra:
- For com range usando input:
  ```python
  for numero in range(inicio, fim + 1):
      print(f"Número: {numero}")
  ```
- Percorrer lista com comparação:
  ```python
  for nome in nomes:
      if nome.lower() == nome_busca.lower():
          print(f"Nome encontrado: {nome}")
          break
  ```
- Contagem entre dois valores:
  ```python
  for i in range(valor_a, valor_b + 1):
      print(f"Valor atual: {i}")
  ```

### Loops WHILE
O arquivo `exemplos_while.py` mostra:
- While com contador:
  ```python
  while contador <= numero:
      print(f"Contador: {contador}")
      contador += 1
  ```
- While verificando senha:
  ```python
  while tentativas < max_tentativas:
      if senha == senha_correta:
          print("Senha correta!")
          break
  ```
- While com break:
  ```python
  while True:
      if numero == 0:
          break
      soma += numero
  ```
- While com continue:
  ```python
  while True:
      if numero % 2 != 0:
          continue
      soma_pares += numero
  ```

### Menu Principal
O arquivo `exemplo_menu_principal.py` integra:
- Todos os exemplos em um menu interativo
- Navegação usando match/case
- Padrão consistente de saída

## Estruturas de Repetição Utilizadas

### Loop FOR
- Usado para iterar sobre sequências (listas, ranges, etc.)
- Controle preciso do número de iterações
- Ideal para quando se conhece o número de repetições
- Exemplos: contagem, iteração em listas, ranges personalizados

### Loop WHILE
- Executa enquanto uma condição for verdadeira
- Mais flexível que o for
- Útil quando não se sabe o número de iterações
- Exemplos: verificação de senha, entrada de dados, contadores

### Controle de Fluxo
- `break`: Interrompe a execução do loop
- `continue`: Pula para a próxima iteração
- Útil para controle de fluxo dentro dos loops
- Exemplos: saída antecipada, filtragem de valores

## Padrão de Saída
Todos os exemplos seguem o mesmo padrão de saída:
1. Título do programa
2. Entrada do usuário
3. Processamento
4. Resultado formatado

## Debugging (Depuração)

### O que é Debugging?
Debugging é o processo de encontrar e corrigir erros (bugs) no seu programa. Com loops, é especialmente importante verificar:
- Condições de parada
- Incrementos/decrementos
- Valores das variáveis de controle
- Fluxo de execução

### Como Fazer Debug no VS Code/Cursor

1. **Configurar o Debug**
   - O arquivo `.vscode/launch.json` já está configurado para o menu principal
   - Você pode adicionar mais configurações para outros arquivos

2. **Iniciar o Debug**
   - Pressione F5 ou clique no ícone de "Play" com o inseto (🐞)
   - Selecione "Python: Menu Principal" na lista de configurações

3. **Pontos de Interrupção (Breakpoints)**
   - Clique na linha onde quer parar (aparece um ponto vermelho)
   - O programa vai parar nessa linha durante a execução

4. **Controles do Debug**
   - ▶️ Continue (F5): Continua a execução
   - ⤵️ Step Over (F10): Executa a linha atual
   - ⤵️ Step Into (F11): Entra dentro da função
   - ⤴️ Step Out (Shift+F11): Sai da função atual
   - ⏹️ Stop (Shift+F5): Para a execução

5. **Painel de Debug**
   - VARIABLES: Mostra todas as variáveis e seus valores
   - WATCH: Adicione variáveis para monitorar
   - CALL STACK: Mostra onde você está no código
   - BREAKPOINTS: Lista todos os pontos de parada

6. **Dicas para Debug de Loops**
   - Monitore as variáveis de controle do loop
   - Verifique as condições de parada
   - Observe o fluxo de execução com break/continue
   - Use o console de debug para testar expressões
   - Os valores das variáveis são atualizados em tempo real
