usuarios = [
    {
        "nome": "João",
        "pets": [],
    },
    {
        "nome": "Ana",
        "pets": ["Pingo", "Lulu"],
    },
    {
        "nome": "Beatriz",
        "pets": ["Lessie"],
    },
    {
        "nome": "Carlos",
        "pets": ["Farofa", "Salsicha", "Batata"],
    },
    {
        "nome": "Antonio",
        "pets": ["Naninha"],
    },
]

for usuario in usuarios:
    if len(usuario["pets"]) == 0:
        print(f"Sou {usuario['nome']} e não tenho pets")
    elif len(usuario["pets"]) == 1:
        print(f"Sou {usuario['nome']} e tenho {len(usuario['pets'])} pet")
    else:
        print(f"Sou {usuario['nome']} e tenho {len(usuario['pets'])} pets")
