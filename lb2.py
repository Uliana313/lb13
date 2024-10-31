class WORKER:
    def __init__(self, Names, YearBorn, Work):
        self.Names = Names
        self.YearBorn = YearBorn
        self.Work = Work

    def CalcAge(self, current_year):
        return current_year - self.YearBorn

    def ShowYear(self):
        print(f"Рік народження: {self.YearBorn}")

    def SetWork(self, new_work):
        self.Work = new_work

# Основна програма
if __name__ == "__main__":
    worker1 = WORKER("Василій Пупкін", 1986, 11)
    worker2 = WORKER("Марія Морич ", 1997, 8)
    worker3 = WORKER("Олександр Совейко", 2004, 2)

    current_year = 2023

    total_work_experience = worker1.Work + worker2.Work + worker3.Work
    total_age = worker1.CalcAge(current_year) + worker2.CalcAge(current_year) + worker3.CalcAge(current_year)

    print(f"Сумарний стаж роботи: {total_work_experience}")
    print(f"Сумарний вік: {total_age}")