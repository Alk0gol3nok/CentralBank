class solo_setters_and_getters:
    def __init__(self, day, month, year):
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

    # Сеттеры
    def set_day(self, day):
        self.day = day

    def set_month(self, month):
        self.month = month

    def set_year(self, year):
        self.year = year

    # Геттеры
    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year
