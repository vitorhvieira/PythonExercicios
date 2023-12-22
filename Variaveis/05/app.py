import math


x1 = float(input("Digite o ponto x1:"))
x2 = float(input("Digite o ponto x2:"))
y1 = float(input("Digite o ponto y1:"))
y2 = float(input("Digite o ponto y2:"))


def calcular_distancia(x1, x2, y1, y2):
    distancia = math.sqrt(math.exp2(x2 - x1) + math.exp2(y2 - y1))
    return print(f"A distancia entres dois pontos é {distancia}")


distancia = calcular_distancia(x1, x2, y1, y2)
