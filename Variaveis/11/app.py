import math

raio = int(input("Digite o valor do raio da esfera:"))


def volume_esfera(raio):
    volume = round(((4 / 3) * (math.pow(raio, 3))) * math.pi, 1)
    return print(f"O volume da esfera é de {volume}")


calcular = volume_esfera(raio)
