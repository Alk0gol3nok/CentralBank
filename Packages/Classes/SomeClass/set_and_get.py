class some_setters_and_getters:
    def __init__(self, start_day, start_month, start_year, end_day, end_month, end_year, query_string):
        self._set_start_day(start_day)
        self._set_start_month(start_month)
        self._set_start_year(start_year)
        self._set_end_day(end_day)
        self._set_end_month(end_month)
        self._set_end_year(end_year)
        self._set_query_string(query_string)

    # Сеттеры
    def _set_start_day(self, start_day):
        self._start_day = start_day

    def _set_start_month(self, start_month):
        self._start_month = start_month

    def _set_start_year(self, start_year):
        self._start_year = start_year

    def _set_end_day(self, end_day):
        self._end_day = end_day

    def _set_end_month(self, end_month):
        self._end_month = end_month

    def _set_end_year(self, end_year):
        self._end_year = end_year

    def _set_query_string(self, query_string):
        self._query_string = query_string

    # Геттеры
    def _get_start_day(self):
        return self._start_day

    def _get_start_month(self):
        return self._start_month

    def _get_start_year(self):
        return self._start_year

    def _get_end_day(self):
        return self._end_day

    def _get_end_month(self):
        return self._end_month

    def _get_end_year(self):
        return self._end_year

    def _get_query_string(self):
        return self._query_string
