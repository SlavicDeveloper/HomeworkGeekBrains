from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as f_1:
        f = f.readlines()
        f_1 = f_1.readlines()
        if len(f) > len(f_1):
            diction = {str(key).strip(): str(val).strip() for key, val in zip_longest(f, f_1, fillvalue=None)}
            print(diction)
        else:
            exit(1)



