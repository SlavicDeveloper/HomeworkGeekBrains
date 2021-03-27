class Road:
    def __init__(self, _length, _width, _mass):
        self._length = _length
        self._width = _width
        self._mass = _mass

    def mass_asp(self):
        return self._length * self._width * self._mass

answer = Road(100, 200, 21)
print(answer.mass_asp())
