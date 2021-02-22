row_of_numbers = list(range(1, 1000, 2)) # list added
third_degree = []
new_third_degree = []
sum_of_elements = 0
for degree in row_of_numbers:
    third_degree.append(degree ** 3)

for indx, elements in enumerate(third_degree):
    sum_of_digits = 0
    while elements != 0:
        unit = elements % 10
        sum_of_digits = sum_of_digits + unit
        elements = elements // 10
    if sum_of_digits % 7 == 0:
        sum_of_elements += third_degree[indx]
print(sum_of_elements)

sum_of_elements = 0
for degree_1 in third_degree:
    new_third_degree.append(degree_1 + 17)
for indx, elements in enumerate(new_third_degree):
    sum_of_digits = 0
    while elements != 0:
        unit = elements % 10
        sum_of_digits = sum_of_digits + unit
        elements = elements // 10
    if sum_of_digits % 7 == 0:
        sum_of_elements += new_third_degree[indx]
print(sum_of_elements)