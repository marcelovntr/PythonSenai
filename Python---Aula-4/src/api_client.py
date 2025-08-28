
# src/api_client.py
"""
Simulação de um cliente de API.
Responsabilidade Única: Apenas interagir com a API externa.
"""
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:
    """
    Classe para interagir com uma API de usuários.
    """
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._session = requests.Session()  # Exemplo de encapsulamento

    def get_user_data(self, user_id: int) -> dict:
        """
        Busca os dados de um usuário na API externa.

        Args:
            user_id: O ID do usuário a ser buscado.

        Returns:
            Um dicionário com os dados do usuário.
        
        Raises:
            requests.RequestException: Se a requisição falhar.
        """
        user_url = f"{self.base_url}/users/{user_id}"
        logger.info(f"Tentando buscar dados de usuário em: {user_url}")
        try:
            with self._session as session:
                response = session.get(user_url)
                response.raise_for_status()         # Lança uma exceção para erros HTTP
                return response.json()
        except requests.RequestException as e:
            logger.error(f"Erro na requisição para a API: {e}")
            raise
