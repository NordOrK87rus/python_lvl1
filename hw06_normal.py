# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#    (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#    (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import random

"""
В методичке увидел использование декоратора @property, по этому позволил себе его использовать :о)

Для удобства тестирования, в конце скрипта оставил процедуры создания классов и наподнения их тестовыми данными.

При наполнении данными возможны ругательства, что такой-то предмет уже преподаётся таким-то учителем. 
Специально не лечил, для наглядности работы ограничения по учителям у классе.
"""


class Person(object):
    def __init__(self, name="", surename="", patronymic=""):
        self._name = name
        self._sname = surename
        self._pname = patronymic

    def __str__(self):
        return f"{self.surename} {self.name} {self.patronymic}"

    @property
    def name(self):
        """
        Возвращает имя
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.split()

    @property
    def surename(self):
        """
        Возвращает фамилию
        """
        return self._sname

    @surename.setter
    def surename(self, value):
        self._sname = value.strip()

    @property
    def patronymic(self):
        """
        Возвращает отчество
        """
        return self._pname

    @patronymic.setter
    def patronymic(self, value):
        self._pname = value.strip()

    @property
    def fio(self):
        """
        Возвращает ФИО
        """
        return f"{self._sname.title()} {self._name[0].upper()}.{self._pname[0].upper()}."

    @property
    def full_name(self):
        """
        Возвращает полное имя
        """
        return f"{self._sname.title()} {self._name.title()}.{self._pname.title()}."


class Student(Person):
    def __init__(self, name="", surename="", patronymic="", mother=Person(), father=Person(), sch_class=None):
        super().__init__(name, surename, patronymic)
        self._mother = mother
        self._father = father
        self._sch_class = sch_class

    def __str__(self):
        return self.fio

    @property
    def parents(self):
        """
        Возвращает словарь с данными родителей
        """
        return {"mother": self.mother, "father": self.father}

    @property
    def parents_fullnames(self):
        """
        Возвращает строку с полными именами родителей
        """
        return f"Мама: {self._mother.full_name}, Папа: {self._father.full_name}"

    @property
    def parents_fio(self):
        """
        Возвращает строку с ФИО родителей
        """
        return f"Мама: {self._mother.fio}, Папа: {self._father.fio}"

    @property
    def mother(self):
        """
        Возвращает данные матери ученика
        """
        return self._mother

    @mother.setter
    def mother(self, value):
        if isinstance(value, Person):
            self._mother = value
        else:
            print("ERROR: значение должно быть объектом класса Person!")

    @property
    def father(self):
        """
        Возвращает данные отца ученика
        """
        return self._father

    @father.setter
    def father(self, value):
        if isinstance(value, Person):
            self._father = value
        else:
            print("ERROR: значение должно быть объектом класса Person!")

    @property
    def sch_class(self):
        """
        Возвращает класс, в которолм учится ученик
        """
        return self._sch_class

    @sch_class.setter
    def sch_class(self, value):
        if isinstance(value, SchClass):
            self._sch_class = value
        else:
            print("ERROR: значение должно быть объектом класса SchClass!")


class SchClass(object):
    def __init__(self, class_id, students=None, teachers=None):
        self.class_id = class_id
        self._student_list = []
        self._teachers = []

        if students:
            for i in students:
                self.add_student(i)

        if teachers:
            for i in teachers:
                self.add_teacher(i)

    def __str__(self):
        return f"{self.class_id}"

    def add_student(self, value):
        """
        Добавляет ученика в класс, предварительно проверяя его существование в существующем списке студентов
        данного класса
        :param value: объект Student
        """
        if isinstance(value, Student):
            if all(map(lambda x: x.name != value.name and
                                 x.surename != value.surename and
                                 x.patronymic != value.patronymic, self.class_students)):
                value.sch_class = self
                self._student_list.append(value)
            else:
                print(f"Ученик \"{value.full_name}\" уже числится в \" {self.class_id}\" классе ")
        else:
            print(f"ERROR: \"{value}\" не является объектом класса Student!")

    def add_teacher(self, value):
        """
        Добавляет учителя в класс, предварительно проверяя не преподаётся ли в данном классе  его
        предмет другим учителем.
        :param value: объект Teacher
        """
        if isinstance(value, Teacher):
            has_teacher = tuple(filter(lambda x: x.subject == value.subject, self._teachers))
            if not len(has_teacher):
                self._teachers.append(value)
            else:
                print(f"В классе \"{self.class_id}\" предмет \"{value.subject}\" уже преподаёт "
                      f"{has_teacher[0].full_name}")
        else:
            print(f"ERROR: \"{value}\" не является объектом класса Teacher!")

    @property
    def class_students(self):
        """
        Возвращает список учеников класса
        """
        return self._student_list

    @property
    def class_teachers(self):
        """
        Возвращает список учителей класса
        """
        return self._teachers

    @property
    def class_teachers_str(self):
        """
        Возвращяет строку со списком учителей класса, разделённых запятой
        """
        return ", ".join(map(str, self._teachers))


class Teacher(Person):
    def __init__(self, subj, name="", surename="", patronymic=""):
        super().__init__(name=name, surename=surename, patronymic=patronymic)
        self._subject = subj

    def __str__(self):
        return f"{self.fio} - {self.subject}"

    @property
    def subject(self):
        """
        Возвращает наименование предмета, преподаваемого учителем
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


