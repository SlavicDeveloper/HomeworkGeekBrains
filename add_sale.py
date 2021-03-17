txt = []
i = 1
points = int(input("Введите число единиц продукции: "))
with open('bakery.csv', 'w', encoding='utf-8') as f:
    while i <= points:
        txt.append(input() + "\n")
        i += 1
    f.writelines(txt)



