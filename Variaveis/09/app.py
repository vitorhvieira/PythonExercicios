lados = int(input("Digite o numero de lados de um poligono:"))


def soma_dos_angulos(lados):
    soma_angulo = (lados - 2) * 180
    angulo = soma_angulo / lados
    return print(
        f"A soma dos angulos internos é de {soma_angulo} e o valor de cada angulo é {angulo}"
    )


soma = soma_dos_angulos(lados)
