def thesaurus(*args):
    names = {}
    for elements in args:
        first_letter = elements[0:1]
        if first_letter in names:
            names[first_letter] = [first_letter] + [elements]
        else:
            names[first_letter] = [elements]
    return names

print(thesaurus("Иван", "Мария", "Петр", "Илья"))




