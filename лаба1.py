#Базовое Задание 1

x = 2
print(x, type(x))
x += 3
print(x, type(x))
x = 0.5 * (x+1)
print(x, type(x))
x += 0.5
print(x, type(x))
x = x < 5
print(x, type(x))
x = str(x)
print(x, type(x))

#Базовое Задание 2

x = 0
for i in range(1, 6):
    x += i
sr = x/5
print(f"Среднее значение этих 5 чисел равно: {format(sr, '.5f')}")
#Базовое Задание 3
total_sum = 0  # Общая сумма чисел
number_count = 5  # Начальное количество чисел
while True:
    average = total_sum / number_count  # Вычисление среднего значения
    print(f"Среднее значение этих {number_count} чисел равно: {format(average, '.5f')}")
    print("Введите число для добавления или 0 для остановки:")
    new_number = float(input())  # Ввод нового числа
    if new_number == 0:
        break  # Прерывание цикла при вводе 0
    total_sum += new_number  # Обновление общей суммы
    number_count += 1  # Увеличение количества чисел
