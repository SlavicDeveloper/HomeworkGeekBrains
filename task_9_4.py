class Stationery:
    def __init__(self, title):
        self.title = title

class Pen(Stationery):
    def draw(self):
        print("Карандаш")

class Pencil(Stationery):
    def draw(self):
        print("Ручка")

class Handle(Stationery):
    def draw(self):
        print("Маркер")

pen = Pen("Канцелярские принадлежности")
pen.draw()
pencil = Pencil("Канцелярские принадлежности")
pencil.draw()
handle = Handle("Канцелярские принадлежности")
handle.draw()
