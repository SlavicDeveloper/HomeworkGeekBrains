prices = [23.41, 45.3, 38.24, 37.01, 29.5, 12.15, 6.46, 32.97, 67.91, 99.09, 90]
for price in prices:
    rub, pen = str(f'{price: 2f}').split(".")
    print(f'{rub} руб {pen:.02s} коп')
print(id(prices))

# task b
prices.sort()
print("Цены по возрастанию с доказательством неизменного объекта: ", *prices, id(prices))  # id совпал

# task c
prices_min = prices[::-1]
print("Цены по убыванию: ", *prices_min)

# task d
highest_prices = prices_min[0:5]
highest_prices.reverse()
print("Самыв большие цены: ", *highest_prices)
