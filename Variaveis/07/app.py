import math


populacao_inical = int(input("Digite a populacao inicial:"))
qtd_pessoas = int(input("Digite a quantidade de pessoas infectadas:"))
tempo = int(input("Digite o tempo percorrido:"))


def calculo_covid(populacao_inical, qtd_pessoas, tempo):
    calculo = round(populacao_inical * math.pow(qtd_pessoas, tempo/7))
    return print(f'A quantidade final de pessoas infectadas sera de {calculo}')


calculo = calculo_covid(populacao_inical, qtd_pessoas, tempo)
