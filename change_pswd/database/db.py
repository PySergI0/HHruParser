import mysql.connector

def connect_db():
    cnx = mysql.connector.connect(user='root', password='ASASasas111', host='localhost', database='my_database',)
    cursor = cnx.cursor()
    yield cursor
    cnx.close()
    
# cursor.execute("CREATE DATABASE my_database")
# cursor.execute("CREATE TABLE accounts (login VARCHAR(255))")
# cursor.execute("ALTER TABLE accounts ADD (password VARCHAR(255))")
# cursor.execute("ALTER TABLE accounts ADD (validity_period DATE)")
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#   print(x)