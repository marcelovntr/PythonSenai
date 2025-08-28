def main():
    try:
        num_primeiro = int(input('Digite um número: '))
        num_segundo = int(input('Digite o segundo número para realizar operações: '))
        print(f"Soma: {num_primeiro + num_segundo}")
        print(f"Subtração: {num_primeiro - num_segundo}")
        print(f"Multiplicação: {num_primeiro * num_segundo}")
        print(f"Divisão: {num_primeiro / num_segundo}")

    # except ZeroDivisionError:
    #     print("Erro: Não é possível dividir por zero!")
    except Exception as e:
        print(f"Erro: {e}")
       

if __name__ == "__main__":
    main()