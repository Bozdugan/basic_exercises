# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)



# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f'{name}: {len(name)}')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

people_list = []
for name in names:
    if name in is_male.keys():
        if not is_male.get(name):
            people_list.append(f'{name}: Женский')
        else:
            people_list.append(f'{name}: Мужской')


for people in people_list:
    print(people)




# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

group_num = len(groups)
if group_num == 1:
    print(f'Всего {group_num} группа:')
elif 2 <= group_num <= 4:
    print(f'Всего {group_num} группы:')
elif group_num > 4:
    print(f'Всего {group_num} группы:')
else:
    raise ValueError('Для корректного подсчета количество групп должно быть больше 0')

for group in groups:
    group_size = len(group)
    if group_size == 1:
        print(f'Группа {groups.index(group) + 1}: {group_size} ученик')
    elif 1 < group_size < 5:
        print(f'Группа {groups.index(group) + 1}: {group_size} ученикa')
    elif group_size >= 5:
        print(f'Группа {groups.index(group) + 1}: {group_size} учеников')
    else:
        raise ValueError('Для корректного подсчета количество учеников должно быть больше 0')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

for group in groups:
    group_index = groups.index(group) + 1
    group_content = groups[group_index - 1]
    group_content_correct = ', '.join(group_content)
    print(f'Группа {group_index}: {group_content_correct}')