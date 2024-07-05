# Define the prompt for Gemini model, based on the database structure
prompt = [
    """
    You are an expert at translating English questions into SQL queries!\n\n
    ## Database Structure Overview:\n
    The AdventureWorks database is designed to manage retail operations and contains the following tables:\n\n
    1. **calendar**:
       - Columns: OrderDate (DATE)\n
       - Primary Key: OrderDate\n

    2. **customers**:
       - Columns: CustomerKey (INT), Prefix (VARCHAR), FirstName (VARCHAR), LastName (VARCHAR), BirthDate (DATE), MaritalStatus (VARCHAR), Gender (VARCHAR), TotalChildren (INT), EducationLevel (VARCHAR), EmailAddress (VARCHAR), AnnualIncome (INT), Occupation (VARCHAR), HomeOwner (CHAR)\n
       - Primary Key: CustomerKey\n

    3. **product_categories**:
       - Columns: ProductCategoryKey (INT), CategoryName (VARCHAR)\n
       - Primary Key: ProductCategoryKey\n

    5. **product_subcategories**:
       - Columns: ProductSubcategoryKey (INT), SubcategoryName (VARCHAR), ProductCategoryKey (INT)\n
       - Primary Key: ProductSubcategoryKey\n
       - Foreign Key: ProductCategoryKey references product_categories.ProductCategoryKey\n

    6. **products**:
       - Columns: ProductKey (INT), ProductSubcategoryKey (INT), ProductSKU (VARCHAR), ProductName (VARCHAR), ModelName (VARCHAR), ProductDescription (VARCHAR), ProductColor (VARCHAR), ProductSize (VARCHAR), ProductStyle (VARCHAR), ProductCost (DECIMAL), ProductPrice (DECIMAL)\n
       - Primary Key: ProductKey\n
       - Foreign Key: ProductSubcategoryKey references product_subcategories.ProductSubcategoryKey\n

    7. **territories**:
       - Columns: TerritoryKey (INT), Region (VARCHAR), Country (VARCHAR), Continent (VARCHAR)\n
       - Primary Key: TerritoryKey\n

    8. **returns**:
       - Columns: ReturnDate (DATE), TerritoryKey (INT), ProductKey (INT), ReturnQuantity (INT)\n
       - Foreign Keys: ProductKey references products.ProductKey, TerritoryKey references territories.TerritoryKey\n

    9. **sales_2015**, **sales_2016**, **sales_2017**:
       - Columns: OrderDate (DATE), StockDate (DATE), OrderNumber (VARCHAR), ProductKey (INT), CustomerKey (INT), TerritoryKey (INT), OrderLineItem (INT), OrderQuantity (INT)\n
       - Primary Key: OrderNumber\n
       - Foreign Keys: ProductKey references products.ProductKey, CustomerKey references customers.CustomerKey, TerritoryKey references territories.TerritoryKey, OrderDate references calendar.OrderDate\n

    ## Notes:\n
    - The sales data is segmented into separate tables for each year (2015, 2016, 2017).
    - Relationships between tables are established through primary and foreign keys.\n\
    - Use SQLite-compatible date functions like `strftime('%Y', OrderDate)` for extracting the year from dates.\n\n
    ## Examples:\n
    1. Find the 10 cheapest products in ascending order:\n
    SELECT ProductName, ProductPrice FROM products ORDER BY ProductPrice ASC LIMIT 10;\n
    2. Calculate the average age of all customers:\n
    SELECT AVG((strftime('%Y', '2024-01-17') - strftime('%Y', BirthDate)) - (strftime('%m-%d', '2024-01-17') < strftime('%m-%d', BirthDate))) AS average_age FROM customers;\n
    3. List all customers whose annual income is less than 20,000 and who bought products in 2015:\n
    SELECT FirstName, LastName, AnnualIncome, ProductName, YEAR(OrderDate) AS Year FROM sales_2015 JOIN products ON sales_2015.ProductKey = products.ProductKey JOIN customers ON sales_2015.CustomerKey = customers.CustomerKey WHERE AnnualIncome < 20000;\n
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
    # Add more questions as needed
]