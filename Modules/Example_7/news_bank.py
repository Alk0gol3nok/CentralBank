from Packages.Classes.SoloClass.solo_reason import solo_general_structure


class parse_news(solo_general_structure):
    def __init__(self, table_name, field_list, query_string):
        super().__init__(table_name, field_list, query_string)

    def _start_initialization(self):
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
                if value == sheet[1]:
                    new_string = value.replace(' ', '')

                    index_string = sheet.index(value)
                    sheet.pop(index_string)
                    sheet.insert(index_string, new_string)
                elif value == sheet[-1]:
                    index_first = value.index(' ')
                    index_second = value.index(' ', index_first + 1)
                    index_third = value.index(' ', index_second + 1)
                    index_fourth = value.index(' ', index_third + 1)
                    index_fifth = value.index(' ', index_fourth + 1)
                    index_sixth = value.index(' ', index_fifth + 1)
                    new_news = value[:index_sixth]

                    index_news = sheet.index(value)
                    sheet.pop(index_news)
                    sheet.insert(index_news, new_news)
        super()._sql_request(general_list)


update_query = parse_news(table_name='Example_seven', field_list=['Date', 'Url', 'Title'],
                          query_string='https://www.cbr.ru/scripts/XML_News.asp')

update_query._start_initialization()
