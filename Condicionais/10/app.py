import re


caractere = input("Digite o caractere:")


def identificador(caractere):
    vogal_minuscula = re.search("[a-z]", caractere)
    vogal_maiuscula = re.search("[A-Z]", caractere)
    numero = re.search("[0-9]", caractere)

    if vogal_minuscula:
        return print("Vogal minuscula")
    elif vogal_maiuscula:
        return print("Vogal maisucla")
    elif numero:
        return print("Numero")


identificar = identificador(caractere)
