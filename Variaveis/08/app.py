import math

raio = float(input("Digite o raio do circulo:"))


def calculo(raio):
    comprimento = 2 * math.pi * raio
    area = math.pi * (math.pow(raio, 2))
    return print(f"O comprimento é de {comprimento} e a area é de {area}")


calcular = calculo(raio)
