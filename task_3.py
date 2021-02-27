new_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
name_list=[]
for elements in new_list:
    nametag_reversed = elements[::-1]
    name_reversed = nametag_reversed[:nametag_reversed.index(" ")]
    normal_name = name_reversed[::-1]
    normal_name_1 = normal_name.lower()  # to lower case
    normal_name_2 = normal_name_1.capitalize()  # to upper case first letter
    name_list.append(normal_name_2)
for names in name_list:
    print("Привет, " + names + "!")

# или

for elements in new_list:
    print(f"Привет, {elements.split()[-1].title()}!")
