"""
== OpenWeatherMap ==
OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.
Необходимо решить следующие задачи:
== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)
        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up
        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in
        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a
    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}
== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):
    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных
2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))
3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.
При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.
При работе с XML-файлами:
Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>
Чтобы работать с пространствами имен удобно пользоваться такими функциями:
    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''
    tree = ET.parse(f)
    root = tree.getroot()
    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}
    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...
"""
import os
import urllib.request as url_req
import gzip
import json
import xml.etree.ElementTree as ET
import sqlite3
import datetime as dtm

APPID = None


def update_data(func):
    """
    Декоратор обновляющий данные в БД перед выборкой
    """
    def wrapper(self, value, dt=None):
        def f_date(v):
            return int(dtm.datetime.fromisoformat(v.isoformat()).timestamp())

        cur_date = f_date(dtm.datetime.date(dtm.datetime.utcnow()))
        for r in range(0, len(value), 20):
            id_s = ",".join(map(str, list(value.keys())[r: r + 20]))
            resp = url_req.urlopen(f'http://api.openweathermap.org/data/2.5/group?id={id_s}&units=metric'
                                   f'&mode=xml&appid={APPID}')

            t_json = json.load(resp)
            for i in t_json['list']:
                print(f"Обновление данных для города \"{i['name']}\"...", end="")
                self.cursor.execute(f"SELECT * FROM weather WHERE id_city={i['id']};")

                if len(self.cursor.fetchall()) > 0:
                    self.cursor.execute(f"UPDATE weather SET temper={i['main']['temp']}, date={cur_date} "
                                        f"WHERE id_city={i['id']};")
                    self._conn.commit()
                else:
                    self.cursor.execute(f"INSERT INTO weather VALUES ({i['id']},\'{i['name']}\',"
                                        f"{f_date(dtm.datetime.fromtimestamp(i['dt']).date())},"
                                        f"{i['main']['temp']},{i['weather'][0]['id']});")
                    self._conn.commit()
                print(" Ok")
        return func(self, value, dt)

    return wrapper


