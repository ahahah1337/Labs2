#Задание 1
def read_numbers_from_input():
    """Считывает вещественные числа, введенные в одной строке, и возвращает их списком."""
    try:
        numbers = input("Введите вещественные числа через пробел: ").strip().split()
        return [float(num) for num in numbers]
    except ValueError:
        print("Некорректный ввод. Убедитесь, что вводите только вещественные числа.")
        return []


def write_numbers_to_file(numbers, filename="numbers.txt"):
    """Записывает каждое число из списка numbers в файл, каждое число на отдельной строке."""
    with open(filename, "a") as file:
        for number in numbers:
            file.write(f"{number}\n")


def read_numbers_from_file(filename="numbers.txt"):
    """Читает числа из файла и возвращает их списком. Если файл не удается прочитать, возвращает пустой список."""
    try:
        with open(filename, "r") as file:
            return [float(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []
    except ValueError:
        print(f"Ошибка при чтении данных из файла '{filename}'.")
        return []


def append_statistics_to_file(numbers, filename="numbers.txt"):
    """Вычисляет сумму, максимум и минимум списка numbers и дописывает их в конец файла."""
    if not numbers:
        return
    total_sum = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    with open(filename, "a") as file:
        file.write(f"Сумма: {total_sum}\n")
        file.write(f"Максимум: {maximum}\n")
        file.write(f"Минимум: {minimum}\n")


def main():
    numbers = read_numbers_from_input()
    if numbers:
        write_numbers_to_file(numbers)

    numbers_from_file = read_numbers_from_file()
    if numbers_from_file:
        append_statistics_to_file(numbers_from_file)


if __name__ == "__main__":
    main()

#Задание 2
def read_input_from_user():
    """Считывает строку, введенную пользователем."""
    return input("Введите строку: ").strip()


def write_input_to_file(input_data, filename="data.txt"):
    """Записывает введенную строку в файл, каждую строку на отдельной строке."""
    with open(filename, "a") as file:
        file.write(f"{input_data}\n")


def read_numbers_from_file(filename="data.txt"):
    """Читает строки из файла и пытается преобразовать их в числа.
       Возвращает список чисел и список нечисловых строк."""
    numbers = []
    non_numbers = []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    non_numbers.append(line.strip())
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    return numbers, non_numbers


def append_statistics_to_file(numbers, filename="data.txt"):
    """Вычисляет сумму, максимум и минимум списка numbers и дописывает их в конец файла."""
    if not numbers:
        return
    total_sum = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    with open(filename, "a") as file:
        file.write(f"Сумма: {total_sum}\n")
        file.write(f"Максимум: {maximum}\n")
        file.write(f"Минимум: {minimum}\n")


def main():
    while True:
        user_input = read_input_from_user()
        if user_input.lower() == "exit":
            break
        write_input_to_file(user_input)

    numbers, _ = read_numbers_from_file()
    append_statistics_to_file(numbers)


if __name__ == "__main__":
    main()

#Задание 3
# Размеры зала
ROWS = 5
COLUMNS = 10

# Инициализация зала: 0 - свободно, 1 - занято
hall = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]


def display_hall(hall):
    """Отображает текущее состояние зала."""
    for row in hall:
        print(' '.join(map(str, row)))
    print()


def count_free_seats(hall):
    """Считает общее количество свободных мест в зале."""
    return sum(row.count(0) for row in hall)


def free_seats_in_row(hall, row):
    """Считает количество свободных мест в указанном ряду."""
    return hall[row].count(0)


def seat_status(hall, row, seat):
    """Проверяет, свободно ли место в указанном ряду и месте."""
    return hall[row][seat] == 0


def main():
    while True:
        print("1. Показать текущее состояние зала")
        print("2. Показать количество свободных мест в зале")
        print("3. Показать количество свободных мест в каждом ряду")
        print("4. Проверить, свободно ли место")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_hall(hall)

        elif choice == "2":
            free_seats = count_free_seats(hall)
            print(f"Количество свободных мест в зале: {free_seats}\n")

        elif choice == "3":
            for row in range(ROWS):
                free_in_row = free_seats_in_row(hall, row)
                print(f"Свободные места в ряду {row + 1}: {free_in_row}")
            print()

        elif choice == "4":
            try:
                row = int(input("Введите номер ряда: ")) - 1
                seat = int(input("Введите номер места: ")) - 1
                if 0 <= row < ROWS and 0 <= seat < COLUMNS:
                    status = "свободно" if seat_status(hall, row, seat) else "занято"
                    print(f"Место {seat + 1} в ряду {row + 1} {status}.\n")
                else:
                    print("Некорректный номер ряда или места.\n")
            except ValueError:
                print("Введите корректные числовые значения.\n")

        elif choice == "5":
            break

        else:
            print("Некорректный выбор. Попробуйте снова.\n")


if __name__ == "__main__":
    main()

#Задание 4
def read_matrix_dimensions(filename):
    """Считывает размеры матрицы из файла."""
    with open(filename, 'r') as file:
        rows = sum(1 for _ in file)
    with open(filename, 'r') as file:
        cols = len(file.readline().strip().split())
    return rows, cols

def get_element(filename, row, col):
    """Получает элемент матрицы из файла по заданным индексу строки и столбца."""
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i == row:
                return float(line.strip().split()[col])
    return None

def write_result_to_file(result, filename="result.txt"):
    """Записывает результат произведения матриц в файл."""
    with open(filename, 'w') as file:
        for row in result:
            file.write(' '.join(map(str, row)) + '\n')

def multiply_matrices(file1, file2, result_file):
    rows1, cols1 = read_matrix_dimensions(file1)
    rows2, cols2 = read_matrix_dimensions(file2)

    if cols1 != rows2:
        raise ValueError("Матрицы нельзя перемножить: число столбцов первой матрицы не равно числу строк второй матрицы.")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            sum_product = 0
            for k in range(cols1):
                element1 = get_element(file1, i, k)
                element2 = get_element(file2, k, j)
                sum_product += element1 * element2
            result[i][j] = sum_product

    write_result_to_file(result, result_file)

def main():
    matrix1_file = "matrix1.txt"
    matrix2_file = "matrix2.txt"
    result_file = "result.txt"

    multiply_matrices(matrix1_file, matrix2_file, result_file)
    print(f"Произведение матриц записано в файл '{result_file}'.")

if __name__ == "__main__":
    main()

#Задание 5
import os

def find_file(filename, search_path):
    """Ищет файл с заданным именем в указанном пути и возвращает абсолютный путь к нему."""
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def main():
    search_path = input("Введите путь для начала поиска (например, C:\\ или /home/username): ")
    filename = "лаба6"

    result = find_file(filename, search_path)

    if result:
        print(f"Файл '{filename}' найден: {result}")
    else:
        print(f"Файл '{filename}' не найден.")

if __name__ == "__main__":
    main()