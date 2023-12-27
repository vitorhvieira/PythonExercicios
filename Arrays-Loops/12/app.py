filaDeDentro = ["Jose", "Maria", "Joao"]
filaDeFora = ["Joana", "Roberta", "Marcos", "Felipe"]

while len(filaDeDentro) < 5:
    pessoa = filaDeFora.pop(0)
    filaDeDentro.append(pessoa)

print(filaDeDentro)
print(filaDeFora)
