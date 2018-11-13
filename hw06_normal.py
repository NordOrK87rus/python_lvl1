# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# + 1. Получить полный список всех классов школы
# ! 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# ! 4. Узнать ФИО родителей указанного ученика
# ! 5. Получить список всех Учителей, преподающих в указанном классе


class Human(object):
    def __init__(self, name="", sname="", pname=""):
        self.name = name
        self.sname = sname
        self.pname = pname

    def set_name(self, value):
        self.name = value

    def set_sname(self, value):
        self.sname = value

    def set_pname(self, value):
        self.sname = value

    def get_fio(self):
        return f"{self.sname.title()} {self.name[0].upper()}.{self.pname[0].upper()}."


class Student(Human):
    def __init__(self, name="", sname="", pname="", mother=Human(), father=Human()):
        super().__init__(name, sname, pname)
        self.mother = mother
        self.father = father

    def __str__(self):
        return self.get_fio()

    def __unicode__(self):
        return self.get_fio()

    def get_parents_fio(self):
        return f"Мама: {self.mother.get_fio()}, Папа: {self.father.get_fio()} "

    def set_mother(self, value):
        if isinstance(value, Human):
            self.mother = value
        else:
            print("ERROR: значение должно быть объектом класса Human!")

    def set_father(self, value):
        if isinstance(value, Human):
            self.father = value
        else:
            print("ERROR: значение должно быть объектом класса Human!")


class SClass(object):
    def __init__(self, class_id, students=None, teachers=None):
        self.class_id = class_id
        self.students = []
        self.teachers = []

        if students:
            for s in students:
                self.add_student(s)

        if teachers:
            for t in students:
                self.add_teacher(t)

    def __str__(self):
        return f"{self.class_id} класс"

    def __unicode__(self):
        return f"{self.class_id} класс"

    def add_student(self, value):
        if isinstance(value, Student):
            self.students.append(value)
        else:
            print(f"ERROR: \"{value}\" не является объектом класса Student!")

    def add_teacher(self, value):
        if isinstance(value, Teacher):
            self.teachers.append(value)
        else:
            print(f"ERROR: \"{value}\" не является объектом класса Teacher!")

    def get_students(self):
        return self.students

    def get_teachers(self):
        return self.teachers


class Teacher(Human):
    def __init__(self, subj):
        super().__init__()
        self.subject = subj


class School(object):
    def __init__(self, school_id):
        self.school_id = school_id
        self.classes = []

    def add_class(self, new_id, students=None, teachers=None):
        new_id = new_id.upper()
        if all(map(lambda x: x.class_id != new_id, self.classes)):
            self.classes.append(SClass(new_id, students, teachers))
        else:
            print(f"Класс \"{new_id}\" уже существует в школе № {self.school_id}.")

    def get_classes(self):
        """
        Возвращает словарь объектов классов школы, где ключ это ID класса, а значение объект класса
        """
        return {i.class_id: i for i in self.classes}

    def get_class(self, class_id):
        class_id = class_id.upper()
        for c in self.classes:
            if c.class_id == class_id:
                return c
        else:
            print(f"В школе №{self.school_id} не существует класса \"{class_id}\".")
            return None


# Создали школу № 123
s123 = School(123)

# Добавляем классы
s123.add_class("5A")
s123.add_class("6Б")
s123.add_class("3В")

# 1 способ добавить ученика:
# получаем Класс в который необходимо добавить ученика
cl = s123.get_class("5A")
# создаём ученика
s = Student(sname="Иванов", name="Иван", pname="Петрович")
# добавляем родителей
s.set_mother(Human(sname="Иванова", name="Василиса", pname="Мудрёновна"))
s.set_father(Human(sname="Иванов", name="Тимур", pname="Задумкин"))
# добавляем ученика в класс
cl.add_student(s)




print(f"Список классов школы №{s123.school_id}:", ", ".join(s123.get_classes().keys()))

x = 0
