fahrenheit = int(input("Digite a temperatura em Fahrenheit:"))


def temperatura_em_celcius(fahrenheit):
    celcius = round((fahrenheit - 32) * 5 / 9)
    return print(f"A temeperatura {fahrenheit} em Celcius é {celcius}")


converter = temperatura_em_celcius(fahrenheit)
