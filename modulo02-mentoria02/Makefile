# Makefile para o projeto de exemplos Python

# Comandos para executar os exemplos
run-panda:
	python exemplo_panda.py

run-error:
	python exemplo_error.py

run-error-divisao:
	python exemplo_error_divisao.py

run-texto:
	python exemplo_texto.py

run-boleano:
	python exemplo_boleano.py

run-inteiros:
	python exemplo_inteiros.py

run-decimais:
	python exemplo_decimais.py

# Comando para instalar dependências
install:
	pip install -r requirements.txt

# Comando para limpar arquivos temporários
clean:
	del /Q *.pyc
	del /Q __pycache__

# Comando para mostrar ajuda
help:
	@echo Comandos disponiveis:
	@echo make run-panda    - Executa o exemplo do pandas
	@echo make run-error    - Executa o exemplo de tratamento de erros
	@echo make run-texto    - Executa o exemplo de texto
	@echo make run-boleano  - Executa o exemplo de booleanos
	@echo make run-inteiros - Executa o exemplo de inteiros
	@echo make run-decimais - Executa o exemplo de decimais
	@echo make install     - Instala as dependencias do requirements.txt
	@echo make clean       - Remove arquivos temporarios
	@echo make help        - Mostra esta mensagem de ajuda