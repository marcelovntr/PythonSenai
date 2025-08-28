import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)

def divide_numeros(a: int, b: int) -> float:
    try: 
        # Vai ser executado complementamente ou até termos um erro
        resultado = a / b
        logging.info("A divisão foi bem-sucedida.")
        return resultado
    except ZeroDivisionError:
        # Se a divisão tiver zero no denominador 
        logging.error("Erro: Divisão por zero não é permitida.")
        return 0.0
    except TypeError:
        # Acontece se uma das variáveis não for numero
        logging.error("Erro: Os argumentos devem ser numéricos.")
        return 0.0
    # else:
    #     # Este bloco é executado se nenhuma exceção ocorrer
    #     logging.info("A divisão foi bem-sucedida.")
    #     return resultado
    finally:
        # Este bloco sempre será executado
        logging.info("Função de divisão finalizada.")

print(divide_numeros(10, 2))
print(divide_numeros(10, 0)) # tem que dar erro
# print(divide_numeros(10, "a")) # tem que dar erro

int_ = 10