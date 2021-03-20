import os

settings = []
i = 1
settings_amount = int(input("Введите число необходимых настроек: "))
while i <= settings_amount:
    settings.append(input())
    i += 1
for el in settings:
    project_tree = os.path.join("my_project", el)
    if not os.path.exists(project_tree):
        os.makedirs(project_tree)


