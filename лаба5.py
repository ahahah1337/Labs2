#Задание 1

def transform_string(s):
    Up, Low = 0, 0
    for i in s:
        if i.isupper():
            Up += 1
        else:
            Low += 1

    if Up > Low:
        return s.upper()
    elif Up < Low:
        return s.lower()
    else:
        return s

# s = input('Введите строку: ')
s = "Hello, World!"
transformed_string = transform_string(s)
print(transformed_string)

#Задание 2
def transform_string(s):
    results = []
    indices = [
        [0, 6],
        [4, 6],
        [9, 17],
        [16, 16, 12, 13, 14, 19],
        [4, 7, 5],
        [1, 7, 5],
        [6, 8, 14, 19],
        [18, 15, -1],
        [0, 4, 6, 7]
    ]

    for idx in indices:
        if len(idx) == 2:
            results.append(s[idx[0]:idx[1]])
        elif len(idx) == 1:
            results.append(s[idx[0]])
        else:
            result = ""
            for i in idx:
                result += s[i]
            results.append(result)

    return results

s = "объектно-ориентированный"
transformed_results = transform_string(s)

for result in transformed_results:
    print(result)

#Задание 3
def check_input(input_str):
    new_num = ''
    for i in input_str:
        if i in '123457890':
            new_num += i
    if not new_num:
        return None
    return int(new_num)

num1 = input('Введите первое число: ')
num1 = check_input(num1)
while num1 is None:
    num1 = input('Введите число заново: ')
    num1 = check_input(num1)

num2 = input('Введите второе число: ')
num2 = check_input(num2)
while num2 is None:
    num2 = input('Введите число заново: ')
    num2 = check_input(num2)

print(num1 + num2)

#Задание 4
dictionary = {
    1: 'объект',
    2: 'кто',
    3: 'ориентир',
    4: 'рента',
    5: 'кот',
    6: 'бот',
    7: 'нота',
    8: 'вор',
    9: 'окно',
}

def sort_dict_by_value(d):
    return {v: k for k, v in sorted(d.items(), key=lambda item: item[1])}

print(sort_dict_by_value(dictionary))
#Задание 5
# Исходные данные
school = {
    '1а' : 30,
    '1б' : 31,
    '1в' : 29,
    '1г' : 30,
    '2а' : 29,
    '2б' : 32,
    '2в' : 33,
    '2г' : 30,
    '11а': 9,
}

# Функции для операций с классами
def append_students(dictionary):
    class_name = input('Введите класс, в котором изменилось количество учеников: ')
    num_students = int(input('Сколько теперь учеников в классе? '))
    dictionary[class_name] = num_students
    return dictionary

def append_class(dictionary):
    class_name = input('Введите название нового класса: ')
    num_students = int(input('Введите количество учащихся в этом классе: '))
    dictionary[class_name] = num_students
    return dictionary

def delete_class(dictionary):
    class_name = input('Введите класс, который был расформирован: ')
    students_in_class = dictionary.pop(class_name)
    num_classes = len(dictionary)
    redistributed_students = students_in_class // num_classes
    remaining_students = students_in_class % num_classes

    for class_key in dictionary:
        dictionary[class_key] += redistributed_students
        if remaining_students > 0:
            dictionary[class_key] += 1
            remaining_students -= 1

    return dictionary

def statistic(dictionary):
    total_classes = len(dictionary)
    total_students = sum(dictionary.values())
    return total_classes, total_students, dictionary

# Операции с классами
action = input('Выберите действие:\nа) Изменить количество учащихся\nб) Добавить новый класс\nв) Расформировать класс\nг) Получить статистику\n')

if action == 'а':
    updated_school = append_students(school)
elif action == 'б':
    updated_school = append_class(school)
elif action == 'в':
    updated_school = delete_class(school)
elif action == 'г':
    total_info = statistic(school)
    print(f'Всего классов в школе: {total_info[0]}\nВсего учеников: {total_info[1]}\nРаспределение по классам:')
    for class_name, num_students in total_info[2].items():
        print(f'{class_name}: {num_students}')
else:
    print('Выбрано некорректное действие.')