valor_do_tenis = float(input("Digite o valor do tenis desejado:"))
dinheiro = float(input("Digite a quantidade de dinheiro que possui:"))


def desconto_necessario(valor_do_tenis, dinheiro):
    calcular_diferenca = (valor_do_tenis - dinheiro) / valor_do_tenis
    calcular_desconto = round(calcular_diferenca * 100, 2)
    return print(
        f"O desconto necessario para comprar o tenis é de {calcular_desconto}%"
    )


desconto = desconto_necessario(110, 50)
