src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = set()
repeat_nums = set()
for el in src:
   if not el in repeat_nums:
      result.add(el)
   else:
      result.discard(el)
   repeat_nums.add(el)

unique_num = [el for el in src if el in result]
print(unique_num)