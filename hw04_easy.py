# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

src_lst = [1, 2, 4, 0]
res_lst = [x**2 for x in src_lst]
print(f"Task1:\n source: {src_lst}\n result: {res_lst}\n\n")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst1 = ['apple', 'peach', 'pineapple', 'banana']
lst2 = ['pomelo', 'banana', 'mango', 'apple']
lst3 = [f for f in lst1 if f in lst2]
print(f"Task2:\n list1: {lst1}\n list2: {lst2}\n result: {lst3}\n\n")


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst_d = [1, 87, 90, -26, 85, 18, -70, -47, -45, 56, 120]
lst_r = [i for i in lst_d if i > 0 and i % 3 == 0 and i % 4 != 0]
print(f"Task3:\n source: {lst_d}\n result: {lst_r}\n")