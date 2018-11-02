# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    """
    Округление до требуемого количества знаков
    :param number: округляемое число
    :param ndigits: количество знаков
    :return: float
    """
    m = 10 ** ndigits
    return int(number * m + 0.5) / m


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    """
    Проверяет равенство сумм первых и последних цифр числа
    :param ticket_number: проверяемое число
    :return: Bool
    """
    sum1 = sum2 = 0
    s_tn = str(ticket_number)
    h_num = len(s_tn) // 2

    for i, c in enumerate(s_tn):
        if i < h_num:
            sum1 += int(c)
        else:
            sum2 += int(c)
    return sum1 == sum2


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
