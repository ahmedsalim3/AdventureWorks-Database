# Define the prompt for Gemini model, based on the database structure
prompt = [
    """
    ## Database Structure Overview:\n
    The AdventureWorks database is designed to manage retail operations and contains the following tables:
    1. 'calendar':
       - Columns: OrderDate (DATE)
       - Primary Key: OrderDate

    2. 'customers':
       - Columns: CustomerKey (INT), Prefix (VARCHAR), FirstName (VARCHAR), LastName (VARCHAR), BirthDate (DATE), MaritalStatus (VARCHAR), Gender (VARCHAR), TotalChildren (INT), EducationLevel (VARCHAR), EmailAddress (VARCHAR), AnnualIncome (INT), Occupation (VARCHAR), HomeOwner (CHAR)
       - Primary Key: CustomerKey

    3. 'product_categories':
       - Columns: ProductCategoryKey (INT), CategoryName (VARCHAR)
       - Primary Key: ProductCategoryKey

    5. 'product_subcategories':
       - Columns: ProductSubcategoryKey (INT), SubcategoryName (VARCHAR), ProductCategoryKey (INT)
       - Primary Key: ProductSubcategoryKey
       - Foreign Key: ProductCategoryKey references product_categories.ProductCategoryKey

    6. 'products':
       - Columns: ProductKey (INT), ProductSubcategoryKey (INT), ProductSKU (VARCHAR), ProductName (VARCHAR), ModelName (VARCHAR), ProductDescription (VARCHAR), ProductColor (VARCHAR), ProductSize (VARCHAR), ProductStyle (VARCHAR), ProductCost (DECIMAL), ProductPrice (DECIMAL)
       - Primary Key: ProductKey
       - Foreign Key: ProductSubcategoryKey references product_subcategories.ProductSubcategoryKey

    7. 'territories':
       - Columns: TerritoryKey (INT), Region (VARCHAR), Country (VARCHAR), Continent (VARCHAR)
       - Primary Key: TerritoryKey

    8. 'returns':
       - Columns: ReturnDate (DATE), TerritoryKey (INT), ProductKey (INT), ReturnQuantity (INT)
       - Foreign Keys: ProductKey references products.ProductKey, TerritoryKey references territories.TerritoryKey

    9. 'sales_2015':
       - Columns: OrderDate (DATE), StockDate (DATE), OrderNumber (VARCHAR), ProductKey (INT), CustomerKey (INT), TerritoryKey (INT), OrderLineItem (INT), OrderQuantity (INT)
       - Primary Key: OrderNumber
       - Foreign Keys: ProductKey references products.ProductKey, CustomerKey references customers.CustomerKey, TerritoryKey references territories.TerritoryKey, OrderDate references calendar.OrderDate

    10. 'sales_2016':
       - Columns: OrderDate (DATE), StockDate (DATE), OrderNumber (VARCHAR), ProductKey (INT), CustomerKey (INT), TerritoryKey (INT), OrderLineItem (INT), OrderQuantity (INT)
       - Primary Key: OrderNumber
       - Foreign Keys: ProductKey references products.ProductKey, CustomerKey references customers.CustomerKey, TerritoryKey references territories.TerritoryKey, OrderDate references calendar.OrderDate

    11. 'sales_2017':
       - Columns: OrderDate (DATE), StockDate (DATE), OrderNumber (VARCHAR), ProductKey (INT), CustomerKey (INT), TerritoryKey (INT), OrderLineItem (INT), OrderQuantity (INT)
       - Primary Key: OrderNumber
       - Foreign Keys: ProductKey references products.ProductKey, CustomerKey references customers.CustomerKey, TerritoryKey references territories.TerritoryKey, OrderDate references calendar.OrderDate

    ## IMPORTANT Notes:
    - Check the attached image to know more details about the database structure.
    - The sales data is segmented into separate tables for each year (2015, 2016, 2017).
    - Relationships between tables are established through primary and foreign keys.
    - Use SQLite-compatible date functions like `strftime('%Y', OrderDate)` for extracting the year from dates.

    ## Examples:
    1. Find the 10 cheapest products in ascending order:
    SELECT ProductName, ProductPrice FROM products ORDER BY ProductPrice ASC LIMIT 10;
    2. Calculate the average age of all customers:
    SELECT AVG((strftime('%Y', '2024-01-17') - strftime('%Y', BirthDate)) - (strftime('%m-%d', '2024-01-17') < strftime('%m-%d', BirthDate))) AS average_age FROM customers;
    3. List all customers whose annual income is less than 20,000 and who bought products in 2015:
    SELECT FirstName, LastName, AnnualIncome, ProductName, YEAR(OrderDate) AS Year FROM sales_2015 JOIN products ON sales_2015.ProductKey = products.ProductKey JOIN customers ON sales_2015.CustomerKey = customers.CustomerKey WHERE AnnualIncome < 20000;
    """
]


