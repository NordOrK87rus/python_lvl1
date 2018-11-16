#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Card(object):
    def __init__(self, player_card=False):
        self.title = "------ Ваша карточка -----" if player_card else "-- Карточка компьютера ---"
        self.num_card = ()

        # Генерируем смписок уникальных случайных чисел
        num_array = random.sample(range(1, 91), k=15)
        self.all_nums = num_array.copy()

        # Заполняем карточку
        for _ in range(3):
            self.num_card += (sorted(random.sample(num_array, k=5)),)
            num_array = list(set(num_array) - set(self.num_card[-1]))

            # Расставляем пустые клетки
            for i in random.sample(range(9), k=4):
                self.num_card[-1].insert(i, None)

    def __str__(self):
        """
        Перезагружаем метод __str__ для реализации вывода карточки в читаемом виде:

        ------ Ваша карточка -----
         6  7          49    57 58
        14 26     -    78    85
        23 33    38    48    71
        --------------------------

        """
        data = ""
        for l in self.num_card:
            for i in l:
                data += "{0:^3}".format(i if i else " ")
            data += "\n"
        return f"{self.title}\n{data}{'-'*26}"

    def __sub__(self, other):
        """
        Перезагружаем метод __sub__ (вычитание), реализуем функционал зачоркивания числа в карте
        :param other: число, которое требуется зачеркнуть
        """
        row = self.find_number(other)
        if row:
            row[row.index(other)] = "-"
            self.all_nums.remove(other)
            return True
        else:
            return False

    @property
    def remain_numbers(self):
        """
        Возвращает количество оставшихся не зачоркнутыми чисел.
        """
        return len(self.all_nums)

    def find_number(self, value):
        """
        Ищет в карточке строку, в которой имеется нужное число.
        Если находит, возвращает эту строку, если не находит, возвращает None
        :param value: искомое число
        """
        for l in self.num_card:
            if value in l:
                return l
        else:
            return None


def barrels():
    """
    "Мешок с бочонками", возвращает номер случайно выбранного бочонка
    """
    nums = list(range(1, 91))
    random.shuffle(nums)
    b_count = len(nums)
    for b in nums:
        b_count -= 1
        yield b, b_count


# ------------ Игра ------------ :
barrel = barrels()
p_card = Card(True)
c_card = Card()


while True:
    new_b, remain = next(barrel)
    c_card - new_b
    print(f"\n\nНовый бочонок: {new_b} (осталось {remain})")
    print(p_card)
    print(c_card)

    while True:
        answer = input("Зачеркнуть цифру? (y/n): ")
        if answer.lower() == 'y':
            result = (p_card - new_b,)
            break
        elif answer.lower() == 'n':
            rn = p_card.find_number(new_b)
            result = not rn, rn
            break
        else:
            print("Вы ввели неверное значение, допустимы ответы \"y\" или \"n\". Попробуйте ещё раз.")
    if not result[0]:
        print("-----\nВы проиграли!")
        if answer.lower() == 'y':
            print(f"В вашей карте нет числа \"{new_b}\".")
        else:
            print(f"В вашей карте имеется число \"{new_b}\" (строка {p_card.num_card.index(result[1])+1}, "
                  f"колонка {result[1].index(new_b)+1})")
        print("-----")
        break
    else:
        if p_card.remain_numbers == 0 and c_card.remain_numbers == 0:
            print("\nУ вас дружеская ничья, так как Вы и компьютер одновременно зачеркнули последнее число в своих "
                  "карточках!")
            print(p_card)
            print(c_card)
        elif p_card.remain_numbers == 0:
            print("\nПоздравляем! Вы выиграли!")
            print(p_card)
            print(c_card)
            break
        elif c_card.remain_numbers == 0:
            print("\nК сожалению Вы проиграли, так как компьютер раньше зачеркнул все числа в своей карте.")
            print(p_card)
            print(c_card)
        else:
            print("Продолжаем игру...")




