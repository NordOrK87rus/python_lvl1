# -*- coding: utf-8 -*-

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

# Вариант 1.
f_body = equation[equation.find('=')+2:]
y = float(f_body[:f_body.find('x')]) * x + float(f_body[f_body.find('+')+2:])
print(y)

# Вариант 2.
f_body = equation.partition('=')[2]
y = eval(f_body.replace('x', '* %f' % x))
print(y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

day, month, year = date.split('.')
if len(day) != 2 or len(month) != 2 or len(year) != 4:
    print("Дата не соответсвует формату: dd.mm.yyyy")
else:
    day, month, year = int(day), int(month), int(year)
    days_in_month = 30 if month in [2, 4, 6, 9, 11] else 31
    if 1 > year or year > 9999:
        print("Год находится вне диапазона допустимых значений. Допускается от 1 до 9999!")
    elif 1 > month or month > 12:
        print("Месяц находится вне диапазона допустимых значений. Допускается от 1 до 12!")
    elif 1 > day or day > days_in_month:
        print("День находится вне диапазона допустимых значений. Допускается от 1 до %d!" % days_in_month)
    else:
        print("Дата \'{0}\' полностью соответсвует требованиям.".format(date))

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

n = 13

last_room = 1
below_floors = 0
rooms_on_floor = 1
while last_room < 2000000000:
    rooms = [i for i in range(last_room, last_room+(rooms_on_floor**2))]
    if n in rooms:
        r_ndx = rooms.index(n)
        floor = r_ndx // rooms_on_floor + below_floors + 1
        r_pos = r_ndx % rooms_on_floor + 1
        print(floor, r_pos)
        break
    else:
        below_floors += len(rooms) // rooms_on_floor
        rooms_on_floor += 1
        last_room = rooms[-1]+1


