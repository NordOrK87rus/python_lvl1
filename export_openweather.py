""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды,
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]

При выгрузке в html можно по коду погоды (weather.id) подтянуть
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sqlite3
import sys


def print_usage():
    print("Usage any from: \nexport_openweather.py --csv filename [<город>]\n"
          "export_openweather.py --json filename [<город>]\n"
          "export_openweather.py --html filename [<город>]\n")


def save_csv(fn, data):
    """
    Процедура экспорта в CSV
    :param fn: имя файла
    :param data: данные для экспорта
    """
    with open(fn, 'w') as f:
        csv_w = csv.DictWriter(f, fieldnames=data[0].keys())
        csv_w.writeheader()
        csv_w.writerows(data)


def save_json(fn, data):
    """
    Процедура экспорта в JSON
    :param fn: имя файла
    :param data: данные для экспорта
    """
    with open(fn, 'w') as f:
        json.dump(data, f)


def save_html(fn, data):
    """
    Процедура экспорта в HTML
    :param fn: имя файла
    :param data: данные для экспорта
    """
    icons = [((200, 201, 202, 211, 212, 221, 230, 231, 232), 'http://openweathermap.org/img/w/11d.png'),
             ((300, 301, 302, 310, 311, 312, 313, 314, 321, 520, 521, 522, 531),
              'http://openweathermap.org/img/w/09d.png'),
             ((500, 501, 502, 503, 504, 511, 600, 601, 602, 611, 612, 615, 616, 620, 621, 622),
              'http://openweathermap.org/img/w/13d.png'),
             ((701, 711, 721, 731, 751, 761, 762, 771, 781), 'http://openweathermap.org/img/w/50d.png'),
             ((741,), 'http://openweathermap.org/img/w/0d.png'),
             ((800,), 'http://openweathermap.org/img/w/01d.png'),
             ((801,), 'http://openweathermap.org/img/w/02d.png'),
             ((802,), 'http://openweathermap.org/img/w/03d.png'),
             ((803, 804), 'http://openweathermap.org/img/w/04d.png')
             ]

    def get_icon(code):
        """
        Возвращает URL иконки
        """
        for ic in icons:
            if code in ic[0]:
                return ic[1]
        else:
            return ""

    with open(fn, 'w') as f:
        f.write('<!DOCTYPE html>'
                '<html lang="en">'
                '<head><meta charset="UTF-8"></head>'
                '<body>'
                '<table border>'
                '<tr><th>icon</th>')
        for i in data[0].keys():
            f.write(f"<th>{i}</th>")
        else:
            f.write("</tr>")

        for i in data:
            f.write(f"<tr><td><img src=\"{get_icon(i['weather_id'])}\" alt=\"{i['weather_id']}\"></td>")
            f.write("".join(map(lambda x: f"<td>{x}</td>", i.values())))

            f.write("</tr>")
        f.write("</table></body>")


def main():
    exp_func, f_name, city = None, None, None

    if len(sys.argv) < 3:
        print_usage()
    else:
        f_name = sys.argv[2]
        if sys.argv[1] == '--csv':
            exp_func = save_csv
        elif sys.argv[1] == '--json':
            exp_func = save_json
        elif sys.argv[1] == '--html':
            exp_func = save_html
        else:
            print("Выбране неверный формат экспорта!")
            print_usage()
            exit()

        if len(sys.argv) > 3:
            city = sys.argv[-1]

    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    if city:
        cursor.execute(f"SELECT id_city FROM weather where city=\'{city}\';")
        if len(cursor.fetchall()) > 0:
            cursor.execute(f"SELECT * from weather where city=\'{city}\';")
        else:
            print("Неверно указан город для выгрузки!")
            exit()
    else:
        cursor.execute(f"SELECT * from weather;")

    r_data = cursor.fetchall()
    if len(r_data) > 0:
        d_data = []
        fields = ('id', 'name', 'date', 'temp', 'weather_id')
        for i in r_data:
            d_data.append({})
            for j in range(5):
                d_data[-1][fields[j]] = i[j]

        exp_func(f_name, d_data)
        print(f"Экспорт в файл {f_name} выполнен!")
    else:
        print('Нет данных для выгрузки! (БД не содержит записей)')


if __name__ == "__main__":
    main()
