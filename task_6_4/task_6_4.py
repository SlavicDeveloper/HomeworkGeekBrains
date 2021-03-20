import os
from collections import defaultdict
root_dir = r"C:\Users\User\Desktop\homework_7\task_6_4"
file_list = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_stat = os.stat(file).st_size
        if file_stat < 100:
            file_list[100].append(file)
        elif 100 < file_stat < 1000:
            file_list[1000].append(file)
        elif 1000 < file_stat < 10000:
            file_list[10000].append(file)
        elif file_stat < 10000:
            file_list[100000].append(file)
print(file_list)
