valor_saque = int(input("Digite o valor do saque: "))
cedulas = [50, 20, 10, 1]
total_cedulas = 0

for cedula in cedulas:
    quantidade_cedulas = valor_saque // cedula
    valor_saque %= cedula
    if quantidade_cedulas > 0:
        print(f"{quantidade_cedulas} cédulas de R${cedula}")
        total_cedulas += quantidade_cedulas

print(f"Total de cédulas: {total_cedulas}")