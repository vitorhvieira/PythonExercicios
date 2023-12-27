letras = ["A", "a", "B", "C", "L", "z", "e", "E"]

quantidade_letras = letras.count("E") + letras.count("e")

if quantidade_letras == 0:
    print("Nenhuma letra 'E' ou 'e' foi encontrada.")
else:
    print(f"Foi encontrada {quantidade_letras} letra 'E' ou 'e'.")
