# # Задание-1:
# # Вывести символы в нижнем регистре, которые находятся вокруг
# # 1 или более символов в верхнем регистре.
# # Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# # Решить задачу двумя способами: с помощью re и без.
#
# line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
#        'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
#        'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
#        'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
#        'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
#        'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
#        'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
#        'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
#        'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
#        'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
#        'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
#        'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
#        'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
#        'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
#        'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
#
# # Решение с помощью re:
# import re
# t1_lst_re = re.findall(r'[a-z]+', line)
# print(f"Задание-1: Решение с помощью re: {t1_lst_re}")
#
# # Решение с без re:
# t1_lst_loop = ['']
# for i in line:
#     if i.islower():
#         t1_lst_loop[-1] += i
#     else:
#         if t1_lst_loop[-1] != '':
#             t1_lst_loop.append('')
# else:
#     if t1_lst_loop[-1] == '':
#         t1_lst_loop.pop()
# print(f"Задание-1: Решение с помощью цикла: {t1_lst_loop}\n")
#
# # Задание-2:
# # Вывести символы в верхнем регистре, слева от которых находятся
# # два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# # Т.е. из строки
# # "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# # нужно получить список строк: ['AY', 'NOGI', 'P']
# # Решить задачу двумя способами: с помощью re и без.
#
# line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
#          'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
#          'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
#          'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
#          'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
#          'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
#          'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
#          'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
#          'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
#          'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
#          'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
#          'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
#          'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
#          'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
#          'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
#
#
# # Решение с помощью re:
# import re
# t2_lst_re = re.findall(r'(?:[a-z]{2})([A-Z]+)(?:[A-Z]{2})', line_2)
# print(f"Задание-2: Решение с помощью re: {t2_lst_re}")
#
# # Решение с без re:
# t2_lst_loop = []
# i = -1
# line_len = len(line_2)
# while i < line_len:
#     i += 1
#     if line_2[i:i+1].isupper():
#         pre = line_2[i-2:i:] if i > 1 else ''
#         if pre.islower():
#             j = i + 1
#             while j < line_len and line_2[j].isupper():
#                     j += 1
#             post = line_2[i:j]
#             if len(post) > 2:
#                 t2_lst_loop.append(post[:-2])
#             i += len(post)-1
# print(f"Задание-2: Решение с помощью цикла: {t2_lst_loop}")

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

from random import randint

f_name = './f_2500.txt'

with open(f_name, 'a') as f:
    for _ in range(25000):
        f.write(str(randint(0, 9)))

