def verificar_estacao():
    mes = int(input("Digite o número do mês (1-12): "))

    match mes:
        case 12 | 1 | 2:
            return"verão"
        case 3 | 4 | 5:
            return"outono"
        case 6 | 7 | 8:
            return"inverno"
        case 9 | 10 | 11:
            return"primavera"
        case _:
            return "Mês inválido!"