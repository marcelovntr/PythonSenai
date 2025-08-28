def calcular_imc():
    peso_inserido = float(input('Insira seu peso:'))
    altura_inserida = float(input('Insira agora sua altura em metros:'))
    imc = peso_inserido/(altura_inserida**2)
    
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Baixo Peso"
    elif imc > 18.5 and imc < 25:
        return f"IMC: {imc:.2f} - Eutrofia"
    elif imc > 25 and imc < 30:
        return f"IMC: {imc:.2f} - Sobrepeso"
    else:
        return f"IMC: {imc:.2f} - Obesidade"