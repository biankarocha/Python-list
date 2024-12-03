n1 = int(input(f"Digite o primeiro número: "))
n2 = int(input(f"Digite o segundo número: "))
if n1 > n2:
    print(f"O número {n1} é maior que {n2}")
elif n1 < n2:
    print(f"O número {n2} é maior que {n1}")
else:
    print(f"O número {n1} é {n2} são iguais")