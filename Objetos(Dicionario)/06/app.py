usuarios = [
    {
        "nome": "João",
        "idade": 25,
    },
    {
        "nome": "Ana",
        "idade": 18,
    },
    {
        "nome": "Beatriz",
        "idade": 15,
    },
    {
        "nome": "Carlos",
        "idade": 16,
    },
    {
        "nome": "Antonio",
        "idade": 32,
    },
]

jovens = []
adultos = []

for pessoa in usuarios:
    if pessoa["idade"] >= 18:
        adultos.append(pessoa)
    else:
        jovens.append(pessoa)

print(adultos)
print(jovens)
