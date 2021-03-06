# -*- coding: utf-8 -*-

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

from math import sqrt
lst = [2, -5, 8, 9, -25, 25, 4]
new_lst = []
for i in lst:
    if i > -1:
        sq = sqrt(i)
        if (sq - int(sq)) == 0:
            new_lst.append(int(sq))
print(new_lst)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

d = "02.11.2013"

# Вариант 1. Со словарями
days_dict = {"01": "первое", "02": "второе", "03": "третье", "04": "четвёртое", "05": "пятое", "06": "шестое",
             "07": "седьмое", "08": "восьмое", "09": "девятое", "10": "десятое", "11": "одиннадцатое",
             "12": "двенадцатое", "13": "тринадцатое", "14": "четырнадцатое", "15": "пятнадцатое", "16": "шестнадцатое",
             "17": "семнадцатое", "18": "восемнадцатое", "19": "девятнадцатое", "20": "двадцатое",
             "21": "двадцать первое", "22": "двадцать второе", "23": "двадцать третье", "24": "двадцать четвёртое",
             "25": "двадцать пятое", "26": "двадцать шестое", "27": "двадцать седьмое", "28": "двадцать восьмое",
             "29": "двадцать девятое", "30": "тридцатое", "31": "тридцать первое"}

month_dict = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня",
              "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}

print("{dd} {mm} {yyyy} года".format(dd=days_dict[d[:2]], mm=month_dict[d[3:5]], yyyy=d[-4:]))

# Вариант 2. Со списками
days_list = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
             'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
             'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе',
             'двадцать третье', 'двадцать четвёртое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое',
             'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']

month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
              'ноября', 'декабря']

print("{dd} {mm} {yyyy} года".format(dd=days_list[int(d[:2])-1], mm=month_list[int(d[3:5])-1], yyyy=d[-4:]))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

from random import randint
n = int(input("Введите желаемое количество элементов списка: "))
i = 0
lst = []
while i < n:
    lst.append(randint(-100, 100))
    i += 1
print(lst)

# Оптимальнее было бы реализовать счётчик через range()


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]

# а)
lst2 = list(set(lst))
print(lst2)

# б)
# Вариант 1: С иcпользованием цикла
lst2 = []
for i in lst:
    if lst.count(i) == 1:
        lst2.append(i)
print(lst2)

# Вариант 2: Inline реализация варианта 1
lst2 = [i for i in lst if lst.count(i) == 1]
print(lst2)

