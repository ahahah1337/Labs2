#Задание 1
value1 = input('Введите первое значение: ')
value2 = input('Введите второе значение: ')

try:
    value1 = int(value1)
    value2 = int(value2)
    print(f'Результат сложения чисел {value1} и {value2}: {value1 + value2}')
except ValueError:
    print(f'Результат конкатенации строк: {value1 + value2}')

#Задание 2
def calculate_cuts(n, piece_increment):
    piece = 1
    cut = 0
    while piece < n:
        cut += 1
        piece += piece_increment
    return cut

n = int(input('Введите количество гостей: '))
print(f'Число разрезов: {calculate_cuts(n, 1)}')

n = int(input('Введите количество гостей: '))
print(f'Число разрезов: {n-1}')

n = int(input('Введите количество гостей: '))
print(f'Число разрезов: {calculate_cuts(n*2, 1)}')

n = int(input('Введите количество гостей: '))
print(f'Число разрезов: {n*2-1}')

n = int(input('Введите количество гостей: '))
print(f'Число разрезов: {calculate_cuts(n+10, 11)}')

#Задание 3
def fibonacci_sequence():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

           n = 0
           generator = fibonacci_sequence()
    while True:
        n += 1
        fibonacci_number = next(generator)
        x = 1 / (5 ** 0.5) * (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n)
        if abs(fibonacci_number - x) > 0.001:
            print(f"Difference occurred at {n}-th number")
        break

#Задание 4
def get_cube_loser(n, m):
    count = 1
    num = 1
    while count <= m:
        m -= count
        count *= 2
        if count > 25:
            count -= 25
            num += 1
        if num > n:
            num = 1
    return num

n, m = int(input("Введите количество детей: ")), int(input("Введите количество кубиков: "))
res = get_cube_loser(n, m)
print(f'Проигравшим будет {res} ребёнок')

#Задание 5

# На основе рекурсии
n = 3
a = []


def move(k, n, x, y, z):
    if n % 2 == 0 and k % 2 == 0 or n % 2 != 0 and k % 2 != 0:
        x, y, z = 1, 2, 3
    else:
        x, y, z = 1, 3, 2

    if k < n:
        for i in range(2 ** k - 1, 2 ** n - 1, 2 ** (k + 1)):
            a[i].append(k + 1)
            a[i].append(x)
            a[i].append(y)
            x, y, z = y, z, x
        move(k + 1, n, x, y, z)


for i in range(2 ** n - 1):
    a.append([])

move(0, n, 1, 2, 3)

for i in range(len(a)):
    print('Диск', a[i][0], ':', a[i][1], '=====>', a[i][2])


# На основе цикла
def move(n, x, y):
    stack = [(n, x, y, 1)]
    while stack:
        n, x, y, step = stack.pop()
        if step == 1:
            if x + y == 3:
                z = 3
            elif x + y == 5:
                z = 1
            else:
                z = 2
            if n == 1:
                print(f'Переместить {n} диск на {y} пирамидку')
            else:
                stack.extend([(n - 1, x, z, 1), (n, x, y, 2), (n - 1, z, y, 1)])
        elif step == 2:
            print(f'Переместить {n} диск на {y} пирамидку')


# n, x, y = int(input("Введите количество дисков: ")), int(input("С какой пирамидки передвинуть(укажите номер пирамидки: 1, 2, 3): ")), int(input("На какую пирамидку передвинуть(укажите номер пирамидки: 1, 2, 3): "))
n, x, y = 3, 1, 2
print('Порядок действий: ')
move(n, x, y)