nota = float(input("Digite sua nota: "))
if nota >= 5 and nota <= 6.9:
    print(f"Você está de Recuperação com {nota}")
elif nota < 5:
    print(f"Você está de Reprovado com {nota}")
elif nota >= 7:
    print(f"Você está de Aprovado com {nota}")