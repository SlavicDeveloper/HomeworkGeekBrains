with open("bakery.csv", "r", encoding="utf-8") as f:
    el_1 = int(input("С какого элемента начать чтение: "))
    el_2 = int(input("На каком элементе закончить прочтение: "))
    content = f.read()
    prices = content.splitlines()
    print(*prices[el_1:el_2])

