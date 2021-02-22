for number in range(1000):
    if number % 10 == 1 and number % 100 != 11:
        print(number, "процент")
    elif 1 < number % 10 < 5 and not 11 < number % 100 < 15:
        print(number, "процента")
    else:
        print(number, "процентов")