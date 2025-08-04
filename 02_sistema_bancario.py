menu = '''
    ========================
        [1] Sacar
        [2] Depositar
        [3] Mostrar extrato
        [4] Sair
    ========================
        '''
saldo = 0
limite = 2300
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 5

while True:

    opcao = input(menu)
    if opcao == '1':
        saque = float(input("Digite o valor de saque: "))

        saldo_insuficiente = saque > saldo
        limite_atingido = saldo > limite
        saques_insuficiente = numero_saques >= LIMITE_SAQUE

        if saldo_insuficiente:
            print("Saldo insuficiente, por favor tente novamente")
        elif saques_insuficiente:
            print("Limite de saques atingido, por favor retorne em outro momento")
        elif limite_atingido:
            print("Limite de saldo atingido, por favor saque seu dinheiro ou solicite aumento de limite")
        elif saldo > 0:
            saldo -= saque
            extrato += f"saque: {saque}\n"
            numero_saques += 1
        else:
            print("Operação falhou tente novamente")



    elif opcao == '2':
        deposito = float(input("Digite o valor de depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"deposito: {deposito:.2f}\n"

    elif opcao == '3':
        print("======extrato======")
        print("Nenhuma transição realizada ainda." if not extrato else extrato)
        print(f"Saldo: {saldo:.2f}")
        print("===================")

    elif opcao == '4':
        break

    else:
        print("Digite uma opção válida")














