valor = float(input("Digite o valor da compra: "))
if valor >= 100:
    resultado = (valor * 10) / 100
    print(f"Com desconto a sua compra ficou R$ {valor - resultado}")
else:
    print(f"Não possui desconto abaixo de R$ 100.00")