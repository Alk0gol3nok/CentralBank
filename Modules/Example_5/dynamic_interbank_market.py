from Packages.Classes.SomeClass.some_reason import some_general_structure


class interbank_quote(some_general_structure):
    table_name = 'Example_five'
    field_list = ['SberBank', 'VTB', 'Tinkof', 'SovkomBank', 'AlfaBank', 'MtsBank', 'Date', 'Time']

    def __init__(self, day_start, month_start, year_start, day_end, month_end, year_end, query_string):
        super().__init__(day_start, month_start, year_start, day_end, month_end, year_end, query_string)

    def _start_initialization(self):
        super()._start_initialization()
        super()._transformation(self.init_dict)
        super()._finish_string()
        self._collection_of_dates(self.xml_structure)

    def _collection_of_dates(self, xml_structure):
        date_list = []
        time_code_list = []
        for tag in xml_structure:
            date_list.append(str(tag.attrib['Date']))
            time_code_list.append(str(tag.attrib['Code']))

        time_list = self._change_code_time(time_code_list)
        self._loading_structure(xml_structure, date_list, time_list)

    @staticmethod
    def _change_code_time(time_code_list):
        time_list = []
        for code in time_code_list:
            if code == '1':
                time_list.append('8:00')
            elif code == '2':
                time_list.append('16:00')
            elif code == '3':
                time_list.append('00:00')
        return time_list

    def _loading_structure(self, xml_structure, date_list, time_list):
        intermediate_list = []
        general_list = []
        index_structure = 0
        index_elem = 0

        while index_structure < len(xml_structure):
            for elem in xml_structure[index_structure]:
                intermediate_list.append(elem.text)
            index_structure += 1

            intermediate_list.append(date_list[index_elem])
            intermediate_list.append(time_list[index_elem])
            general_list.append(intermediate_list)
            intermediate_list = []
            index_elem += 1

        self._editing_data(general_list)

    def _editing_data(self, general_list):
        for sheet in general_list:
            for value in sheet[:6]:
                if value == '-':
                    new_value = value.replace('-', '.')
                    new_value = float(f'0{new_value}00')

                    index = sheet.index(value)
                    sheet.pop(index)
                    sheet.insert(index, new_value)
                else:
                    value = value.replace(',', '.')
                    value = float(value)
        self._sql_request(general_list)

    def _sql_request(self, general_list):
        sql_insert_param = ('insert into ' +
                            self.table_name + ' (' +
                            self.field_list[0] + ', ' +
                            self.field_list[1] + ', ' +
                            self.field_list[2] + ', ' +
                            self.field_list[3] + ', ' +
                            self.field_list[4] + ', ' +
                            self.field_list[5] + ', ' +
                            self.field_list[6] + ', ' +
                            self.field_list[7] + ') ' +
                            'values (?, ?, ?, ?, ?, ?, ?, ?)')

        self._accept_sql(general_list, sql_insert_param)


update_query = interbank_quote(day_start=1, month_start=7, year_start=2001, day_end=13, month_end=7, year_end=2001,
                               query_string='http://www.cbr.ru/scripts/xml_mkr.asp?'
                                            'date_req1=%s/%s/%s&date_req2=%s/%s/%s')

update_query._start_initialization()
