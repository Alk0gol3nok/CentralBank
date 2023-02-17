from Packages.Classes.SomeClass.some_reason import some_general_structure


class balances_institutions(some_general_structure):
    table_name = 'Example_three'
    field_list = ['InRussia', 'InMoscow', 'Date']

    def __init__(self, day_start, month_start, year_start, day_end, month_end, year_end, query_string):
        super().__init__(day_start, month_start, year_start, day_end, month_end, year_end, query_string)

    def _start_initialization(self):
        super()._start_initialization()
        super()._transformation(self.init_dict)
        super()._finish_string()
        self._collection_of_dates(self.xml_structure)

    def _collection_of_dates(self, xml_structure):
        date_list = []
        for tag in xml_structure:
            date_list.append(str(tag.attrib['Date']))

        self._loading_structure(xml_structure, date_list)

    def _loading_structure(self, xml_structure, date_list):
        intermediate_list = []
        general_list = []
        index_structure = 0
        index_date = 0

        while index_structure < len(xml_structure):
            for elem in xml_structure[index_structure]:
                intermediate_list.append(elem.text)
            index_structure += 1

            intermediate_list.append(date_list[index_date])
            general_list.append(intermediate_list)
            intermediate_list = []
            index_date += 1

        self._editing_data(general_list)

    def _editing_data(self, general_list):
        for sheet in general_list:
            sheet[0] = sheet[0].replace(',', '.')
            sheet[0] = float(sheet[0])
            sheet[1] = sheet[1].replace(',', '.')
            sheet[1] = float(sheet[1])

        self._sql_request(general_list)

    def _sql_request(self, general_list):
        sql_insert_param = ('insert into ' +
                            self.table_name + ' (' +
                            self.field_list[0] + ', ' +
                            self.field_list[1] + ', ' +
                            self.field_list[2] + ') ' +
                            'values (?, ?, ?)')
        self._accept_sql(general_list, sql_insert_param)


update_query = balances_institutions(day_start=1, month_start=6, year_start=2001, day_end=22, month_end=6,
                                     year_end=2001, query_string='http://www.cbr.ru/scripts/XML_ostat.asp?date_req1'
                                                                 '=%s/%s/%s&date_req2=%s/%s/%s')

update_query._start_initialization()


