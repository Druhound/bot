from PSQL.main import *

"""
PSQL file

@connect_database(database, user, host, password)
@commit_changes(connect)
@cursor(connect)
@cursor_close(cursor)

@create_table(cursor, table, tuple)
@update_table(cursor, table, dict, where)
@drop_table(cursor, table)

@create_seq(cursor, name, table='temp_')
@drop_seq(cursor, seq)

@select_all(cursor, name)

"""


connect = connect_database('bot_db', 'bot_user', 'localhost', 'thvfred65tgjuik')
cursor = cursor(connect)

table = "temp"
sequence = "temp_id_seq"
tuple = ("id integer DEFAULT nextval('temp_id_seq') NOT NULL, ", "content TEXT")
dictionary = {'content': "'text'"}
where = {'id': 1}
IF = ">="

create_seq(cursor, 'id', table)
create_table(cursor, table, tuple)
update_table(cursor, table, dictionary, where, IF)
select_all(cursor, table)
select_all(cursor, sequence)
commit_changes(connect)

# drop_table(cursor, "temp")
# drop_seq(cursor, 'temp_id_seq')

# commit_changes(connect)

cursor_close(cursor)

