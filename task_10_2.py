class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def size_method(self):
        return (self.size)/6.5 + 0.5

    def height_method(self):
        return (self.height) * 2 + 0.3

class Coat(Clothes):
    def size_method(self):
        Clothes.size_method(self)

class Costume(Clothes):
    def height_method(self):
        Clothes.height_method(self)


s = Clothes(12, 156)
print(s.size_method())
print(s.height_method())
