from Packages.Classes.SomeClass.some_reason import some_general_structure


class range_query_dollar(some_general_structure):
    table_name = 'Example_two'
    field_list = ['Nominal', 'Value', 'Date']

    def __init__(self, day_start, month_start, year_start, day_end, month_end,
                 year_end, query_string, code_valuta):
        super().__init__(day_start, month_start, year_start, day_end, month_end,
                         year_end, query_string)
        self.code_valuta = code_valuta

    def _start_initialization(self):
        super()._start_initialization()
        self.init_dict['code_valuta'] = self.code_valuta
        super()._transformation(self.init_dict)
        self._set_query_string(self._get_query_string().replace('%s', self.code_valuta, 1))
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
            sheet[0] = int(sheet[0])
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


update_query = range_query_dollar(day_start=2, month_start=3, year_start=2001, day_end=14, month_end=3,
                                  year_end=2001,
                                  query_string='http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=%s/%s/%s'
                                               '&date_req2=%s/%s/%s&VAL_NM_RQ=%s', code_valuta='R01235')
update_query._start_initialization()
