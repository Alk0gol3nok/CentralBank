from Packages.Classes.SomeClass.some_reason import some_general_structure


class h_pay(some_general_structure):
    table_name = 'Example_ten'
    field_list = ['Date', 'Price', 'Nominal', 'Metall', 'Q']

    def __init__(self, day_start, month_start, year_start, day_end, month_end, year_end, query_string):
        super().__init__(day_start, month_start, year_start, day_end, month_end, year_end, query_string)

    def _start_initialization(self):
        super()._start_initialization()
        super()._transformation(self.init_dict)
        super()._finish_string()
        self._loading_structure(self.xml_structure)

    def _loading_structure(self, xml_structure):
        intermediate_list = []
        general_list = []
        index_structure = 0
        index_elem = 0

        while index_structure < len(xml_structure):
            for elem in xml_structure[index_structure]:
                intermediate_list.append(elem.text)
            index_structure += 1

            general_list.append(intermediate_list)
            intermediate_list = []
            index_elem += 1
        self._editing_data(general_list)

    def _editing_data(self, general_list):
        for sheet in general_list:
            for value in sheet:
                if value == sheet[0]:
                    continue
                if ',' in value:
                    new_dot = value.replace(',', '.')
                    new_dot = float(new_dot)

                    index_comma = sheet.index(value)
                    sheet.pop(index_comma)
                    sheet.insert(index_comma, new_dot)
                else:
                    new_number = int(value)

                    index_number = sheet.index(value)
                    sheet.pop(index_number)
                    sheet.insert(index_number, new_number)
        self._sql_request(general_list)

    def _sql_request(self, general_list):
        sql_insert_param = ('insert into ' +
                            self.table_name + ' (' +
                            self.field_list[0] + ', ' +
                            self.field_list[1] + ', ' +
                            self.field_list[2] + ', ' +
                            self.field_list[3] + ', ' +
                            self.field_list[4] + ') ' +
                            'values (?, ?, ?, ?, ?)')

        self._accept_sql(general_list, sql_insert_param)


update_query = h_pay(day_start=1, month_start=12, year_start=2005, day_end=6, month_end=12, year_end=2005,
                     query_string='http://www.cbr.ru/scripts/XMLCoinsBase.asp?date_req1=%s/%s/%s&date_req2=%s/%s/%s')

update_query._start_initialization()