# Módulo 02 - Mentoria 05

Este projeto contém exemplos práticos de estruturas de dados em Python, focando em listas, tuplas, conjuntos, dicionários e filas (deque).

## Conteúdo do Projeto

O projeto inclui vários exemplos práticos de estruturas de dados:

### Exemplos de Estruturas de Dados
- `exemplo_lista.py`: Demonstrações de operações com listas
- `exemplo_tupla.py`: Exemplos de uso de tuplas
- `exemplo_conjunto.py`: Demonstrações de conjuntos
- `exemplo_dicionario.py`: Exemplos de dicionários
- `exemplo_fila.py`: Demonstrações de filas (deque)
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
   python exemplo_lista.py
   python exemplo_tupla.py
   python exemplo_conjunto.py
   python exemplo_dicionario.py
   python exemplo_fila.py
   ```

## Estrutura do Projeto

- `Makefile`: Comandos para executar o projeto
- `exemplo_lista.py`: Demonstrações de listas
- `exemplo_tupla.py`: Demonstrações de tuplas
- `exemplo_conjunto.py`: Demonstrações de conjuntos
- `exemplo_dicionario.py`: Demonstrações de dicionários
- `exemplo_fila.py`: Demonstrações de filas (deque)
- `exemplo_menu_principal.py`: Menu interativo com todos os exemplos

## Exemplos Detalhados

### Listas
O arquivo `exemplo_lista.py` demonstra:
- Adição de elementos com input:
  ```python
  while True:
      numero = input("Digite um número (ou 's' para sair): ")
      if numero.lower() == 's':
          break
      numeros.append(float(numero))
  ```
- Iteração com for:
  ```python
  for i, num in enumerate(numeros, 1):
      print(f"{i}. {num}")
  ```
- Cálculos com listas:
  ```python
  media = sum(numeros) / len(numeros)
  ```

### Dicionários
O arquivo `exemplo_dicionario.py` mostra:
- Criação de dicionário:
  ```python
  pessoa = {
      "nome": "João",
      "idade": 20
  }
  ```
- Modificação de valores:
  ```python
  pessoa["nome"] = novo_nome
  pessoa["idade"] = nova_idade
  ```

### Filas (Deque)
O arquivo `exemplo_fila.py` demonstra:
- Adição de elementos:
  ```python
  fila.append(nome)
  ```
- Atendimento (remoção):
  ```python
  pessoa_atendida = fila.popleft()
  ```
- Verificação de fila vazia:
  ```python
  match len(fila):
      case 0:
          print("Fila vazia!")
  ```

## Estruturas de Dados Utilizadas

### Listas
- Coleção ordenada e mutável
- Permite elementos duplicados
- Acesso por índice
- Exemplos: coleções de números, nomes, etc.

### Tuplas
- Coleção ordenada e imutável
- Permite elementos duplicados
- Acesso por índice
- Exemplos: coordenadas, configurações fixas

### Conjuntos
- Coleção não ordenada e mutável
- Não permite elementos duplicados
- Operações de conjunto (união, interseção)
- Exemplos: conjunto de IDs únicos

### Dicionários
- Coleção de pares chave-valor
- Chaves únicas
- Valores podem ser de qualquer tipo
- Exemplos: cadastros, configurações

### Filas (Deque)
- Estrutura de dados dupla (FIFO/LIFO)
- Operações eficientes nas extremidades
- Exemplos: filas de atendimento

## Comparativo Rápido das Estruturas de Dados

| Tipo | Mutável | Ordenado | Ítens repetidos | Acesso por índice | Uso comum |
|------|---------|----------|-----------------|-------------------|-----------|
| list | ✅ | ✅ | ✅ | ✅ | Qualquer coleção de dados |
| tuple | ❌ | ✅ | ✅ | ✅ | Dados fixos que não mudam |
| set | ✅ | ❌ | ❌ | ❌ | Eliminar duplicatas |
| deque | ✅ | ✅ | ✅ | ✅ (com limitações) | Filas e pilhas (queue, stack) |
| array | ✅ | ✅ | ✅ | ✅ | Dados numéricos (ex: sensores) |

## Padrão de Saída
Todos os exemplos seguem o mesmo padrão de saída:
1. Título do programa
2. Explicação da estrutura
3. Entrada do usuário
4. Processamento
5. Resultado formatado

## Debugging (Depuração)

### O que é Debugging?
Debugging é o processo de encontrar e corrigir erros (bugs) no seu programa. Com estruturas de dados, é importante verificar:
- Tipos de dados corretos
- Índices válidos
- Chaves existentes
- Estado das estruturas

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

6. **Dicas para Debug de Estruturas de Dados**
   - Monitore o conteúdo das estruturas
   - Verifique os tipos de dados
   - Observe as operações de modificação
   - Use o console de debug para testar expressões
   - Os valores são atualizados em tempo real
