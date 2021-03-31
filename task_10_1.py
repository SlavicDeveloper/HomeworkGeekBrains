class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(str, self.matrix))

    def __add__(self, other):
        list_of_el = []  # пересоздаем матрицу
        for el_1 in range(len(self.matrix)):
            list_of_el.append([])
            for el_2 in range(len(self.matrix[0])):  # проход по элементам списка (по подспискам как элементам)
                list_of_el[el_1].append(self.matrix[el_1][el_2] + other.matrix[el_1][el_2])
        return "\n".join(map(str, list_of_el))  # повторяем действия


row_1 = [[1, 2, 4], [3, 5, 6]]
row_2 = [[3, 8, 6], [2, 9, 7]]

mat_1 = Matrix(row_1)
mat_2 = Matrix(row_2)
print(mat_1 + mat_2)
