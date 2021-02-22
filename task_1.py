duration = int(input())
hours = duration // 3600
minutes = (duration % 3600) // 60
seconds = (duration % 3600) % 60
print(hours, "ч", minutes, "мин", seconds, "сек")