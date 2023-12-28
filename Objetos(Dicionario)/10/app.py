patricia = {"nome": "Patricia", "carrinho": []}
carlos = {"nome": "Carlos", "carrinho": []}
renato = {"nome": "Renato", "carrinho": []}
jose = {"nome": "José", "carrinho": []}
roberto = {"nome": "Roberto", "carrinho": []}

tv = {"nome": "TV Samsung 4K", "valorEmCentavos": 129900}
notebook = {"nome": "Notebook Dell", "valorEmCentavos": 399990}
mouse = {"nome": "Mouse MX Master 3", "valorEmCentavos": 23000}
teclado = {"nome": "Teclado Keychron K8", "valorEmCentavos": 50000}
caboUsb = {"nome": "Cabo USB 2 Metros", "valorEmCentavos": 1990}
carregador = {"nome": "Carregador portátil", "valorEmCentavos": 4590}
webcam = {"nome": "Webcam C920s", "valorEmCentavos": 80000}
monitor = {"nome": "Monitor LG 29 FHD", "valorEmCentavos": 129900}


jose["carrinho"].append({"item": tv, "quantidade": 1})
jose["carrinho"].append({"item": caboUsb, "quantidade": 2})
jose["carrinho"].append({"item": webcam, "quantidade": 1})

carlos["carrinho"].append({"item": notebook, "quantidade": 2})

patricia["carrinho"].append({"item": teclado, "quantidade": 1})
patricia["carrinho"].append({"item": caboUsb, "quantidade": 2})
patricia["carrinho"].append({"item": carregador, "quantidade": 1})
patricia["carrinho"].append({"item": mouse, "quantidade": 1})
patricia["carrinho"].append({"item": monitor, "quantidade": 1})

renato["carrinho"].append({"item": webcam, "quantidade": 5})

roberto["carrinho"].append({"item": webcam, "quantidade": 1})
roberto["carrinho"].append({"item": caboUsb, "quantidade": 2})
roberto["carrinho"].append({"item": monitor, "quantidade": 1})

print(jose["carrinho"])
print(carlos["carrinho"])
print(patricia["carrinho"])
print(renato["carrinho"])
print(roberto["carrinho"])
