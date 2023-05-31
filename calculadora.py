print("Calculadora")

while True:
    opcao_escolhida = int(input("""
Digite uma opcao abaixo para realizar o calculo desejado:
Digite 1 para Multiplicacao
Digite 2 para Soma
Digite 3 para Divisao
Digite 4 para Subtracao
Digite 5 para Fechar a Calculadora
"""))
    if opcao_escolhida != 5:
        numero_1 = float(input("Digite o primeiro numero que deseja efetuar o calculo:"))

        numero_2 = float(input("Digite o segundo numero que deseja efetuar o calculo:"))
    if opcao_escolhida == 1:
        calculo = numero_1 * numero_2
        print("O resultado da Multiplicacao foi", calculo)
    elif opcao_escolhida == 2:
        calculo = numero_1 + numero_2
        print("O resultado da Soma foi", calculo)  
    elif opcao_escolhida == 3:
        calculo = numero_1 / numero_2
        print("O resultado da Divisao foi", calculo)    
    elif opcao_escolhida == 4:
        calculo = numero_1 - numero_2
        print("O resultado da Subtracao foi", calculo)  
    elif opcao_escolhida == 5:
        print("fim!")
        break        
    else:
        print("opcao invalida!")

