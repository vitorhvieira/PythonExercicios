nota = float(input("Qual o valor da nota?:"))


def boletim(nota):
    if nota < 4:
        return print(" O estudando obteve conceito E")
    elif nota < 5.9:
        return print(" O estudando obteve conceito D")
    elif nota < 7.9:
        return print(" O estudando obteve conceito C")
    elif nota < 8.9:
        return print(" O estudando obteve conceito B")
    else:
        return print(" O estudando obteve conceito A")


aluno = boletim(nota)
