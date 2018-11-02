# # Задание-1:
# # Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# # Первыми элементами ряда считать цифры 1 1
#
# def fibonacci(n, m):
#     """
#     Возвращает список элементов с n по m из ряда Фибоначчи
#     :param n: номер начального элемента
#     :param m: номер последнего элемента
#     :return: list
#     """
#
#     f_nums = [1, 1]
#
#     while len(f_nums) < m:
#         f_nums.append(f_nums[-2] + f_nums[-1])
#     return f_nums[n-1:m]


# # Задача-2:
# # Напишите функцию, сортирующую принимаемый список по возрастанию.
# # Для сортировки используйте любой алгоритм (например пузырьковый).
# # Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
#
#
# def sort_to_max(origin_list):
#     """
#     Сортировка значений списка по возрастанию
#     :param origin_list: сортируемый список
#     :return: list
#     """
#     sorted_list = []
#     while len(origin_list) > 0:
#         n = min(origin_list)
#         sorted_list.append(n)
#         origin_list.remove(n)
#     return sorted_list
#
#
# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# # Задача-3:
# # Напишите собственную реализацию стандартной функции filter.
# # Разумеется, внутри нельзя использовать саму функцию filter.
#
#
# def my_filter(condition, data):
#     """
#     Фильтрует переданный список по условию
#     :param condition: функция(условие) проверки элементов списка (должна возвращать True или False)
#     :param data: список фильтруемых значений
#     :return: list
#     """
#     filtered_data = []
#     for i in data:
#         if condition(i):
#             filtered_data.append(i)
#     return filtered_data
#
#
# print(my_filter(lambda x: x > 0, [-2, 0, 6, -1, 10]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


from math import sqrt


def is_parallelogram(a, b, c, d):
    """
    Определение, является ли точки вершинами параллерограмма
    :param a, b, c, d: координаты точек в формате (x , y)
    :return: Bool
    """

    def get_l(v1, v2):
        return sqrt((v2[0] - v1[0]) ** 2 + (v2[1] - v1[1]) ** 2)

    # Реализация по условию: AB = DC, AD = BC т.е. противоположные стороны попарно равны
    var1 = get_l(a, b) == get_l(d, c) and get_l(a, d) == get_l(b, c)

    # Реализация по условию: AC**2 + BD**2 = AB**2 + BC**2 + CD**2 + AD**2
    ls_equation = get_l(a, c) ** 2 + get_l(b, d) ** 2
    rs_equation = get_l(a, b) ** 2 + get_l(b, c) ** 2 + get_l(c, d) ** 2 + get_l(a, d) ** 2
    var2 = ls_equation == rs_equation

    return var1 or var2


A1 = (1, 3)
A2 = (4, 7)
A3 = (2, 8)
A4 = (-1, 4)

print(is_parallelogram(A1, A2, A3, A4))

