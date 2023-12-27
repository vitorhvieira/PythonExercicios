quantidade_De_Agua_Ingerida = float(
    input("Digite a quantidade de agua ingerida em litro:")
)


def consumo_de_agua(quantidade_De_Agua_Ingerida):
    if quantidade_De_Agua_Ingerida < 1.5:
        return print(
            "Risco Alto - Você está ingerindo pouquissima água, beba mais água!"
        )
    elif quantidade_De_Agua_Ingerida < 3:
        return print("Risco Moderado - Você está ingerindo pouca água, beba mais!")
    else:
        return print(
            "Risco Baixo - Você está ingerindo uma boa quantidade de água, parabéns!"
        )


consumo = consumo_de_agua(quantidade_De_Agua_Ingerida)