class School(object):
    def __init__(self, school_id):
        self.school_id = school_id
        self.classes = []
        self.teachers = []

    def add_class(self, new_id, students=None, teachers=None):
        """
        Добавляет новый класс в школу
        :param new_id: идентификатор класса
        :param students: необязяательный параметр - список учеников класса
        :param teachers: необязяательный параметр - список преподавателей класса
        """
        new_id = new_id.upper()
        if all(map(lambda x: x.class_id != new_id, self.classes)):
            self.classes.append(SchClass(new_id, students, teachers))
        else:
            print(f"Класс \"{new_id}\" уже существует в школе № {self.school_id}.")

    def get_classes(self):
        """
        Возвращает строку классов школы, разделённых запятыми
        """
        return ", ".join(map(str, self.classes))

    def get_class(self, class_id):
        """
        Возвращает объект класса школы, согласно идентификатору класса
        :param class_id: идентификатор искомого класса
        """
        class_id = class_id.upper()
        for c in self.classes:
            if c.class_id == class_id:
                return c, None
        else:
            return None, f"В школе №{self.school_id} не существует класса \"{class_id}\"."

    def add_teacher(self, value):
        """
        Добавляет учителя в школу
        :param value: объект Teacher
        """
        if isinstance(value, Teacher):
            self.teachers.append(value)
        else:
            print(f"ERROR: \"{value}\" не является объектом класса Teacher!")

    def get_students_from_class(self, class_id):
        """
        Возвращает список учеников класса
        :param class_id: идентификатор анализируемого класса
        """
        _c, _c_err = self.get_class(class_id)
        if _c:
            return ", ".join(map(str, _c.class_students))
        else:
            return f"НЕТ -> {_c_err}"

    def get_student(self, surename, name, patronymic):
        """
        Возвращает объект ученика школы по фамилии, и мени и отчеству
        :param surename: фамилия
        :param name: имя
        :param patronymic: отчество
        """
        for cl in self.classes:
            for _s in cl.class_students:
                if _s.name == name and _s.surename == surename and _s.patronymic == patronymic:
                    return _s
        return None

    def get_student_subjects(self, student_full_name):
        """
        Возвращает список предметов, изучаемых учеником
        :param student_full_name: Фамилия имя отчество ученика
        """
        st = self.get_student(*student_full_name.split())
        if st:
            return ", ".join({i.subject for i in st.sch_class.class_teachers})
        else:
            return f"Ученик \"{student_full_name}\" не найден."


