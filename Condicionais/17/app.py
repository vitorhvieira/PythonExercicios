valor_do_produto = float(input("Digite o valor do produto: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
valor_pago = float(input("Digite o valor pago: "))


def extrato(valor_do_produto, parcelas, valor_pago):
    valor_parcelas = round(valor_do_produto / parcelas)
    parcelas_restantes = round(parcelas - valor_pago / (parcelas * 10))
    return print(f"Restam {parcelas_restantes} de RS{valor_parcelas:.2f}")


produto = extrato(valor_do_produto, parcelas, valor_pago)
