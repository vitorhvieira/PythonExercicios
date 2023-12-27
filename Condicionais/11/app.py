renda_mensal = float(input("Qual sua renda mensal?: "))
meses_decorrido = int(input("Quantos meses decorridos??: "))
total_pago = float(input("Qual o valor total pago?: "))


def parcela(renda_mensal, meses_decorrido, total_pago):
    parcelas = 0

    if renda_mensal > 20000:
        parcelas = renda_mensal * 0.18 / 100
    else:
        return print(
            "O valor da parcela desse mês é R$ 0 reais. Nenhum valor é devido pois a renda do estudante está abaixo do valor mínimo de R$ 2000 reais."
        )

    if meses_decorrido > 60:
        return print("Valor quitado depois de 60 meses")

    if total_pago >= 1800000:
        return print("Valor total pago. Divida quitada!")


aluno = parcela(renda_mensal, meses_decorrido, total_pago)
