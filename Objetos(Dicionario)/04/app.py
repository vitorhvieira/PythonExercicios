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

for usuario in usuarios:
    usuario["maior_idade"] = usuario["idade"] > 17

print(usuarios)
