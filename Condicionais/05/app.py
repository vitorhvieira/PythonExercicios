candidato = float(input("Digite a altura do jogador:"))


def peneira(candidato):
    if candidato >= 180:
        return print("APROVADO")
    else:
        return print("REPROVADO")


jogador = peneira(candidato)
