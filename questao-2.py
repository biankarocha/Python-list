n1 = int(input(f"Digite o primeiro número: "))
n2 = int(input(f"Digite o segundo número: "))
operacao = input("utilize uma das operações a seguir: (+ ,- ,* , /) ")
if operacao == '+':
  resultado = n1 + n2
elif operacao == '-':
  resultado = n1 - n2
elif operacao == '*':
  resultado = n1 * n2
elif operacao == '/':
  resultado = n1 / n2
print(f"{n1} {operacao} {n2} = {resultado}")