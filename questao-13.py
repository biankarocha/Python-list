n = int(input("Digite um número: "))
tabuada = input("Digite a qual tabuada você quer: [+, -, *, /]: ")
for i in range(1, 11):
    if tabuada == '+':
        resultado = n + i
    elif tabuada == '-':
        resultado = n - i
    elif tabuada == '*':
        resultado = n * i
    elif tabuada == '/':
        resultado = n / i if i != 0 else "indefinido"
    else:
        print("Operador inválido. Tente novamente com +, -, * ou /.")
    break
    print(f"{n} {tabuada} {i} = {resultado:.1f}")