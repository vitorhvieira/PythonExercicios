original = [5, 7, 10, 13, 17, 21, 26, 34, 100, 118, 245]
copia = []

for i in original:
    if i >= 10 and i <= 20 or i >= 100:
        copia.append(i)

print(copia)
