jogada1 = input("Jogador 1 escolha (par ou impar)").lower()
jogada2 = input("Jogador 2 escolha (par ou impar)").lower()


def jogada(jogada1, jogada2):
    if jogada1 == jogada2:
        return print("Escolha opções diferentes")

    numero1 = int(input("Jogador 1 digite o numero para a jogada:"))
    numero2 = int(input("Jogador 2 digite o numero para a jogada:"))

    calculo = abs(numero1 % numero2)

    if calculo == 0 and jogada1 == "par":
        return print("Jogador 1 venceu!")
    elif calculo == 0 and jogada2 == "par":
        return print("Jogador 2 venceu!")
    elif calculo == 1 and jogada1 == "impar":
        return print("Jogador 1 venceu!")
    elif calculo == 1 and jogada2 == "impar":
        return print("Jogador 2 venceu!")


jogar = jogada(jogada1, jogada2)
