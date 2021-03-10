src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[i] if src[i] > src[i - 1] else print('') for i in range(1, len(src))]
set_result = set(result)
set_result.remove(None)
new_result_list = list(set_result)
print(new_result_list)
