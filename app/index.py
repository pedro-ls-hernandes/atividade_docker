def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = num1 + num2
        operador = '+'
    elif escolha == '2':
        resultado = num1 - num2
        operador = '-'
    elif escolha == '3':
        resultado = num1 * num2
        operador = '*'
    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            operador = '/'
        else:
            print("Erro! Divisão por zero.")
            return
    else:
        print("Opção inválida.")
        return

    print(f"{num1} {operador} {num2} = {resultado}")

calculadora()