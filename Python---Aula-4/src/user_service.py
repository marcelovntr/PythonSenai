"""
Serviço de lógica de negócio para manipulação de usuários.
Responsabilidade Única: Contém a lógica de negócio do usuário.
"""
import logging
from typing import Dict, Any, Optional
from src.data_store import DataStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    """
    Serviço que utiliza o armazenamento de dados para obter e processar dados de usuário.
    Este é um exemplo de COMPOSIÇÃO: o UserService "tem um" DataStore.
    """
    def __init__(self, data_store: DataStore):
        # Inversão de Controle, por Injeção de Dependecia
        self.data_store = data_store

                                                    # Optional pode ou não ter valor
                                                    # depende de uma validação para retornar o valor
    def get_and_validate_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """
        Busca dados de um usuário, valida se está ativo e retorna as informações.

        Args:
            user_id: O ID do usuário.

        Returns:
            Um dicionário com os dados do usuário, ou None se o usuário não for válido.
        """
        user_data = self.data_store.get_user_by_id(user_id)
        if user_data:
            if user_data.get('is_active'):
                logger.info(f"Usuário {user_id} validado com sucesso.")
                return user_data
            else:
                logger.warning(f"Usuário {user_id} encontrado, mas está inativo.")
                return None
        logger.error(f"Usuário {user_id} não encontrado.")
        return None
    
    def create_new_user(self, user_name: str, email: str) -> Dict[str, Any]:
        """Cria um novo usuário e o adiciona ao armazenamento."""
        new_user = {
            "name": user_name,
            "email": email,
            "is_active": True
        }
        return self.data_store.create_user(new_user)

    def delete_existing_user(self, user_id: int) -> bool:
        """Deleta um usuário do armazenamento."""
        return self.data_store.delete_user(user_id)


    # def update_user(self, user_id: int, email: str) -> bool:
        