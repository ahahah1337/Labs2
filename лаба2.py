#1
n=int('Введите четырёхзначное число:')
while len(n)<4:
    n='0'+n


if n[:2]==n[2:][::-1]:
    print(1)

else:
    print(100)
#2
year = int(input("Введите число: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Год високосный")
else:
    print("Не високосный")

#3
number = int(input('Введите число: '))

# Определение правильной формы слова "корова" в зависимости от числа
if 4 < number % 100 < 21 or number % 10 == 0 or 4 < number % 10 < 10:
    print(f'На лугу пасётся {number} коров')
elif number % 10 == 1:
    print(f'На лугу пасётся {number} корова')
else:
    print(f'На лугу пасётся {number} коровы')
#4

num = int(input('Введите число: '))

# Поиск наименьшего натурального делителя через цикл for
print('\n---------------------Цикл for---------------------')
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print('Наименьший натуральный делитель: ', i)
        break
else:
    print('Простое число')

# Поиск наименьшего натурального делителя через цикл while
print('\n---------------------Цикл while---------------------')
i = 2
while i <= int(num**0.5):
    if num % i == 0:
        print('Наименьший натуральный делитель: ', i)
        break
    i += 1
else:
    print('Простое число')

