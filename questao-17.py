num = 1
positivos = 0

while num != 0:
    num = int(input("Digite um número (0 para sair): "))
    if num > 0:
        positivos += 1

print("Quantidade de números positivos:", positivos)