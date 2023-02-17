from Packages.DataBase import configuration
from Packages.Parser import library
from set_and_get import solo_setters_and_getters


class quote_today(solo_setters_and_getters):
    query_string = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s/%s/%s'
    table_name = 'Example_one'
    field_list = ['NumCode', 'CharCode', 'Nominal', 'Name', 'Value', 'Date']

    def __init__(self, day, month, year):
        super().__init__(day, month, year)

    def _start_initialization(self):
        day = self.get_day()
        month = self.get_month()
        year = self.get_year()

        init_dict = {'day': day, 'month': month, 'year': year}

        self._transformation(init_dict)

    def _transformation(self, init_dict):
        dict_data = self._rebuild_date(init_dict['day'], init_dict['month'], init_dict['year'])

        self._preparation_for_request(dict_data)
        self._finish_string(dict_data)

    @staticmethod
    def _rebuild_date(day, month, year):
        if int(day) < 10:
            day = ('0%s' % day)
        else:
            day = (str(day))
        if int(month) < 10:
            month = ('0%s' % month)
        else:
            month = (str(month))

        return {'day': day, 'month': month, 'year': year}

    @classmethod
    def _preparation_for_request(cls, dict_data):
        for key in dict_data:
            cls.query_string = cls.query_string.replace('%s', str(dict_data[key]), 1)

    def _finish_string(self, dict_data):
        xml_structure = (library.ET.fromstring(library.requests.get(self.query_string).content))

        self._loading_structure(xml_structure, dict_data)

    def _loading_structure(self, xml_structure, dict_data):
        date = f'{dict_data["day"]}.{dict_data["month"]}.{dict_data["year"]}'
        intermediate_list = []
        general_list = []
        index_structure = 0

        while index_structure < len(xml_structure):
            for elem in xml_structure[index_structure]:
                intermediate_list.append(elem.text)
            index_structure += 1

            intermediate_list.append(date)
            general_list.append(intermediate_list)
            intermediate_list = []

        self._editing_data(general_list, date)

    def _editing_data(self, general_list, date):
        for sheet in general_list:
            sheet[2] = int(sheet[2])
            sheet[4] = sheet[4].replace(',', '.')
            sheet[4] = float(sheet[4])

        self._sql_request(general_list, date)

    def _sql_request(self, general_list, date):
        sql_insert_param = ('insert into ' +
                            self.table_name + ' (' +
                            self.field_list[0] + ', ' +
                            self.field_list[1] + ', ' +
                            self.field_list[2] + ', ' +
                            self.field_list[3] + ', ' +
                            self.field_list[4] + ', ' +
                            self.field_list[5] + ') ' +
                            'values (?, ?, ?, ?, ?, ?)')

        self._accept_sql(general_list, sql_insert_param)
        self._check_data(date)

    @staticmethod
    def _accept_sql(general_list, sql_insert_param):
        for sheet in general_list:
            configuration.cursor.execute(sql_insert_param, sheet)
            configuration.cursor.commit()
            configuration.connection_to_db.commit()
        return True

    def _check_data(self, date):
        date_dictionary = {'day': date[0:2], 'month': date[3:5], 'year': date[6:]}

        if str(date_dictionary['day'][0]) == '0':
            date_dictionary['day'] = int(date_dictionary['day'][-1])
        else:
            date_dictionary['day'] = int(date_dictionary['day'][:])
        if str(date_dictionary['month'][0]) == '0':
            date_dictionary['month'] = int(date_dictionary['month'][-1])
        else:
            date_dictionary['month'] = int(date_dictionary['month'][:])

        day_check = date_dictionary['day']
        month_check = date_dictionary['month']
        year_check = int(date_dictionary['year'])
        self._check_limit(day_check, month_check, year_check)

    def _check_limit(self, day, month, year): # 2/2/2002
        high_year_list = [2000, 2004, 2008, 2012, 2016, 2020, 2024]
        month_31_list = [1, 3, 5, 7, 8, 10, 12]

        if year in high_year_list:
            if month == 2:
                if day == 29:
                    day = 1
                    month += 1
                    return
                day += 1
                return
            else:
                if month in month_31_list:
                    if month == 12:
                        if day == 31:
                            day = 1
                            month = 1
                            year += 1
                            return
                        else:
                            day += 1
                            return
                    else:
                        if day == 31:
                            day = 1
                            month += 1
                            return
                        else:
                            day += 1
                            return
                else:
                    if day == 30:
                        day = 1
                        month += 1
                        return
                    else:
                        day += 1
                        return

        if month in month_31_list:
            if month == 12:
                if day == 31:
                    month = 1
                    year += 1
                    day = 1
                else:
                    day += 1
            else:
                if day == 31:
                    day = 1
                    month += 1
                else:
                    day += 1
        else:
            if month == 2:
                if day == 28:
                    day = 1
                    month += 1
                else:
                    day += 1
            else:
                if day == 30:
                    day = 1
                    month += 1
                else:
                    day += 1

        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

        self._checker()

    def _checker(self):
        if self.get_day() == 22 and self.get_month() == 3 and self.get_year() == 2002:
            print(f'{self.get_day()}.{self.get_month()}.{self.get_year()} - Failing')
            library.sys.exit('Выход за диапазон')
        else:
            print(f'{self.get_day()}.{self.get_month()}.{self.get_year()} - Success')


