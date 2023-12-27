tipo_de_pagamento = input(
    "Tipo de pagamento? (dinheiro, credito, debito, cheque): "
).lower()
valor_do_produto = float(input("Valor do produto: "))


def desconto(tipo_de_pagamento, valor_do_produto):
    desconto = 0
    if tipo_de_pagamento == "dinheiro" or tipo_de_pagamento == "debito":
        desconto = 0.10
    elif tipo_de_pagamento == "cheque":
        desconto = 0.03
    elif tipo_de_pagamento == "credito":
        desconto = 0.05

    valor_final = valor_do_produto - (valor_do_produto * desconto)
    return print(f"Valor a ser pago:R${valor_final:.2f}")


pagar = desconto(tipo_de_pagamento, valor_do_produto)
