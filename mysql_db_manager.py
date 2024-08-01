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
            password=self.db_config["password"]
        )
        cursor = conn.cursor()

        with open(script_path, 'r') as file:
            sql_script = file.read()
        
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        print("SQL script executed successfully")
        cursor.close()
        conn.close()

    def Importer(self, csv_file_path, table_name):

        conn = MySQLdb.connect(
            host=self.db_config.get("host"),
            user=self.db_config.get("user"),
            password=self.db_config.get("password"),
            database=self.db_config.get("database")
        )
        cursor = conn.cursor()

        with open(csv_file_path, 'r') as csv_file:
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
        print(f'Done importing {csv_file_path}')
        cursor.close()
        conn.close()
        
# Example usage
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root1976519",
    "database": "adventureworks"
}

db_manager = MySQLDatabaseManager(db_config)
db_manager.Setup('create_schema.sql')
db_manager.Importer('dataset/AdventureWorks_Customers.csv', 'customers')
db_manager.Importer('dataset/AdventureWorks_Calendar.csv', 'calendar')
db_manager.Importer('dataset/AdventureWorks_Product_Categories.csv', 'product_categories')
db_manager.Importer('dataset/AdventureWorks_Product_Subcategories.csv', 'product_subcategories')
db_manager.Importer('dataset/AdventureWorks_Products.csv', 'products')
db_manager.Importer('dataset/AdventureWorks_Territories.csv', 'territories')
db_manager.Importer('dataset/AdventureWorks_Returns.csv', 'returns')
db_manager.Importer('dataset/AdventureWorks_Sales_2015.csv', 'sales_2015')
db_manager.Importer('dataset/AdventureWorks_Sales_2016.csv', 'sales_2016')
db_manager.Importer('dataset/AdventureWorks_Sales_2017.csv', 'sales_2017')



