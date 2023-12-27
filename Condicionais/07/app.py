portadora_De_Doenca = input("Possui alguma doença grave?:").lower()
aposentado = input("Ja é aposentado(a)?:").lower()
total_De_Rendimentos = float(input("Qual o total de rendimento?:"))


def imposto(portadora_De_Doenca, aposentado, total_De_Rendimentos):
    if portadora_De_Doenca == "sim":
        portadora_De_Doenca = True
    elif portadora_De_Doenca == "nao":
        portadora_De_Doenca = False

    if aposentado == "sim":
        portadora_De_Doenca = True
    elif aposentado == "nao":
        portadora_De_Doenca = False

    if total_De_Rendimentos <= 2855970:
        total_De_Rendimentos = True
    else:
        total_De_Rendimentos = False

    if portadora_De_Doenca and aposentado and total_De_Rendimentos:
        return print("ISENTA")
    elif portadora_De_Doenca and aposentado and not total_De_Rendimentos:
        return print("VAZA LEAO! JA TA DIFICIL SEM VOCE")
    elif portadora_De_Doenca and not aposentado and total_De_Rendimentos:
        return print("ISENTA")
    elif not portadora_De_Doenca and aposentado and total_De_Rendimentos:
        return print("ISENTA")
    else:
        return print("PEGA LEAO")


verificar = imposto(portadora_De_Doenca, aposentado, total_De_Rendimentos)
