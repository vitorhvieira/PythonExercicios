capital = float(input("Digite valor do capital:"))
taxa = float(input("Digite a taxa:"))
periodo = int(input("Digite o periodo:"))


def calcular_juros_compostos(capital, taxa, periodo):
    montante = round(capital * ((1 + taxa) ** periodo), 2)
    return print(f"O valor do montante sera de {montante}")


calcular = calcular_juros_compostos(capital, taxa, periodo)
