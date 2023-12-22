peso = float(input("Digite o peso:"))
altura = float(input("Digite a altura:"))


def calculadora_IMC(peso, altura):
    imc = round(peso / altura**2, 1)
    return print(f"Seu IMC é de {imc}")


calcular = calculadora_IMC(peso, altura)
