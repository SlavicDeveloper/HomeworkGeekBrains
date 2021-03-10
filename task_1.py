def odd_nums_gen(max_num):
    max_num = int(max_num)
    for el in range(1, max_num + 1, 2):
        yield el

odd_nums = odd_nums_gen(input())
print(*odd_nums)




