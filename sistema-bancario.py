menu = '''
    =======================
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
     
    =======================     
        '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        deposito = float(input('Digite o valor do depósito: '))

        if deposito > 0:
                saldo += deposito
                extrato += f"Depósito : {deposito}\n"

        else:
            print("Operação falhou! o valor informado é ivalido.")



    elif opcao == '2':
        saque = float(input('Digite o valor do saque: '))

        excedeu_saldo = saque > saldo
        excedeu_limite = saldo > limite
        excedeu_saques = numero_saques >=LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! número máximo de saqueas excedido.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque : R$ {saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == '3':
        print("\n=========Extrato=======")
        print("Não forem realizados movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================")

    elif opcao == '4':
        break

    else:
        print("Operação inválida, por favor digite a operação desejada.")



