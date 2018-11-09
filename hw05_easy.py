from os import mkdir, rmdir, getcwd, path as os_path, listdir as os_listdir
from sys import argv
from re import compile


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.



def make_dir(dir_name):
    """
    Функция создающая директорию
    :param dir_name: абсолютный путь к создаваемой директории
    """
    try:
        mkdir(dir_name)
        print(f"Директория {dir_name} создана успешно.")
    except FileExistsError:
        print(f"Директория {dir_name} уже существует!")


def del_dir(dir_name):
    """
    Функция удаляющая указанную директорию
    :param dir_name: абсолютный путь к удаляемлй директории
    """
    try:
        rmdir(dir_name)
        print(f"Директория {dir_name} удалена успешно.")
    except FileNotFoundError:
        print(f"Директория {dir_name} не найдена!")


print("Задача-1: Создание директорий:")
for i in range(9):
    make_dir(os_path.join(os_path.dirname(argv[0]), f"dir_{i+1}"))

print("\nЗадача-1: Удаление директорий:")
regex = compile(r'dir_\d')
for i in filter(regex.match, os_listdir(os_path.dirname(argv[0]))):
    del_dir(os_path.abspath(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print("\nЗадача-2: Вывод папок текущей директории:")
print(f"Текущая директория: \"{getcwd()}\"содержит следующие папки:\n ", "\n ".join(filter(os_path.isdir,
                                                                                           os_listdir(getcwd()))))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print("\nЗадача-3: Создание копии файла, из которого запущен данный скрипт: ")
with open(argv[0], 'r') as s:
    # Разбираем имя файла скрипта на имя и расширение, для дальнейшего формирования нового имени
    fn, fe = os_path.splitext(os_path.basename(s.name))
    print(f"{os_path.basename(s.name)} -> {fn}_copy{fe}")
    # Создаём копию файла скрипта
    with open(os_path.join(os_path.dirname(s.name), f"{fn}_copy{fe}"), 'w') as d:
        d.write(s.read())

