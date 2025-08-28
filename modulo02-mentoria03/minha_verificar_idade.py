def verificar_idade():
    idade = int(input('Digite sua idade para verificação:'))
    if idade < 18:
        return "unless youve got a fake id... get home!"
    elif idade >= 18 and idade < 65:
        return "Permitida a entrada, beba com moderação!"
    elif idade > 65 and idade < 111:
        return "enjoy the night, grandpa!"
    # elif idade < 0 and idade > 111:
    #     return 'idade inválida'
    else:
        return 'idade inválida'