# Создали школу № 123
s123 = School(123)

# Формируем список учителей школы
s123.add_teacher(Teacher(surename="Треуголкина", name="Бэлла", patronymic="Эдуардовна", subj="Математика"))
s123.add_teacher(Teacher(surename="Рубик", name="Григорий", patronymic="Васильевич", subj="Математика"))
s123.add_teacher(Teacher(surename="Фуганок", name="Иван", patronymic="Петрович", subj="Труд"))
s123.add_teacher(Teacher(surename="Рубильник", name="Геннадий", patronymic="Сулейманович", subj="Труд"))
s123.add_teacher(Teacher(surename="Кречетова", name="Валенитина", patronymic="Юрьевна", subj="Литература"))
s123.add_teacher(Teacher(surename="Куркузова", name="Марина", patronymic="Сергеевна", subj="Музыка"))

# Добавляем классы сразу с учениками и учителями
s123.add_class("5A",
               students=[Student(surename="Иванов", name="Иван", patronymic="Петрович",
                                 mother=Person(surename="Иванова", name="Василиса", patronymic="Васильевна"),
                                 father=Person(surename="Иванов", name="Пётр", patronymic="Фёдорович")),
                         Student(surename="Захаркин", name="Василий", patronymic="Иванович",
                                 mother=Person(surename="Захаркина", name="Татьяна", patronymic="Дмитриевна"),
                                 father=Person(surename="Захаркин", name="Иванович", patronymic="Васильевич")),
                         ],

               )

s123.add_class("3В",
               students=[Student(surename="Ромашкина", name="Любовь", patronymic="Васильевна",
                                 mother=Person(surename="Ромашкина", name="Инга", patronymic="Захаровна"),
                                 father=Person(surename="Ромашкин", name="Геннадий", patronymic="Фёдорович")),
                         Student(surename="Шагрин", name="Сергей", patronymic="Александрович",
                                 mother=Person(surename="Шагрина", name="Елена", patronymic="Петровна"),
                                 father=Person(surename="Шагрин", name="Герман", patronymic="Дмитриевич")),
                         ],
               )

# Добавляем в классы случайный набор учителей из доступного списка
for c in ("5A", "3В"):
    cur_cl = s123.get_class(c)[0]
    used_ndx = set()
    while len(used_ndx) <= 3:
        i = random.randint(0, len(s123.teachers) - 1)
        if i not in used_ndx:
            cur_cl.add_teacher(s123.teachers[i])
            used_ndx.add(i)
        else:
            continue

# Выборки согласно задания:

print("--- 1. Получить полный список всех классов школы:")
print(f"Список классов школы №{s123.school_id}: {s123.get_classes()}")

print("\n--- 2. Получить список всех учеников в указанном классе (каждый ученик отображается в формате \"Фамилия "
      "И.О.\"):")
for c in ("5A", "3В"):
    print(f"Список учеников {c} класса школы №{s123.school_id}: {s123.get_students_from_class(c)}")

print("\n--- 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы):")
for s in ("Иванов Иван Петрович", "Шагрин Сергей Александрович",):
    print(f"Список предметов ученика \"{s}\": {s123.get_student_subjects(s)}")

print("\n--- 4. Узнать ФИО родителей указанного ученика:")
for s in ("Ромашкина Любовь Васильевна", "Захаркин Василий Иванович",):
    print(f"Родители ученика \"{s}\": {s123.get_student(*s.split()).parents_fio}")

print("\n--- 5. Получить список всех Учителей, преподающих в указанном классе:")
for c in ("5A", "3В"):
    cur_cl = s123.get_class(c)
    if cur_cl[0]:
        print(f"\nСписок учителей преподающих в классе \"{cur_cl[0]}\": \n - ", "\n -  ".join(map(str,
                                                                                                  cur_cl[
                                                                                                      0].class_teachers)
                                                                                              )
              )
    else:
        print(cur_cl[1])