random_questions = [
    "Provide a breakdown of total sales quantities by region and country for each year from 2015 to 2017, from highest to lowest",
    "Provide a summary of the total number of returns by region",
    "Retrieve details of the top 5 products sold in 2017, including their key attributes such as name, cost, price, profit margin, and order date",
    "Provide the average quantity of returns per year for the years 2015, 2016, and 2017",
    "Retrieve the total quantities of sales per region for the years 2015, 2016, and 2017, alongside the cumulative total across all years, sorted by the highest quantities in 2015.",
    "Provide the total number of sales for each year from 2015 to 2017",
    "Calculate the return rate (percentage) of products for each Country in 2017, ensuring that the return rate calculation is not affected by integer division. Display the total return quantity, total order quantity, and the return rate",
    "Retrieve the top 5 customers by their total purchases across all years, including their first name, last name, age, total purchases, and country",
    "Provide the average age of customers as of today in 2024.",
    "Provide the first name, last name, annual income, and product name for customers with an annual income of less than $20,000 in 2015, including the year of the order",
    "Show me the details of 5 products sold in 2017, including their key attributes such as name, cost, price, profit margin, and order date",
    "Retrieve the order number, product key, customer key, order date (day, month, year), and sales amount for all orders in 2015, ordered by sales amount in ascending order",
    "Identify the most popular product subcategory based on the number of orders in 2015.",
    "List all customers who own a home and have an annual income above $50,000.",
    "List the top 3 occupations of customers based on the number of orders placed in 2015.",
    "Determine the percentage of male and female customers who made purchases in 2015, 2016 and 2017.",
    "Identify the territory with the lowest sales revenue in 2015.",
    "List the names of customers who have more than two children and made a purchase in 2015.",
    "Group the customers by their education level, show their details too.",
    "أظهر لي تفاصيل 5 منتجات تم بيعها في عام 2017، بما في ذلك سماتها الرئيسية مثل الاسم والتكلفة والسعر وهامش الربح وتاريخ الطلب",
    "أرجو تزويدي بملخص عن العدد الإجمالي للإرجاعات حسب المنطقة",
    "Fournir un résumé du nombre total de retours par région.",
    "Identifier la sous-catégorie de produit la plus populaire en fonction du nombre de commandes en 2015.",
    "Muéstrame los detalles de 5 productos vendidos en 2017, incluyendo sus atributos clave como nombre, costo, precio, margen de beneficio y fecha de pedido.",
    # Add more questions as needed
]

