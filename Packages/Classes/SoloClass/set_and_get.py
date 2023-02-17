class solo_setters_and_getters:
    def __init__(self, table_name, field_list, query_string):
        self._set_query_string(query_string)
        self._set_table_name(table_name)
        self._set_field_list(field_list)

    # Сеттеры
    def _set_query_string(self, query_string):
        self._query_string = query_string

    def _set_table_name(self, table_name):
        self._table_name = table_name

    def _set_field_list(self, field_list):
        self._field_list = field_list

    # Геттеры
    def _get_query_string(self):
        return self._query_string

    def _get_table_name(self):
        return self._table_name

    def _get_field_list(self):
        return self._field_list
