from quote_for_today import quote_today

update_query = quote_today(day=2, month=3, year=2002)

while True:
    update_query._start_initialization()