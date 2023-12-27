ladoA = int(input("Digite o numero:"))
ladoB = int(input("Digite o numero:"))


def domino(ladoA, ladoB):
    if ladoA == ladoB:
        return print("Não")
    else:
        return print("Sim")


jogar = domino(ladoA, ladoB)
