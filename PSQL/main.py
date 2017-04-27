import psycopg2
import csv

"""
START DATABASE
"""


def connect_database(database, user, host, password):
    connect = psycopg2.connect(
        database=database,  # 'bot_db'
        user=user,  # 'bot_user'
        host=host,  # 'localhost'
        password=password)  # 'thvfred65tgjuik'
    return connect


def cursor(connect):
    return connect.cursor()


def cursor_close(cursor):
    cursor.close()
    print("### CURSOR CLOSE ###\n")


"""
END DATABASE
"""

"""
START TABLE
"""


def create_table(cursor, table, tuple):
    SQL = ""
    for item in tuple:
        SQL += item
    cursor.execute("CREATE TABLE IF NOT EXISTS " + table + " (id serial NOT NULL" + SQL + ")")
    print("### CREATE TABLE ###\n")


def drop_table(cursor, table):
    cursor.execute("DROP TABLE IF EXISTS " + table)
    print("### DROP TABLE ###\n")


# def insert_table_seq(cursor, table, header, values):
#     VALUE = ''
#     header = ''
#     first = True
#     cursor.execute("INSERT INTO " + table + "" + header + " VALUES " + VALUE)
#     print("### INSERT TABLE CSV ###\n")


def insert_table_CSV(cursor, table, header, values):
    VALUE = ''
    header = ''
    first = True
    for line in values:
        if first:
            VALUE += "(" + line.get('node') + ");"
            first = False
        else:
            VALUE = "(" + line.get('node') + "), " + VALUE
    cursor.execute("INSERT INTO " + table + "" + header + " VALUES " + VALUE)
    print("### INSERT TABLE CSV ###\n")


def update_table(cursor, table, dict, dict2, IF):
    SQL = ""
    where = " "
    for key in dict:
        SQL += SQL + key + " = " + str(dict[key]) + " "
    for key in dict2:
        where += where + key + IF + str(dict2[key]) + " "
    cursor.execute("UPDATE " + table + " set " + SQL + "where" + where)
    print("Total number of rows updated :", cursor.rowcount)
    print("### UPDATE TABLE ###\n")


"""
END TABLE
"""

"""
START SEQUENCE
"""


def create_seq(cursor, name, table='temp_'):
    if not table.endswith("_"):
        table += "_"
    seq = table + name + "_seq"
    cursor.execute("CREATE SEQUENCE IF NOT EXISTS " + seq)
    print("### CREATE SQUENCE ###\n")
    return seq


def drop_seq(cursor, seq):
    cursor.execute("DROP SEQUENCE IF EXISTS " + seq)
    print("### DROP SEQUENCE ###\n")


"""
END SEQUENCE
"""


def select_all(cursor, name):
    cursor.execute("SELECT * FROM " + name)
    print("### FROM * SELECT (" + name + ") ###")
    print(cursor.fetchall())
    print("### END SELECT ###\n")


def commit_changes(connect):
    connect.commit()
    print("### COMMIT CHANGES ###\n")
