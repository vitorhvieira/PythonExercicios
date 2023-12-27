idade = int(input("Qual a sua idade?:"))
patologia_cardiaca = input("Possui alguma patologia cardiaca?:")
altura = float(input("Qual a sua altura?:"))
estudante = input("Voce é estudante?:").lower()


def montanha_russa(idade, patologia_cardiaca, altura, estudante):
    if 12 > idade or idade > 65:
        return print("ACESSO NEGADO caso a pessoa não possa brincar")

    if patologia_cardiaca == "sim":
        return print("ACESSO NEGADO caso a pessoa não possa brincar")

    if altura < 150:
        return print("ACESSO NEGADO caso a pessoa não possa brincar")

    if estudante == "sim" or idade < 18:
        return print(
            "10 reais caso esse seja o valor que a pessoa deve pagar para brincar"
        )
    else:
        return print(
            "20 reais caso esse seja o valor que a pessoa deve pagar para brincar"
        )


permitido = montanha_russa(idade, patologia_cardiaca, altura, estudante)
