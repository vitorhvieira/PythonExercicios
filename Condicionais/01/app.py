jogador1 = input("Jogador 1 Digite a sua jogada (Pedra, Papel ou Tesoura):").lower()
jogador2 = input("Jogador 2 Digite a sua jogada (Pedra, Papel ou Tesoura):").lower()


def jogada(jogador1, jogador2):
    if jogador1 == "pedra" and jogador2 == "tesoura":
        return print("Jogador 1 ganhou")
    elif jogador1 == "tesoura" and jogador2 == "papel":
        return print("Jogador 1 ganhou")
    elif jogador1 == "papel" and jogador2 == "papel":
        return print("Jogador 1 ganhou")
    elif jogador2 == "tesoura" and jogador1 == "papel":
        return print("Jogador 2 ganhou")
    elif jogador2 == "papel" and jogador1 == "papel":
        return print("Jogador 2 ganhou")
    elif jogador2 == "pedra" and jogador1 == "tesoura":
        return print("Jogador 2 ganhou")
    elif jogador1 == jogador2:
        return print("Empate")
    else:
        return print("Digite uma jogada valida")


partida = jogada(jogador1, jogador2)
