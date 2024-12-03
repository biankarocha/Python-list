numero = int(input("Digite um numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"O {numero} é divisível por 3 e 5 ao mesmo tempo")
else:
    print(f"O {numero} não é divisível por 3 e 5 ao mesmo tempo")
