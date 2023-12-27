dia = int(input("Digite o numero correspondente ao dia da semana:"))


def semana(dia):
    if dia == 1:
        return print("Domingo")
    elif dia == 2:
        return print("Segunda")
    elif dia == 3:
        return print("Terça Feira")
    elif dia == 4:
        return print("Quarta Feira")
    elif dia == 5:
        return print("Quinta Feira")
    elif dia == 6:
        return print("Sexta Feira")
    elif dia == 7:
        return print("Sabado")
    else:
        return print("O dia da semana informado não é válido.")


dias = semana(dia)
