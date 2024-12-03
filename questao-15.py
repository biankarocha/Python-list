n = int(input("Digite um numero: "))
soma = 0
for i in range (1 , n + 1):
    if i % 2 == 0:
        soma += i
    print(f"A soma de 1 a {n} é = {soma}")