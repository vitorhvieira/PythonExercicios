import math


a = int(input("Digite o coeficiente a:"))
b = int(input("Digite o coeficiente b:"))
c = int(input("Digite o coeficiente c:"))


def delta(a, b, c):
    delta = math.pow(a, 2) - 4 * b * c
    return print(f"O valor de Delta é de {delta}")


calcular = delta(a, b, c)
