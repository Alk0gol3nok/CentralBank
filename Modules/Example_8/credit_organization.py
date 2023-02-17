from Packages.Classes.SoloClass.solo_reason import solo_general_structure


class name_matching(solo_general_structure):
    def __init__(self, table_name, field_list, query_string):
        super().__init__(table_name, field_list, query_string)

    def _start_initialization(self):
        super()._finish_string()
        self._collection_of_dates(self.xml_structure)

    def _collection_of_dates(self, xml_structure):
        date_list = []
        for tag in xml_structure:
            date_list.append(str(tag.attrib['DU']))

        self._loading_structure(xml_structure, date_list)

    def _loading_structure(self, xml_structure, date_list):
        intermediate_list = []
        general_list = []
        index_structure = 0
        index_elem = 0

        while index_structure < len(xml_structure):
            for elem in xml_structure[index_structure]:
                intermediate_list.append(elem.text)
            index_structure += 1

            intermediate_list.append(date_list[index_elem])
            general_list.append(intermediate_list)
            intermediate_list = []
            index_elem += 1

        super()._sql_request(general_list)


update_query = name_matching(table_name='Example_eight', field_list=['ShortName', 'Bic', 'DateCreate'],
                             query_string='https://www.cbr.ru/scripts/XML_bic.asp?')

update_query._start_initialization()
