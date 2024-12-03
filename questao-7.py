n = int(input("Digite um número até 100: "))
if n >= 10 and n <= 50:
    print(f"O número {n} está no intervalo de 10 a 50")
elif n < 10:
    print(f"O número {n} está abaixo do intervalo de 10 a 50")
elif n > 50:
    print(f"O número {n} está acima do intervalo de 10 a 50")