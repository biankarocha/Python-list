n = int(input("Quantos números você deseja inserir? "))
soma = 0

for i in range(n):
    num = float(input("Digite o número: "))
    soma += num

media = soma / n
print("A média dos números é:", media)