raio_base = int(input("Digite o radio da base:"))
altura_cilindro = int(input("Digite a altura do cilindro:"))


def area_total(raio_base, altura_cilindro):
    area = 2 * raio_base * (raio_base + altura_cilindro)
    return print(f"A Area total do cilindro é {area}pi")


area = area_total(raio_base, altura_cilindro)
