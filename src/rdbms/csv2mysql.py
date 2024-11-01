from tqdm import tqdm
import csv
import MySQLdb

class MySQLDatabaseManager:
    def __init__(self, db_config):
        self.db_config = db_config

    def Setup(self, script_path):
        """
        Executes an SQL script to set up the database and tables
        """
        conn = MySQLdb.connect(
            host=self.db_config["host"],
            user=self.db_config["user"],
            password=self.db_config["password"],
            port=self.db_config.get("port", 3306)
        )
        cursor = conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {self.db_config['database']}")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config['database']}")
        cursor.execute(f"USE {self.db_config['database']}")

        with open(script_path, 'r') as file:
            sql_script = file.read()
        
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        print(f"{db_config['database']} Database schema was setup successfully!")
        cursor.close()
        conn.close()

    def Importer(self, csv_file_path, table_name):

        conn = MySQLdb.connect(
            host=self.db_config.get("host"),
            user=self.db_config.get("user"),
            password=self.db_config.get("password"),
            database=self.db_config.get("database"),
            port=self.db_config.get("port", 3306)
        )
        cursor = conn.cursor()

        with open(csv_file_path, 'r', encoding='ISO-8859-1') as csv_file:
            csv_data = csv.DictReader(csv_file)
            columns = csv_data.fieldnames
            column_placeholders = ', '.join(['%s'] * len(columns))

            sql = f"""
            INSERT INTO {table_name} ({', '.join(columns)})
            VALUES ({column_placeholders})
            """

            print(f'Importing the CSV file: {csv_file_path}')

            for row in tqdm(csv_data):
                values = [row.get(column) for column in columns]
                cursor.execute(sql, values)

        conn.commit()
        cursor.close()
        conn.close()
        
        
if __name__ == "__main__":
    db_config = {
        "host": "xxx.x.x.x",
        "user": "xxxx",
        "password": "xxxx",
        "database": "test",
        "port": 0000
    }

    db_manager = MySQLDatabaseManager(db_config)
    db_manager.Setup('schema.sql')
    pwd = '../'
    db_manager.Importer(pwd + 'data/AdventureWorks_Customers.csv', 'customers')
    db_manager.Importer(pwd + 'data/AdventureWorks_Calendar.csv', 'calendar')
    db_manager.Importer(pwd + 'data/AdventureWorks_Product_Categories.csv', 'product_categories')
    db_manager.Importer(pwd + 'data/AdventureWorks_Product_Subcategories.csv', 'product_subcategories')
    db_manager.Importer(pwd + 'data/AdventureWorks_Products.csv', 'products')
    db_manager.Importer(pwd + 'data/AdventureWorks_Territories.csv', 'territories')
    db_manager.Importer(pwd + 'data/AdventureWorks_Returns.csv', 'returns')
    db_manager.Importer(pwd + 'data/AdventureWorks_Sales_2015.csv', 'sales_2015')
    db_manager.Importer(pwd + 'data/AdventureWorks_Sales_2016.csv', 'sales_2016')
    db_manager.Importer(pwd + 'data/AdventureWorks_Sales_2017.csv', 'sales_2017')



