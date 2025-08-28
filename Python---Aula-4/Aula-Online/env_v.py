
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente de um arquivo .env
load_dotenv()

# Nunca hard-code segredos no código
# export DB_PASSWORD="value"
# export API_KEY="value"
db_senha = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")

if not db_senha or not api_key:
    print("Aviso: Variáveis de ambiente DB_PASSWORD ou API_KEY não foram carregadas.")
   
else:
    print("Sucesso: Segredos carregados de variáveis de ambiente.")
    print(f"Variáveis de ambiente {db_senha} ou {api_key}")