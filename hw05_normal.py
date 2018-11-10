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

from os import getcwd, chdir, path as os_path, listdir as os_listdir
from sys import argv
from hw05_easy import del_dir, make_dir, list_of_folders

print(f"sys.argv = {argv}\n")

cmd_list = [(1, 'Перейти в папку'),
            (2, 'Просмотреть содержимое текущей папки'),
            (3, 'Удалить папку'),
            (4, 'Создать папку')]


def do_cmd(cmd):
    """
    Обработка команд пользователя
    :param cmd: введённая пользователем команда
    """
    if cmd == "1":
        d = input(" -> Введите имя папки для перехода: ")
        d = d.strip()
        if d in list_of_folders() or d == os_path.pardir:
            chdir(d)
            print(f" -> Успешно перешел в папку {d}")
        else:
            print(f" -> Невозможно перейти в папку {d}, так как её не существует.")
    elif cmd == "2":
        for i in os_listdir(getcwd()):
            print(" ", i)
    elif cmd == "3":
        d = input(" -> Введите имя папки для удаления: ")
        d = d.strip()
        del_dir(d.strip())
    elif cmd == "4":
        d = input(" -> Введите имя создаваемой папки: ")
        d = d.strip()
        make_dir(d.strip())
    else:
        print(f"Команда \"{cmd}\" недопустима.")


if len(argv) > 1:
    # Выполняет команду переданную аргументом при запуске утилиты
    do_cmd(argv[1].strip())
else:
    # Если небыло передано аргументов, то утилита просит пользователя ввести команду
    # и будет выполняться пока пользователь не ведёт exit
    print(f"\nВыберите действие:")
    for n, d in cmd_list:
        print("{0}. {1}".format(n, d))

    in_cmd = input(f":> ")
    do_cmd(in_cmd.strip())