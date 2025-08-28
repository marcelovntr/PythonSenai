"""
Testes de unidade para o serviço de usuário com um armazenamento de dados local.
"""
import pytest
from src.user_service import UserService
from src.data_store import DataStore

# Fixture que cria uma nova instância do DataStore para cada teste.
# Fake do Data
@pytest.fixture
def data_store():
    """Retorna uma nova instância do DataStore para testes."""
    return DataStore()

# Teste 1: Sucesso - Usuário ativo é encontrado
def test_get_and_validate_user_active(data_store):
    """
    Testa se o serviço retorna o usuário corretamente quando ele está ativo.
    """

    # given - setup de dados
    user_service = UserService(data_store)

    # when - ação que está sendo testada
    result = user_service.get_and_validate_user(1)
    
    # then - verificação do resultado
    assert result is not None
    assert result['name'] == "João"
    assert result['is_active'] is True

# Teste 2: Falha - Usuário inativo
def test_get_and_validate_user_inactive(data_store):
    """
    Testa se o serviço retorna None quando o usuário está inativo.
    """
    user_service = UserService(data_store)
    result = user_service.get_and_validate_user(2)

    assert result is None

# Teste 3: Falha - Usuário não existente
def test_get_and_validate_user_not_found(data_store):
    """
    Testa se o serviço retorna None quando o usuário não existe.
    """
    user_service = UserService(data_store)
    result = user_service.get_and_validate_user(999) # ID inexistente
    
    assert result is None

# Teste 4: Sucesso - Criação de novo usuário
def test_create_new_user(data_store):
    """
    Testa se o método de criação de usuário adiciona um novo usuário corretamente.
    """
    user_service = UserService(data_store)
    initial_user_count = len(data_store.get_users())
    
    new_user = user_service.create_new_user("Carlos", "carlos@example.com")
    
    assert new_user is not None
    assert new_user['name'] == "Carlos"
    assert new_user['is_active'] is True
    assert len(data_store.get_users()) == initial_user_count + 1

# Teste 5: Sucesso - Deleção de usuário
def test_delete_existing_user(data_store):
    """
    Testa se o método de deleção remove o usuário corretamente.
    """
    user_service = UserService(data_store)
    initial_user_count = len(data_store.get_users())
    
    # Deleta o usuário com ID 1
    was_deleted = user_service.delete_existing_user(1)
    
    assert was_deleted is True
    assert len(data_store.get_users()) == initial_user_count - 1
    assert data_store.get_user_by_id(1) is None

# Teste 6: Falha - Deleção de usuário não existente
def test_delete_non_existent_user(data_store):
    """
    Testa se o método retorna False ao tentar deletar um usuário que não existe.
    """
    user_service = UserService(data_store)
    initial_user_count = len(data_store.get_users())
    
    was_deleted = user_service.delete_existing_user(999) # ID inexistente
    
    assert was_deleted is False
    assert len(data_store.get_users()) == initial_user_count

# Para rodar os testes, use o comando: pytest