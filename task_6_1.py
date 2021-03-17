with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    list_of_lines = []
    for line in f:
        lines = (line.split()[0], line.split()[5][1:4], line.split()[6][:22])
        list_of_lines.append(lines)

print(list_of_lines, type(list_of_lines))

