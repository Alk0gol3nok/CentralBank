from Packages.Classes.SomeClass.some_reason import some_general_structure


class precious_metals(some_general_structure):
    table_name = 'Example_four'
    field_list = ['Buy', 'Sell', 'Date', 'Metal']

    def __init__(self, day_start, month_start, year_start, day_end, month_end, year_end, query_string):
        super().__init__(day_start, month_start, year_start, day_end, month_end, year_end, query_string)

    def _start_initialization(self):
        super()._start_initialization()
        super()._transformation(self.init_dict)
        super()._finish_string()
        self._collection_of_dates(self.xml_structure)

    def _collection_of_dates(self, xml_structure):
        date_list = []
        metal_code_list = []
        for tag in xml_structure:
            date_list.append(str(tag.attrib['Date']))
            metal_code_list.append(str(tag.attrib['Code']))

        metal_list = self._change_code_metal(metal_code_list)
        self._loading_structure(xml_structure, date_list, metal_list)

    @staticmethod
    def _change_code_metal(metal_code_list):
        metal_list = []
        for code in metal_code_list:
            if code == '1':
                metal_list.append('Палладий')
            elif code == '2':
                metal_list.append('Золото')
            elif code == '3':
                metal_list.append('Иридий')
            elif code == '4':
                metal_list.append('Родий')
        return metal_list

    def _loading_structure(self, xml_structure, date_list, metal_list):
        intermediate_list = []
        general_list = []
        index_structure = 0
        index_elem = 0

        while index_structure < len(xml_structure):
            for elem in xml_structure[index_structure]:
                intermediate_list.append(elem.text)
            index_structure += 1

            intermediate_list.append(date_list[index_elem])
            intermediate_list.append(metal_list[index_elem])
            general_list.append(intermediate_list)
            intermediate_list = []
            index_elem += 1

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
                            self.field_list[2] + ', ' +
                            self.field_list[3] + ') ' +
                            'values (?, ?, ?, ?)')

        self._accept_sql(general_list, sql_insert_param)


update_query = precious_metals(day_start=1, month_start=7, year_start=2001, day_end=13, month_end=7, year_end=2001,
                               query_string='http://www.cbr.ru/scripts/xml_metall.asp?'
                                            'date_req1=%s/%s/%s&date_req2=%s/%s/%s')

update_query._start_initialization()


