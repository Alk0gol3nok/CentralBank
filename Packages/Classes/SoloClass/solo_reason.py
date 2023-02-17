from Packages.Classes.SoloClass.set_and_get import solo_setters_and_getters
from Packages.Parser import library
from Packages.DataBase import configuration


class solo_general_structure(solo_setters_and_getters):
    def __init__(self, table_name, field_list, query_string):
        super().__init__(table_name, field_list, query_string)

    def _finish_string(self):
        self.xml_structure = (library.ET.fromstring(library.requests.get(self._get_query_string()).content))

    def _sql_request(self, general_list):
        sql_insert_param = ('insert into ' +
                            self._get_table_name() + ' (' +
                            self._get_field_list()[0] + ', ' +
                            self._get_field_list()[1] + ', ' +
                            self._get_field_list()[2] + ') ' +
                            'values (?, ?, ?)')

        self._accept_sql(general_list, sql_insert_param)

    @staticmethod
    def _accept_sql(general_list, sql_insert_param):
        for sheet in general_list:
            configuration.cursor.execute(sql_insert_param, sheet)
            configuration.cursor.commit()
            configuration.connection_to_db.commit()
        return print('Data uploaded successfully')
