candidato = float(input("Digite a altura do jogador:"))


def peneira(candidato):
    if candidato < 180:
        return print("REPROVADO")
    elif candidato <= 185:
        return print("LÍBERO")
    elif candidato <= 195:
        return print("PONTEIRO")
    elif candidato <= 205:
        return print("OPOSTO")
    else:
        return print("CENTRAL")


jogador = peneira(candidato)
