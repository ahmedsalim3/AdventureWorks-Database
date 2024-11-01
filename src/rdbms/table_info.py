import sqlite3
from src.config import DATABASE_DIR


def table_info(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")

        # Get column information
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        print("Columns:")
        
        primary_keys = []  # Initialize primary keys list
        for column in columns:
            print(f"  {column[1]}: {column[2]} (Nullable: {column[3]})")
            if column[5] == 1:  # Check if this column is a primary key
                primary_keys.append(column[1])  # Append the column name

        print("Primary Keys:", primary_keys if primary_keys else "None")

        # Get foreign key information
        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        foreign_keys = cursor.fetchall()
        print("Foreign Keys:")
        for fk in foreign_keys:
            print(f"  {fk[3]} references {fk[2]}({fk[4]})")
        
        print("\n")

    conn.close()


table_info(DATABASE_DIR)
