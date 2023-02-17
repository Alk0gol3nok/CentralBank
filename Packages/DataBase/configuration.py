import pyodbc

connection_to_db = pyodbc.connect(r'Driver={SQL Server};'
                                  r'Server=DESKTOP-NS3AHBI\SQLEXPRESS;'
                                  r'DataBase=CentralBank;'
                                  r'Trusted_Connection=yes;')
cursor = connection_to_db.cursor()