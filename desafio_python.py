## 3 saques diários no máximo 500,00 por saque

## se não tiver saldo "saldo insuficiente"

## não pode depositar -100 reais

## extrato deve aparecer todos os depósitos e saques realizados

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("-------> Depósito <-------")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
        else:
            print("Operação inválida! O valor digitado não é positivo.")

    elif opcao == "s":
        print("-------> Saque <-------")
        valor_saque = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Conta com saldo insuficiente.")
        elif excedeu_limite:
            print("O valor limite é de R$500,00 por saque.")
        elif excedeu_saques:
            print("Não é possível fazer saque, limite excedido.")
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R${valor_saque:.2f}\n"
        else:
            print("Operação inválida! O valor digitado não é positivo.")


    elif opcao == "e":
        print("-------> Extrato <-------")
        print("Não existem movimentações na conta selecionada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------> Fim do extrato <-------")

    elif opcao == "q":
        break

    else:
        print("Opcaração inválida, selecione uma opção existente.")