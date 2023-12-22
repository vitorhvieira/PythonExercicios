distancia_Percorrida = float(input("Digite a distancia percorrida em metros:"))
tempo = float(input("Digite o tempo percorrido em segundos:"))


def velocidade_media(distancia_Percorrida, tempo):
    velocidade = (distancia_Percorrida / tempo) * 3.6
    return print(f"A veolocidade media foi de {velocidade}km/h")


velocidade = velocidade_media(distancia_Percorrida, tempo)
