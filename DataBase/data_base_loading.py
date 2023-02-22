from Packages.DataBase import configuration


class db_loader:
    example_one_list = []

    configuration.cursor.execute('Select * from Example_one')

    for elem in configuration.cursor:
        example_one_list.append(elem[1:])
