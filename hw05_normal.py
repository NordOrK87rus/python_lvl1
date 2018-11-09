# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os


def f_help():
    print("\nДоступны следующие команды:")
    for c, d in [('help', 'получение справки'), ('cd', 'перейти в папку'),
                 ('ls', 'вывести содержимое текущей папки'), ('rmd', 'удалить папку'),
                 ('mkd', 'создать папку'), ('exit', 'выход из программы')]:
        print("{0:>5} - {1}".format(c, d))
    print()


def f_ls():
    return os.listdir(os.getcwd())


def f_cd():
    d = input("Введите имя директории для перехода: ")
    d = d.strip()
    if d in f_ls():
        os.chdir(d)
        print(f"Успешно перешел в директорию {d}")
    else:
        print(f"Невозможно перейти в директорию {d}, так как её не существует.")


while True:
    in_cmd = input("Введите команду или help для вывода помощи: ")
    in_cmd = in_cmd.strip()
    if in_cmd == 'exit':
        break
    elif in_cmd == 'help':
        f_help()
    elif in_cmd == 'cd':
        f_cd()
    elif in_cmd == 'ls':
        for i in f_ls():
            print(" ", i)

