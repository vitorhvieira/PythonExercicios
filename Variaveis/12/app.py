import math

capital = float(input("Digite valor do capital:"))
montante = float(input("Digite o montante:"))
periodo = int(input("Digite o periodo:"))


def calcular_taxa_juros(capital, montante, periodo):
    taxa = math.pow(montante / capital, 1 / periodo) - 1
    return print(f"A taxa de juros sera de {round(taxa * 100, 3)}")


calcular = calcular_taxa_juros(capital, montante, periodo)
