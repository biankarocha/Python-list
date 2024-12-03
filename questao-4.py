idade = int(input("Digite sua idade: "))
if idade <= 12:
    print(f"Você é criança")
elif idade >=13 and idade < 17:
    print(f"Você é adolescente")
elif idade >= 18:
    print(f"Você é uma pessoa adulta")