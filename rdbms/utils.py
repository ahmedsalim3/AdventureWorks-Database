import sqlite3

def table_info(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"{table_name}:")
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for column in columns:
            print(column)
        print("\n")

    conn.close()

sqlite_file = 'adventureworks.db'
table_info(sqlite_file)
