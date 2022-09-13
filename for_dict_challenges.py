# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_list = []

for i in students:
    name_list.append(i.get('first_name'))

name_count_list = set(name_list)

for name in name_count_list:
    name_num = name_list.count(name)
    print(f'{name}: {name_num}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_list = []

for i in students:
    name_list.append(i.get('first_name'))

name_num = Counter(name_list).most_common()

most_common_name = name_num[0][0]
print(f'Самое частое имя среди учеников: {most_common_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

common_class_list = []

for raw_class in school_students:
    class_list = []
    for name in raw_class:
        class_list.append(name.get('first_name'))
    common_class_list.append(class_list)


for fine_class in common_class_list:
    name_num = Counter(fine_class).most_common()
    most_common_name = name_num[0][0]
    print(f'Самое частое имя в классе {common_class_list.index(fine_class) + 1} : {most_common_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ВОТ ПО ЭТОЙ ЗАДАЧЕ ОСОБЕННО ВАЖНА ОБРАТНАЯ СВЯЗЬ.
# НАВЕРНЯКА ЕСТЬ БОЛЕЕ ИЗЯЩНОЕ РЕШЕНИЕ ПРИ ПОМОЩИ КАКОЙ-НИБУДЬ БИБЛИОТЕКИ, НО Я НЕ НАШЕЛ.
people_list_2a = []
people_list_2b = []


a = school[0].get('students')
b1 = school[1].get('students')
b2 = school[2].get('students')
for raw_name in a:
    people_list_2a.append(*raw_name.values())
for raw_name in b1:
    people_list_2b.append(*raw_name.values())
for raw_name in b2:
    people_list_2b.append(*raw_name.values())

class_2a_girls = 0
class_2a_boys = 0
class_2b_girls = 0
class_2b_boys = 0
for name in people_list_2a:
    if name in is_male.keys():
        if not is_male.get(name):
            class_2a_girls += 1
        else:
            class_2a_boys += 1

for name in people_list_2b:
    if name in is_male.keys():
        if not is_male.get(name):
            class_2b_girls += 1
        else:
            class_2b_boys += 1

print(f'Класс 2A: девочки {class_2a_girls}, мальчики {class_2a_boys}\n'
      f'Класс 2Б: девочки {class_2b_girls}, мальчики {class_2b_boys}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

people_list_2a = []
people_list_3c = []


a = school[0].get('students')
c = school[1].get('students')

for raw_name in a:
    people_list_2a.append(*raw_name.values())
for raw_name in c:
    people_list_3c.append(*raw_name.values())

class_2a_girls = 0
class_2a_boys = 0
class_3c_girls = 0
class_3c_boys = 0
for name in people_list_2a:
    if name in is_male.keys():
        if not is_male.get(name):
            class_2a_girls += 1
        else:
            class_2a_boys += 1

for name in people_list_3c:
    if name in is_male.keys():
        if not is_male.get(name):
            class_3c_girls += 1
        else:
            class_3c_boys += 1


def girl_status_check():
    if class_2a_girls > class_3c_girls:
        return 'Больше всего девочек в классе 2a'
    else:
        return 'Больше всего девочек в классе 3c'


def boys_status_check():
    if class_2a_boys > class_3c_boys:
        return 'Больше всего мальчиков в классе 2a'
    else:
        return 'Больше всего мальчиков в классе 3c'


print(boys_status_check())
print(girl_status_check())

