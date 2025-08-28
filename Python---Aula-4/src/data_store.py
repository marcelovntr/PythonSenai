"""
Simulação de um armazenamento de dados local.
Responsabilidade Única: Gerenciar a lista de usuários em memória.
"""
from typing import List, Dict, Any

class DataStore:
    """
    Classe para interagir com o armazenamento de dados local.
    """

    def __init__(self):
        # Inicializa a lista de usuários como atributo de instância
        # Protegido
        self._users_data: List[Dict[str, Any]] = [
            {"id": 1, "name": "João", "is_active": True, "email": "joao@example.com"},
            {"id": 2, "name": "Maria", "is_active": False, "email": "maria@example.com"},
            {"id": 3, "name": "Carlos", "is_active": True, "email": "carlos@example.com"},
            {"id": 4, "name": "Ana", "is_active": True, "email": "ana@example.com"}
        ]
        # item privado/private
        self.__users_data2: List[Dict[str, Any]] = []

    def get_users(self) -> List[Dict[str, Any]]:
        """Retorna todos os usuários na lista."""
        return self._users_data

    def get_user_by_id(self, user_id: int) -> Dict[str, Any] | None:
        """Busca um usuário por ID na lista."""
        for user in self._users_data:
            if user['id'] == user_id:
                return user
        return None

    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Adiciona um novo usuário à lista."""
        new_id = len(self._users_data) + 1
        user_data['id'] = new_id
        self._users_data.append(user_data)
        return user_data

    def delete_user(self, user_id: int) -> bool:
        """Deleta um usuário da lista por ID."""
        user = self.get_user_by_id(user_id)
        if user:
            self._users_data.remove(user)
            return True
        return False
