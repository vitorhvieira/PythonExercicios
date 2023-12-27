ladoA = int(input("Digite o numero:"))
ladoB = int(input("Digite o numero:"))


def domino(ladoA, ladoB):
    if ladoA == ladoB == 0:
        return print("Bucha de Branco")
    elif ladoA == ladoB == 1:
        return print("Bucha de As")
    elif ladoA == ladoB == 2:
        return print("Bucha de Duque")
    elif ladoA == ladoB == 3:
        return print("Bucha de Terno")
    elif ladoA == ladoB == 4:
        return print("Bucha de Quadra")
    elif ladoA == ladoB == 5:
        return print("Bucha de Quina")
    elif ladoA == ladoB == 6:
        return print("Bucha de Sena")
    else:
        return print("SIM")


jogar = domino(ladoA, ladoB)
