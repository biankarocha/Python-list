num = int(input("Digite um número inteiro: "))
div = 2
primo = True

while div < num:
    if num % div == 0:
        primo = False
        break
    div += 1

if primo:
    print(num, "é um número primo.")
else:
    print(num, "não é um número primo.")