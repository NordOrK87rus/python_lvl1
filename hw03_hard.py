# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def calc(expr):
    """
    Сложение или вычитание простых дробей
    :param expr: вычисляемое выражение
    :return: str(результат вычисления)
    """
    def parse_val(v):
        """
        Разбор дроби на числитель и зна=менатель
        :param v: чтрока разибаемой дроби
        :return: list[числитель, знаменатель]
        """
        int_p = None
        if " " in v:
            int_p, v = v.split()
        if "/" in v:
            fract = list(map(int, v.split("/")))
        else:
            fract = [int(v), 1]


        if int_p:
            fract[0] = fract[1] * int(int_p) + fract[0]
        return fract

    def reduce_fraction(n, m):
        """
        Сокращение дроби
        :param n: Числитель
        :param m: Знаменатель
        :return: Сокращённая дробь (если это возможно)
        """
        if n > m:
            k = n
        else:
            k = m
        while k != 1:
            if n % k == 0 and m % k == 0:
                return n // k, m // k
            else:
                k -= 1
        return n, m

    op = "+" if "+" in expr else "-"
    v1_ndx = expr.find(" ", expr.index("/"))
    v1 = parse_val(expr[:v1_ndx])
    v2 = parse_val(expr[expr.index(op, v1_ndx) + 1:].strip())

    if v1[1] != v2[1]:
        v_oz1 = list(map(lambda x: x * v2[1], v1))
        v_oz2 = list(map(lambda x: x * v1[1], v2))
        v1 = v_oz1
        v2 = v_oz2
    res = [eval(f"{v1[0]} {op} {v2[0]}"), v1[1]]

    res = reduce_fraction(res[0], res[1])

    int_part = res[0] // res[1]

    if int_part:
        return f"{int_part} {res[0] - res[1] * int_part}/{res[1]}"
    else:
        return f"{res[0]}/{res[1]}"


expr = input("Введите выражение: ")
print(calc(expr))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def calc_zp(w_data):
    hof_data = None
    hours.seek(0)
    for hof in hours.readlines()[1:]:
        hof_data = hof.strip().split()
        if w_data[0] == hof_data[0] and w_data[1] == hof_data[1]:
            if int(hof_data[2]) < int(w_data[4]):
                w_data[2] = int((int(w_data[2]) / int(w_data[4])) * int(hof_data[2]))
                break
            elif int(hof_data[2]) > int(w_data[4]):
                w_data[2] = int(w_data[2]) + int((int(w_data[2]) / int(w_data[4]) * 2) * (int(hof_data[2]) - int(w_data[4])))
                break
    return hof_data[2], w_data


with open("data/workers", "r") as workers:
    with open("data/hours_of") as hours:
        for w in workers.readlines()[1:]:
            w_zp = calc_zp(w.strip().split())
            print(f"{w_zp[1][0]} {w_zp[1][1]} отработано {w_zp[0]} часов, зарплата {w_zp[1][2]}")



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

with open("data/fruits.txt", 'r') as fruits:
    for f in fruits:
        if len(f.strip()):
            with open(f"data/fruits_{f[0].upper()}", 'a') as fs:
                fs.write(f)
