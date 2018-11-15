# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not param:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), param)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(param))
    except FileExistsError:
        print('директория {} уже существует'.format(param))


def ping():
    print("pong")


def cp():
    if not param:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return
    src_fpath = os.path.abspath(param)

    with open(src_fpath, 'r') as s:
        fn, fe = os.path.splitext(os.path.basename(src_fpath))
        copy_num = 1
        while os.path.exists(f"{fn}_copy{copy_num}{fe}"):
            copy_num += 1
        with open(os.path.join(os.path.dirname(s.name), f"{fn}_copy{copy_num}{fe}"), 'w') as d:
            d.write(s.read())
    print(f'копия файла {param} создана с именем {fn}_copy{copy_num}{fe}')


def cd():
    if not param:
        print("Необходимо указать директорию для перехода")
        return
    abs_path = os.path.abspath(param)
    try:
        os.chdir(abs_path)
        print(f"переход в {abs_path} успешно выполнен")
    except FileNotFoundError:
        print(f"невозможно выполнить переход, директория {abs_path} не существует")


def ls():
    print(os.path.abspath(os.getcwd()))


def rm():
    if not param:
        print("Необходимо указать имя удаляемого файла вторым параметром")
        return
    del_fpath = os.path.abspath(param)
    confirm = input(f"Вы действительно хотите удалить {del_fpath}? (y/n): ").strip().lower() == 'y'
    if confirm:
        try:
            os.remove(del_fpath)
            print(f"файл {del_fpath} успешно удалён")
        except FileNotFoundError:
            print(f"файл не существует")
        except PermissionError as e:
            print(f"невозможно удалить {del_fpath} - {e.strerror}")
    else:
        print(f'Удаление {param} отменено пользователем')


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "cd": cd,
    "rm": rm,
    "ls": ls
}

try:
    param = sys.argv[2]
except IndexError:
    param = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
