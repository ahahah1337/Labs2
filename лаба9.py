#Задание 1
import numpy as np
import matplotlib.pyplot as plt

class Figure:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

class Circle(Figure):
    def __init__(self, center_x, center_y, radius):
        super().__init__(center_x, center_y)
        self.radius = radius
        self.area = np.pi * self.radius**2
        self.circumference = 2 * np.pi * self.radius

class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def vertices(self):
        return [self.x1, self.x2, self.x3, self.x1], [self.y1, self.y2, self.y3, self.y1]

class Rectangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.x4, self.y4 = x4, y4

    def vertices(self):
        return [self.x1, self.x2, self.x3, self.x4, self.x1], [self.y1, self.y2, self.y3, self.y4, self.y1]

def draw_circle(circle):
    fig, ax = plt.subplots()
    circle_plot = plt.Circle((circle.center_x, circle.center_y), circle.radius, color='blue', fill=False)
    ax.add_artist(circle_plot)
    ax.set_xlim(circle.center_x - circle.radius - 1, circle.center_x + circle.radius + 1)
    ax.set_ylim(circle.center_y - circle.radius - 1, circle.center_y + circle.radius + 1)
    ax.set_aspect('equal', 'box')
    plt.show()

def draw_polygon(vertices):
    plt.plot(vertices[0], vertices[1])
    plt.show()

print('Выберите цифру рисунка:\n1) Треугольник\n2) Круг\n3) Прямоугольник')
choice = input()

if choice == '1':
    triangle1 = Triangle(0, 0, 1, 1, 2, 0)
    draw_polygon(triangle1.vertices())
elif choice == '2':
    circle1 = Circle(0, 0, 2)
    draw_circle(circle1)
elif choice == '3':
    rectangle1 = Rectangle(0, 0, 0, 1, 2, 1, 2, 0)
    draw_polygon(rectangle1.vertices())
else:
    print('Данная операция отсутствует')

#Задание 2
import numpy as np

class Matrix:
    def __init__(self, data: list[list[int]]):
        self.data = np.array(data)

    def __str__(self):
        result = ''
        for row in self.data:
            result += '\t'.join(map(str, row)) + '\n'
        return result.strip()

    def size(self) -> tuple[int, int]:
        return self.data.shape

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.size() != other.size():
            raise ValueError("Размеры матриц не совпадают")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix(self.data * other)
        elif isinstance(other, Matrix):
            if self.data.shape[1] != other.data.shape[0]:
                raise ValueError("Матрицы нельзя умножить")
            return Matrix(np.dot(self.data, other.data))
        else:
            raise TypeError("Неверный тип для умножения")

    __rmul__ = __mul__

    def transpose(self) -> 'Matrix':
        return Matrix(self.data.T)

#Задание 3
import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __str__(self):
        result = ''
        for row in self.data:
            result += '\t'.join(map(str, row)) + '\n'
        return result.strip()

    def size(self):
        return self.data.shape

    def __add__(self, other):
        if self.size() != other.size():
            raise ValueError("Размеры матриц не совпадают")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix(self.data * other)
        elif isinstance(other, Matrix):
            if self.data.shape[1] != other.data.shape[0]:
                raise ValueError("Матрицы нельзя умножить")
            return Matrix(np.dot(self.data, other.data))
        else:
            raise TypeError("Неверный тип для умножения")

    __rmul__ = __mul__

    def transpose(self):
        return Matrix(self.data.T)

class Vector(Matrix):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        super().__init__([end - start for start, end in zip(self.start_point, self.end_point)])

    def __add__(self, other):
        result_matrix = super().__add__(other)
        if result_matrix is None:
            return None
        return Vector(self.start_point, result_matrix.data[0])

    def __sub__(self, other):
        return Vector(self.start_point, [end - diff for end, diff in zip(self.end_point, other.data[0])])

    def __mul__(self, other):
        if isinstance(other, Vector):
            other = other.transpose()
        result_matrix = super().__mul__(other)
        if result_matrix.size() == (1, 1):
            return result_matrix.data[0, 0]
        return result_matrix.data

    __rmul__ = __mul__

    def length(self):
        return np.linalg.norm(self.data[0])

    def cosine(self, other):
        return (self * other) / (self.length() * other.length())

    def about(self):
        print(f'Вектор №{id(self)}:')
        print(f'\tКоординаты вектора: {self.data}')
        print(f'\tКоординаты начальной точки: {self.start_point}')
        print(f'\tКоординаты конечной точки: {self.end_point}')
        print(f'\tДлина вектора: {self.length()}')

    def cross_product(self, other):
        if len(self.data[0]) not in {2, 3}:
            raise ValueError("Вектор должен быть размерностью 2 или 3 для векторного произведения")
        return Vector([0, 0, 0], np.cross(self.data[0], other.data[0]))

#Задание 4