from Packages.Classes.SomeClass.set_and_get import some_setters_and_getters
from Packages.Parser import library
from Packages.DataBase import configuration


class some_general_structure(some_setters_and_getters):
    def __init__(self, day_start, month_start, year_start, day_end, month_end, year_end, query_string):
        super().__init__(day_start, month_start, year_start, day_end, month_end, year_end, query_string)

    def _start_initialization(self):
        start_day = self._get_start_day()
        start_month = self._get_start_month()
        start_year = self._get_start_year()
        end_day = self._get_end_day()
        end_month = self._get_end_month()
        end_year = self._get_end_year()

        self.init_dict = {'start_day': start_day, 'start_month': start_month, 'start_year': start_year,
                          'end_day': end_day, 'end_month': end_month, 'end_year': end_year}

    def _transformation(self, init_dict):
        start_dict_data = self._rebuild_start_date(init_dict['start_day'],
                                                   init_dict['start_month'],
                                                   init_dict['start_year'])

        end_dict_data = self._rebuild_end_date(init_dict['end_day'],
                                               init_dict['end_month'],
                                               init_dict['end_year'])

        self._preparation_for_request(start_dict_data, end_dict_data)

    @staticmethod
    def _rebuild_start_date(start_day, start_month, start_year):
        if int(start_day) < 10:
            start_day = ('0%s' % start_day)
        else:
            start_day = (str(start_day))
        if int(start_month) < 10:
            start_month = ('0%s' % start_month)
        else:
            start_month = (str(start_month))

        return {'start_day': start_day, 'start_month': start_month, 'start_year': start_year}

    @staticmethod
    def _rebuild_end_date(end_day, end_month, end_year):
        if int(end_day) < 10:
            end_day = ('0%s' % end_day)
        else:
            end_day = (str(end_day))
        if int(end_month) < 10:
            end_month = ('0%s' % end_month)
        else:
            end_month = (str(end_month))

        return {'end_day': end_day, 'end_month': end_month, 'end_year': end_year}

    def _preparation_for_request(self, start_dict_data, end_dict_data):

        for key in start_dict_data:
            self._set_query_string(self._get_query_string().replace('%s', str(start_dict_data[key]), 1))

        for key in end_dict_data:
            self._set_query_string(self._get_query_string().replace('%s', str(end_dict_data[key]), 1))

    def _finish_string(self):
        self.xml_structure = (library.ET.fromstring(library.requests.get(self._get_query_string()).content))

    @staticmethod
    def _accept_sql(general_list, sql_insert_param):
        for sheet in general_list:
            configuration.cursor.execute(sql_insert_param, sheet)
            configuration.cursor.commit()
            configuration.connection_to_db.commit()
        return print('Data uploaded successfully')