schema_info = (
    """Only use the following tables:

    CREATE TABLE calendar (
        "OrderDate" DATE NOT NULL, 
        PRIMARY KEY ("OrderDate")
    )

    /*
    3 rows from calendar table:
    OrderDate
    2015-01-01
    2015-01-02
    2015-01-03
    */


    CREATE TABLE customers (
        "CustomerKey" INTEGER NOT NULL, 
        "Prefix" VARCHAR(100) NOT NULL, 
        "FirstName" VARCHAR(100) NOT NULL, 
        "LastName" VARCHAR(100) NOT NULL, 
        "BirthDate" DATE NOT NULL, 
        "MaritalStatus" VARCHAR(100) NOT NULL, 
        "Gender" VARCHAR(100) NOT NULL, 
        "EmailAddress" VARCHAR(100) NOT NULL, 
        "AnnualIncome" INTEGER NOT NULL, 
        "TotalChildren" INTEGER NOT NULL, 
        "EducationLevel" VARCHAR(100) NOT NULL, 
        "Occupation" VARCHAR(100) NOT NULL, 
        "HomeOwner" VARCHAR(100) NOT NULL, 
        PRIMARY KEY ("CustomerKey")
    )

    /*
    3 rows from customers table:
    CustomerKey	Prefix	FirstName	LastName	BirthDate	MaritalStatus	Gender	EmailAddress	AnnualIncome	TotalChildren	EducationLevel	Occupation	HomeOwner
    11000	MR.	JON	YANG	1966-04-08	M	M	jon24@adventure-works.com	90000	2	Bachelors	Professional	Y
    11001	MR.	EUGENE	HUANG	1965-05-14	S	M	eugene10@adventure-works.com	60000	3	Bachelors	Professional	N
    11002	MR.	RUBEN	TORRES	1965-08-12	M	M	ruben35@adventure-works.com	60000	3	Bachelors	Professional	Y
    */


    CREATE TABLE product_categories (
        "ProductCategoryKey" INTEGER NOT NULL, 
        "CategoryName" VARCHAR(100) DEFAULT NULL, 
        PRIMARY KEY ("ProductCategoryKey")
    )

    /*
    3 rows from product_categories table:
    ProductCategoryKey	CategoryName
    1	Bikes
    2	Components
    3	Clothing
    */


    CREATE TABLE product_subcategories (
        "ProductSubcategoryKey" INTEGER NOT NULL, 
        "SubcategoryName" VARCHAR(100) DEFAULT NULL, 
        "ProductCategoryKey" INTEGER DEFAULT NULL, 
        PRIMARY KEY ("ProductSubcategoryKey"), 
        FOREIGN KEY("ProductCategoryKey") REFERENCES product_categories ("ProductCategoryKey")
    )

    /*
    3 rows from product_subcategories table:
    ProductSubcategoryKey	SubcategoryName	ProductCategoryKey
    1	Mountain Bikes	1
    2	Road Bikes	1
    3	Touring Bikes	1
    */


    CREATE TABLE products (
        "ProductKey" INTEGER NOT NULL, 
        "ProductSubcategoryKey" INTEGER DEFAULT NULL, 
        "ProductSKU" VARCHAR(100) NOT NULL, 
        "ProductName" VARCHAR(100) NOT NULL, 
        "ModelName" VARCHAR(100) NOT NULL, 
        "ProductDescription" VARCHAR(250) NOT NULL, 
        "ProductColor" VARCHAR(100) NOT NULL, 
        "ProductSize" VARCHAR(100) NOT NULL, 
        "ProductStyle" VARCHAR(100) NOT NULL, 
        "ProductCost" DECIMAL(10, 4) NOT NULL, 
        "ProductPrice" DECIMAL(10, 4) NOT NULL, 
        PRIMARY KEY ("ProductKey"), 
        FOREIGN KEY("ProductSubcategoryKey") REFERENCES product_subcategories ("ProductSubcategoryKey")
    )

    /*
    3 rows from products table:
    ProductKey	ProductSubcategoryKey	ProductSKU	ProductName	ModelName	ProductDescription	ProductColor	ProductSize	ProductStyle	ProductCost	ProductPrice
    214	31	HL-U509-R	\"Sport-100 Helmet, Red\"	Sport-100	\"Universal fit, well-vented, lightweight , snap-on visor.\"	Red	0	0	13.0863	34.9900
    215	31	HL-U509	\"Sport-100 Helmet, Black\"	Sport-100	\"Universal fit, well-vented, lightweight , snap-on visor.\"	Black	0	0	12.0278	33.6442
    218	23	SO-B909-M	\"Mountain Bike Socks, M\"	Mountain Bike Socks	Combination of natural and synthetic fibers stays dry and provides just the right cushioning.	White	M	U	3.3963	9.5000
    */


    CREATE TABLE returns (
        "ReturnDate" DATE NOT NULL, 
        "TerritoryKey" INTEGER NOT NULL, 
        "ProductKey" INTEGER NOT NULL, 
        "ReturnQuantity" INTEGER NOT NULL, 
        FOREIGN KEY("TerritoryKey") REFERENCES territories ("TerritoryKey"), 
        FOREIGN KEY("ProductKey") REFERENCES products ("ProductKey")
    )

    /*
    3 rows from returns table:
    ReturnDate	TerritoryKey	ProductKey	ReturnQuantity
    2015-01-18	9	312	1
    2015-01-18	10	310	1
    2015-01-21	8	346	1
    */


    CREATE TABLE sales_2015 (
        "OrderDate" DATE NOT NULL, 
        "StockDate" DATE NOT NULL, 
        "OrderNumber" VARCHAR(100) NOT NULL, 
        "ProductKey" INTEGER NOT NULL, 
        "CustomerKey" INTEGER NOT NULL, 
        "TerritoryKey" INTEGER NOT NULL, 
        "OrderLineItem" INTEGER NOT NULL, 
        "OrderQuantity" INTEGER NOT NULL, 
        PRIMARY KEY ("OrderNumber"), 
        FOREIGN KEY("OrderDate") REFERENCES calendar ("OrderDate"), 
        FOREIGN KEY("TerritoryKey") REFERENCES territories ("TerritoryKey"), 
        FOREIGN KEY("CustomerKey") REFERENCES customers ("CustomerKey"), 
        FOREIGN KEY("ProductKey") REFERENCES products ("ProductKey")
    )

    /*
    3 rows from sales_2015 table:
    OrderDate	StockDate	OrderNumber	ProductKey	CustomerKey	TerritoryKey	OrderLineItem	OrderQuantity
    2015-01-01	2001-09-21	SO2015-1	332	14657	1	1	1
    2015-01-03	2001-09-29	SO2015-10	310	29170	4	1	1
    2015-01-17	2001-10-23	SO2015-100	313	29238	4	1	1
    */


    CREATE TABLE sales_2016 (
        "OrderDate" DATE NOT NULL, 
        "StockDate" DATE NOT NULL, 
        "OrderNumber" VARCHAR(100) NOT NULL, 
        "ProductKey" INTEGER NOT NULL, 
        "CustomerKey" INTEGER NOT NULL, 
        "TerritoryKey" INTEGER NOT NULL, 
        "OrderLineItem" INTEGER NOT NULL, 
        "OrderQuantity" INTEGER NOT NULL, 
        PRIMARY KEY ("OrderNumber"), 
        FOREIGN KEY("OrderDate") REFERENCES calendar ("OrderDate"), 
        FOREIGN KEY("TerritoryKey") REFERENCES territories ("TerritoryKey"), 
        FOREIGN KEY("CustomerKey") REFERENCES customers ("CustomerKey"), 
        FOREIGN KEY("ProductKey") REFERENCES products ("ProductKey")
    )

    /*
    3 rows from sales_2016 table:
    OrderDate	StockDate	OrderNumber	ProductKey	CustomerKey	TerritoryKey	OrderLineItem	OrderQuantity
    2016-01-01	2002-10-17	SO2016-1	385	14335	1	1	1
    2016-01-02	2002-09-12	SO2016-10	360	13647	9	1	1
    2016-01-13	2002-09-25	SO2016-100	373	17632	10	1	1
    */


    CREATE TABLE sales_2017 (
        "OrderDate" DATE NOT NULL, 
        "StockDate" DATE NOT NULL, 
        "OrderNumber" VARCHAR(100) NOT NULL, 
        "ProductKey" INTEGER NOT NULL, 
        "CustomerKey" INTEGER NOT NULL, 
        "TerritoryKey" INTEGER NOT NULL, 
        "OrderLineItem" INTEGER NOT NULL, 
        "OrderQuantity" INTEGER NOT NULL, 
        PRIMARY KEY ("OrderNumber"), 
        FOREIGN KEY("OrderDate") REFERENCES calendar ("OrderDate"), 
        FOREIGN KEY("TerritoryKey") REFERENCES territories ("TerritoryKey"), 
        FOREIGN KEY("CustomerKey") REFERENCES customers ("CustomerKey"), 
        FOREIGN KEY("ProductKey") REFERENCES products ("ProductKey")
    )

    /*
    3 rows from sales_2017 table:
    OrderDate	StockDate	OrderNumber	ProductKey	CustomerKey	TerritoryKey	OrderLineItem	OrderQuantity
    2017-01-01	2003-12-13	SO2017-1	529	23791	1	2	2
    2017-01-01	2003-09-27	SO2017-10	536	11530	6	1	2
    2017-01-02	2003-09-08	SO2017-100	479	11099	9	3	1
    */


    CREATE TABLE territories (
        "TerritoryKey" INTEGER NOT NULL, 
        "Region" VARCHAR(100) DEFAULT NULL, 
        "Country" VARCHAR(100) DEFAULT NULL, 
        "Continent" VARCHAR(100) DEFAULT NULL, 
        PRIMARY KEY ("TerritoryKey")
    )

    /*
    3 rows from territories table:
    TerritoryKey	Region	Country	Continent
    1	Northwest	United States	North America
    2	Northeast	United States	North America
    3	Central	United States	North America
    */"""
)