class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage_n": wage, "bonus_n": bonus}


class Position(Worker):
    def get_full_name(self):
        name_sur = self.name + " " + self.surname + "-" + self.position
        return name_sur
    def get_total_income(self):
        return sum(self._income.values())


a = Position("Петр", "Петров", "сантехник", 4985, 349)
print(a.get_full_name())
print(a.get_total_income())


