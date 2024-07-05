import sqlite3

def import_sql_file(sqlite_file, sql_file):
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()

    with open(sql_file, 'r', encoding='utf-8') as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)

    conn.commit()
    conn.close()
    print("DATABASE available at", sqlite_file)

if __name__ == '__main__':
    sqlite_file = 'adventureworks.db'
    sql_file = 'adventureworks_schema.sql'

    import_sql_file(sqlite_file, sql_file)