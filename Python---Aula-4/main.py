"""
Ponto de entrada do programa.
"""
import logging
from src.user_service import UserService
from src.data_store import DataStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# É boa pratica começar o código dentro do __name__ == "__main__"
if __name__ == "__main__":
    # Instancia o DataStore e o UserService
    data_store = DataStore()
    user_service = UserService(data_store) # Injetar uma dependencia
    

    # Ao alterar o atributo privado com __, o nome do atributo é modificado internamente.
    # Isso é conhecido como name mangling.
    data_store._DataStore__users_data2.__getitem__(0)

    user_service.get_and_validate_user()


    # Demonstração 1: Buscar um usuário que existe (o ID 1)
    logger.info("\n--- Buscando e validando o usuário com ID 1 ---")
    user_id = 1
    user = user_service.get_and_validate_user(user_id)
    if user:
        logger.info(f"Dados do usuário {user_id}: {user}")
    else:
        logger.warning(f"Usuário {user_id} não pôde ser validado.")
        
    # Demonstração 2: Buscar um usuário que não existe (o ID 999)
    logger.info("\n--- Buscando e validando o usuário com ID 999 ---")
    user_id_inexistente = 999
    user_inexistente = user_service.get_and_validate_user(user_id_inexistente)
    if user_inexistente:
        logger.info(f"Dados do usuário {user_id_inexistente}: {user_inexistente}")
    else:
        logger.warning(f"Usuário {user_id_inexistente} não pôde ser validado.")

    # Demonstração 3: Criar um novo usuário
    logger.info("\n--- Criando um novo usuário: Ana ---")
    new_user = user_service.create_new_user("Ana", "ana@example.com")
    logger.info(f"Novo usuário criado com sucesso: {new_user}")
    
    # Demonstração 4: Buscar o novo usuário
    logger.info(f"\n--- Buscando o novo usuário (ID {new_user['id']}) ---")
    retrieved_user = user_service.get_and_validate_user(new_user['id'])
    if retrieved_user:
        logger.info(f"Novo usuário encontrado e validado: {retrieved_user}")
    
    # Demonstração 5: Deletar um usuário
    logger.info("\n--- Deletando o usuário com ID 1 ---")
    was_deleted = user_service.delete_existing_user(1)
    if was_deleted:
        logger.info("Usuário com ID 1 deletado com sucesso.")
    
    # Demonstração 6: Tentar buscar o usuário deletado
    logger.info("\n--- Tentando buscar o usuário com ID 1 novamente ---")
    deleted_user = user_service.get_and_validate_user(1)
    if deleted_user is None:
        logger.info("Usuário com ID 1 não encontrado, conforme o esperado.")
