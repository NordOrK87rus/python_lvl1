# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker(object):
    def __init__(self, data):
        self.name, self.surename, self.zp, self.rank, self.norm = data.split()
        self.zp = int(self.zp)
        self.norm = int(self.norm)

    @property
    def full_name(self):
        return f"{self.name.title()} {self.surename.title()}"

    def calc_zp(self, wh):
        wh = int(wh)
        if wh < self.norm:
            return int((self.zp / self.norm) * wh)
        elif wh > self.norm:
            return self.zp + int(((self.zp / self.norm) * 2) * (wh - self.norm))
        else:
            return self.zp


workers_list = []
with open("data/workers", "r") as wf:
    for w in wf.readlines()[1:]:
        workers_list.append(Worker(w))

with open("data/hours_of") as hours:
    for hof in hours.readlines()[1:]:
        n, s, hf = hof.split()
        for w in workers_list:
            if w.name == n and w.surename == s:
                print(f"{w.full_name} отработано {hf} часов, зарплата {w.calc_zp(hf)}")
                break
        else:
            print(f"Работник {n.title()} {s.title()} не найден.")
