#Задание 1
def find_sequence(pi_digits, sequence):
    """Find the first occurrence of a sequence in the pi_digits."""
    seq_len = len(sequence)
    for i in range(len(pi_digits) - seq_len + 1):
        if pi_digits[i:i + seq_len] == sequence:
            return (i, i + seq_len - 1)
    return None


def main():
    with open("pi-10million.txt") as f:
        pi_digits = f.readline().strip()

    sequences_to_find = {
        'six 9s': '999999',
        'six 8s': '888888',
        'six 0s': '000000',
        '141592': '141592',
        '8993927': '8993927'
    }

    for name, seq in sequences_to_find.items():
        result = find_sequence(pi_digits, seq)
        if result:
            print(f"The sequence '{seq}' ({name}) was found at positions {result}")
        else:
            print(f"The sequence '{seq}' ({name}) was not found in the first 10 million digits of pi.")


if __name__ == "__main__":
    main()

#Задание 2
from timeit import default_timer

def read_pi_digits(filename):
    """Чтение первых 100 символов из файла с числом Пи."""
    with open(filename) as f:
        return f.read(100)

def binary_search(numbers, target):
    """Бинарный поиск в отсортированном массиве."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def golden_section_search(numbers, key):
    """Метод золотого сечения."""
    phi = (1 + 5 ** 0.5) / 2
    a = 0
    b = len(numbers) - 1

    while b - a >= 1:
        x1 = int(b - (b - a) / phi)
        x2 = int(a + (b - a) / phi)
        A = numbers[a:x2 + 1]
        B = numbers[x1:b + 1]

        if key in A:
            b = x2
        elif key in B:
            a = x1
        else:
            return None
    return a

def interpolating_search(arr, x):
    """
    Интерполяционный поиск элемента в отсортированном массиве.

    :param arr: Отсортированный массив.
    :param x: Искомое число.
    :return: Индекс искомого числа в массиве, или None, если число не найдено.
    """
    l = 0
    u = len(arr) - 1

    while l <= u:
        i = l + ((u - l) * (x - arr[l]) // (arr[u] - arr[l]))

        if x == arr[i]:
            return i
        elif x < arr[i]:
            u = i - 1
        else:
            l = i + 1

# Чтение первых 100 символов числа Пи
fs = read_pi_digits("pi-10million.txt")

# Создание отсортированного массива для поиска
LS = sorted([int(i) for i in range(1, 10000000)])

# Поиск с использованием бинарного поиска
t = default_timer()
print(binary_search(LS, 9999999))
print("Время выполнения бинарного поиска: {:.10f}".format(default_timer() - t))

# Поиск с использованием метода золотого сечения
t = default_timer()
print(golden_section_search(LS, 9999999))
print("Время выполнения метода золотого сечения: {:.10f}".format(default_timer() - t))

# Поиск с использованием интерполяционного поиска
t = default_timer()
print(interpolating_search(LS, 9999999))
print("Время выполнения интерполяционного поиска: {:.10f}".format(default_timer() - t))

#Задание 3
from timeit import default_timer

def binary_search(numbers, num):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if num == numbers[mid]:
            return mid
        elif num < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1  # Возвращаем -1, если число не найдено

def golden_cut_search(arr, key):
    phi = 0.5*(1 + 5 ** 0.5)
    a = 0
    b = len(arr) - 1
    while b - a >= 1:
        x1 = int(b - (b - a)/phi)
        x2 = int(a + (b - a)/phi)
        if arr[x1] == key:
            return x1
        elif arr[x2] == key:
            return x2
        elif key < arr[x1]:
            b = x1
        elif key > arr[x2]:
            a = x2
        else:
            a = x1
            b = x2
    return -1  # Возвращаем -1, если число не найдено

def interpolating_search(arr, x):
    l = 0
    u = len(arr) - 1

    while l <= u and arr[l] <= x <= arr[u]:
        i = l + ((u - l) * (x - arr[l]) // (arr[u] - arr[l]))

        if x == arr[i]:
            return i
        elif x < arr[i]:
            u = i - 1
        else:
            l = i + 1
    return -1  # Возвращаем -1, если число не найдено

# Загружаем данные из файла
with open("pi-10million.txt", "r") as f:
    numbers = sorted(map(int, f.readline().split()))

print('=====Бинарный поиск=====')
t = default_timer()
print(binary_search(numbers, 9999999))
print('{:.10f}'.format(default_timer() - t))

print('=====Поиск по золотому сечению=====')
t = default_timer()
print(golden_cut_search(numbers, 9999999))
print('{:.10f}'.format(default_timer() - t))

print('=====Интерполирующий поиск=====')
t = default_timer()
print(interpolating_search(numbers, 9999999))
print('{:.10f}'.format(default_timer() - t))

#Дополнительное задание 1
def heapify(arr, n, i):
    """Преобразует поддерево с корнем в узле i в кучу, n - размер кучи"""
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # левый = 2*i + 1
    right = 2 * i + 2  # правый = 2*i + 2

    # Если левый дочерний элемент больше корня
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем местами

        # Рекурсивно преобразуем в кучу затронутое поддерево
        heapify(arr, n, largest)

def heap_sort(arr):
    """Основная функция для сортировки массива заданного размера"""
    n = len(arr)

    # Построение кучи (перегруппируем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # перемещаем текущий корень в конец
        heapify(arr, i, 0)

# Пример использования:
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Исходный массив:", arr)
    heap_sort(arr)
    print("Отсортированный массив:", arr)

#Дополнительное задание 2
import requests

def download_data(url, filename):
    """Скачивает файл с заданного URL и сохраняет его локально."""
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def parse_line(line):
    """Парсит строку из файла и возвращает словарь с данными о малом теле."""
    return {
        'number': line[0:7].strip(),
        'name': line[175:193].strip(),
        'absolute_magnitude': float(line[8:13].strip()),
        'slope_parameter': float(line[14:19].strip()),
        'epoch': line[20:25].strip(),
        'mean_anomaly': float(line[26:35].strip()),
        'arg_perihelion': float(line[37:46].strip()),
        'asc_node': float(line[48:57].strip()),
        'inclination': float(line[59:68].strip()),
        'eccentricity': float(line[70:79].strip()),
        'mean_daily_motion': float(line[80:91].strip()),
        'semi_major_axis': float(line[92:103].strip()),
        'reference': line[194:202].strip(),
        'other': line[203:209].strip()
    }

def read_data(filename):
    """Считывает данные из файла и возвращает список словарей."""
    data = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Пропуск пустых строк
                data.append(parse_line(line))
    return data

def sort_by_name(data):
    """Сортирует данные по имени малого тела."""
    return sorted(data, key=lambda x: x['name'])

def binary_search(data, target):
    """Ищет малое тело по имени в отсортированном массиве с использованием бинарного поиска."""
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid]['name'] == target:
            return data[mid]
        elif data[mid]['name'] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def linear_search(data, target, key):
    """Ищет малое тело в неотсортированном массиве по заданному ключу."""
    for item in data:
        if item[key] == target:
            return item
    return None

def main():
    # Скачиваем данные
    url = "https://www.minorplanetcenter.net/iau/MPCORB/MPCORB.DAT"
    filename = "MPCORB.DAT"
    download_data(url, filename)

    # Читаем данные
    data = read_data(filename)
    print(f"Прочитано {len(data)} записей.")

    # Сортируем данные
    sorted_data = sort_by_name(data)

    # Пример использования бинарного поиска
    target_name = "Ceres"
    result = binary_search(sorted_data, target_name)
    if result:
        print(f"Найдено: {result}")
    else:
        print(f"Малое тело с именем '{target_name}' не найдено.")

    # Пример использования линейного поиска
    target_number = "000001"
    result = linear_search(data, target_number, 'number')
    if result:
        print(f"Найдено: {result}")
    else:
        print(f"Малое тело с номером '{target_number}' не найдено.")

if __name__ == "__main__":
    main()


