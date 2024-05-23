#Задание 1
class First:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def write_num(self):
        print(f'Первое число: {self.num1}, второе число: {self.num2}')

    def redact(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def summa(self):
        return self.num1 + self.num2

    def max_number(self):
        if self.num1 > self.num2:
            return '>'
        elif self.num1 < self.num2:
            return '<'
        else:
            return '='

def main():
    obj = First(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
    obj.write_num()
    print(f'{obj.num1} + {obj.num2} = {obj.summa()}')
    print(f'{obj.num1} {obj.max_number()} {obj.num2}')

    while input('Вы хотите изменить числа? (Yes/No): ').strip().lower() == 'yes':
        obj.redact(int(input('Введите первое изменённое число: ')), int(input('Введите второе изменённое число: ')))
        obj.write_num()
        print(f'{obj.num1} + {obj.num2} = {obj.summa()}')
        print(f'{obj.num1} {obj.max_number()} {obj.num2}')

if __name__ == '__main__':
    main()

#Здание 2
class Polynomial:
    def __init__(self, *terms: int):
        self._terms = terms

    def __str__(self):
        if not self._terms:
            return "0"
        out = []
        for p, term in enumerate(self._terms):
            if term == 0:
                continue
            sign = " + " if term > 0 else " - "
            term_str = f"{abs(term)}" if abs(term) != 1 or p == 0 else ""
            variable_str = "x" if p > 0 else ""
            exponent_str = f"^{p}" if p > 1 else ""
            out.append(f"{term_str}{variable_str}{exponent_str}")
        result = sign.join(out).strip()
        return result if result[0] != "+" else result[2:]

    def __mul__(self, other: 'Polynomial'):
        result_terms = [0] * (len(self._terms) + len(other._terms) - 1)
        for i, term1 in enumerate(self._terms):
            for j, term2 in enumerate(other._terms):
                result_terms[i + j] += term1 * term2
        return Polynomial(*result_terms)

#Задание 3
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3D):  # Scalar (dot) product
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:  # Scalar multiplication
            return Vector3D(self.x * other, self.y * other, self.z * other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def cos_angle(self, other):
        return (self * other) / (abs(self) * abs(other))

#Задание 4
class Train:
    def __init__(self, departure, destination, departure_time, arrival_time):
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __add__(self, other):
        if self.destination == other.departure and self.arrival_time < other.departure_time:
            new_departure = self.departure
            new_destination = other.destination
            new_departure_time = self.departure_time
            new_arrival_time = other.arrival_time
            return Train(new_departure, new_destination, new_departure_time, new_arrival_time)
        else:
            return None

    def __str__(self):
        return (f"Train from {self.departure} to {self.destination}, "
                f"departing at {self.departure_time}, arriving at {self.arrival_time}")

# Примеры использования
train1 = Train("Москва", "Санкт-Петербург", "10:00", "14:00")
train2 = Train("Санкт-Петербург", "Москва", "15:00", "19:00")

combined_train = train1 + train2

if combined_train:
    print(f"Поезда ({train1}) и ({train2}) могут быть объединены.")
    print(f"Объединённый поезд: {combined_train}")
else:
    print("Поезда не могут быть объединены.")