class OWData(object):
    class CityList(object):
        def __init__(self):
            self._files = {'cities': ('city.list.json.gz', 'http://bulk.openweathermap.org/sample/city.list.json.gz'),
                           'country_codes': ('country_codes.xml', 'http://www.artlebedev.ru/country-list/xml/')}

            for k, f in self._files.items():
                if not os.path.exists(f[0]):
                    print(f"Файл {f[0]} не найден! \nСкачиваю файл.... ", end="")
                    resp = url_req.urlopen(f[1])
                    with open(f[0], 'wb') as fd:
                        fd.write(resp.read())
                    print("Ok")

            # Вычитываем данные из списка городов
            with gzip.open(self._files['cities'][0]) as gf:
                self._data = json.load(gf)

            # Вычитываем коды стран
            self._country_codes = ET.parse(self._files['country_codes'][0])

        @property
        def countries(self):
            """
            Возвращает список доступных стран
            """
            result = set()
            for c in {i['country'] for i in self._data if len(i['country']) > 0}:
                result.add((c, self._country_codes.findtext(f'./country/[alpha2=\"{c}\"]/english')))
            return sorted(result)

        def cities_of_country(self, country):
            """
            Перечень городов страны
            :param country: наименование анализируемой страны
            """
            if len(country) > 2:
                ccode = self._country_codes.findtext(f'./country/[english=\"{country}\"]/alpha2')
            else:
                ccode = country.upper()
            return {i["id"]: i["name"] for i in self._data if i['country'] == ccode}

        def find_country(self, value):
            """
            Ищет страну по коду или наименованию

            """
            result = self._country_codes.findtext(f'./country/[alpha2=\"{value.upper()}\"]/alpha2')
            result = self._country_codes.findtext(f'./country/[english=\"{value}\"]/alpha2') if not result else result
            return result

        def find_city(self, value):
            """
            Поиск города
            """
            try:
                return {next(filter(lambda x: x["name"] == value, self._data))['id']: value}
            except StopIteration:
                return

    # ------------------------------------------------------------------
    class LocalDB(object):
        def __init__(self):
            self._conn = sqlite3.connect("weather.db")
            self.cursor = self._conn.cursor()
            if not self._check_db():
                self.cursor.execute("CREATE TABLE weather("
                                    "id_city INTEGER PRIMARY KEY,"
                                    "city VARCHAR(255), "
                                    "date DATE, "
                                    "temper INTEGER, "
                                    "id_weather INTEGER )")

        def __del__(self):
            self._conn.close()

        def _check_db(self):
            """
            Проверяет существование нужной нам таблицы
            """
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name='weather';")
            return len(self.cursor.fetchall())

        def find_city_by_name(self, value):
            """
            Поиск в БД города по наименованию
            """
            self.cursor.execute(f"SELECT DISTINCT id_city, city FROM weather WHERE city=\'{value}\';")
            return self.cursor.fetchall()

        @update_data
        def get_city_data(self, value, dt=None):
            """
            Получение данных по городу/списку городов из БД
            """
            self.cursor.execute(f"SELECT * FROM weather WHERE id_city "
                                f"IN({','.join(map(str, value.keys()))}) {'AND date=%d' % dt if dt else ' '} ORDER "
                                f"BY city ASC;")
            return self.cursor.fetchall()

    # ------------------------------------------------------------------
    def __init__(self):
        global APPID
        self._cl = OWData.CityList()
        self._db = OWData.LocalDB()

        try:
            with open('app.id', 'r') as f_id:
                result = f_id.read()
        except FileNotFoundError:
            print(f'Не найден файл app.id')
        except IOError as e:
            print(e)
        else:
            APPID = result.strip()

    @property
    def countries(self):
        return self._cl.countries

    def print_countries(self):
        """
        Выводит список доступных в файле стран
        """
        print("Список доступных стран:")
        s_template = "[{0:<2}] {1:<%d}" % (max(map(lambda x: len(x[1]) if x[1] else 0, self.countries)) + 2)
        for i in sorted({l[0][0] for l in self.countries}):
            print(f"------------\n{i}:\n------------")
            cl = list(filter(lambda x: x[0][0] == i, self.countries))
            for j in range(0, len(cl), 2):
                s = ""
                for ci in cl[j: j + 2]:
                    s += s_template.format(ci[0], ci[1] if ci[1] else f"{ci[0]}_UNKNOWN")
                print(s)

    def print_cities_of_country(self, country):
        """
        Выводит список городов указанной страны
        :param country: страна для выборки
        """
        print(f"Список городов страны {country}:")
        ccl = self._cl.cities_of_country(country)
        if len(ccl) > 0:
            s_template = " ".join(
                ["{%d:<%d}" % (i[0], i[1],) for i in enumerate([max(map(len, ccl.values())) + 2] * 3)])
            ccl_si = sorted(ccl, key=lambda x: ccl[x])
            for j in range(0, len(ccl), 3):
                print(s_template.format(*(map(lambda x: ccl.get(x, ""), ccl_si[j:j + 3] +
                                              [""] * (3 - len(ccl_si[j:j + 3]))))))
        else:
            print(f"Не могу найти города для страны \"{country}\"")

    def print_weather(self, trg_data):
        """
        Выводит данные о погоде
        """
        data_lst = {}
        country = self._cl.find_country(trg_data)
        if not country:

            city = self._db.find_city_by_name(trg_data)
            city = {city[0][0]: city[0][1]} if len(city) > 0 else self._cl.find_city(trg_data)
            if city:
                data_lst.update(city)
        else:
            data_lst.update(self._cl.cities_of_country(country))

        c_data = self._db.get_city_data(data_lst)
        if len(c_data) > 0:
            max_clen = max(map(lambda x: len(x) + 2, data_lst.values()))
            h_line = ("{l_sym:-^%d}+{l_sym:-^13}+{l_sym:-^17}" % (max_clen if max_clen > 7 else 7)).format(l_sym="-")
            s_template = "{0:<%d}|{1:^13}|{2:^17}" % (max_clen if max_clen > 7 else 7)
            print(h_line)
            print(s_template.format("Город", "Температура", "Дата"))
            print(h_line)
            for i in c_data:
                print(s_template.format(i[1], i[3], dtm.date.fromtimestamp(i[2]).strftime('%d.%m.%Y')))
        else:
            print("Данные не обнаружены!")


def print_help():
    """
    Вывод помощи
    """
    print("\n"+"=" * 15)
    for m in ((1, "Вывести список доступных стран"), (2, "Вывести список доступных городов"),
              (3, "Вывести данные о погоде"), (0, "Выход"),
              ):
        print(f"{m[0]}. {m[1]}")
    print("-" * 15)


def main():
    owd = OWData()
    while True:
        print_help()
        user_answer = input("Выберите действие: ")

        if user_answer == "1":
            owd.print_countries()
        elif user_answer == "2":
            cur_country = input("Ввведите код страны или её название (из списка): ")
            owd.print_cities_of_country(cur_country.strip())
        elif user_answer == "3":
            req_data = input("Ввведите город или страну для выборки: ")
            owd.print_weather(req_data.strip())
        elif user_answer == "0":
            break
        else:
            print("Вы ввели неверную команду, попробуйте ещё раз.")


if __name__ == "__main__":
    main()
