TABLES = [
    'calendar',
    'customers',
    'product_categories',
    'product_subcategories',
    'products',
    'returns',
    'sales_2015',
    'sales_2016',
    'sales_2017',
    'territories',
]

SENTENCES = [
    'The calendar table stores unique order dates, serving as a reference for tracking sales and events.',
    'The customers table contains detailed information about each customer, including personal details, demographics, and financial status.',
    'The product_categories table classifies products into categories, allowing for organized product management and reporting.',
    'The product_subcategories table further refines product classifications by linking subcategories to their respective categories.',
    'The products table holds detailed information about each product, including specifications, pricing, and category associations.',
    'The returns table records product returns, including details about the returned items, quantities, and associated territories.',
    'The sales_2015 table tracks sales transactions for the year 2015, capturing essential details about orders, products, and customers.',
    'The sales_2016 table documents sales transactions for 2016, providing insights into customer purchases and product performance.',
    'The sales_2017 table captures sales data for the year 2017, enabling analysis of trends and customer behavior over time.',
    'The territories table defines geographical regions where sales occur, offering context for sales data and customer distribution.',
]

SCHEMAS = [
    """
    CREATE TABLE `calendar` (
    `OrderDate` date NOT NULL,
    PRIMARY KEY (`OrderDate`)
    )""",
    """CREATE TABLE `customers` (
    `CustomerKey` int NOT NULL,
    `Prefix` varchar(100) NOT NULL,
    `FirstName` varchar(100) NOT NULL,
    `LastName` varchar(100) NOT NULL,
    `BirthDate` date NOT NULL,
    `MaritalStatus` varchar(100) NOT NULL,
    `Gender` varchar(100) NOT NULL,
    `EmailAddress` varchar(100) NOT NULL,
    `AnnualIncome` int NOT NULL,
    `TotalChildren` int NOT NULL,
    `EducationLevel` varchar(100) NOT NULL,
    `Occupation` varchar(100) NOT NULL,
    `HomeOwner` varchar(100) NOT NULL,
    PRIMARY KEY (`CustomerKey`)
    )""",
    """CREATE TABLE `product_categories` (
    `ProductCategoryKey` int NOT NULL,
    `CategoryName` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`ProductCategoryKey`)
    )""",
    """CREATE TABLE `product_subcategories` (
    `ProductSubcategoryKey` int NOT NULL,
    `SubcategoryName` varchar(100) DEFAULT NULL,
    `ProductCategoryKey` int DEFAULT NULL,
    PRIMARY KEY (`ProductSubcategoryKey`),
    FOREIGN KEY (`ProductCategoryKey`) REFERENCES `product_categories` (`ProductCategoryKey`)
    )""",
    """CREATE TABLE `products` (
    `ProductKey` int NOT NULL,
    `ProductSubcategoryKey` int DEFAULT NULL,
    `ProductSKU` varchar(100) NOT NULL,
    `ProductName` varchar(100) NOT NULL,
    `ModelName` varchar(100) NOT NULL,
    `ProductDescription` varchar(250) NOT NULL,
    `ProductColor` varchar(100) NOT NULL,
    `ProductSize` varchar(100) NOT NULL,
    `ProductStyle` varchar(100) NOT NULL,
    `ProductCost` decimal(10,4) NOT NULL,
    `ProductPrice` decimal(10,4) NOT NULL,
    PRIMARY KEY (`ProductKey`),
    FOREIGN KEY (`ProductSubcategoryKey`) REFERENCES `product_subcategories` (`ProductSubcategoryKey`)
    )""",
    """CREATE TABLE `returns` (
    `ReturnDate` date NOT NULL,
    `TerritoryKey` int NOT NULL,
    `ProductKey` int NOT NULL,
    `ReturnQuantity` int NOT NULL,
    FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
    FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`)
    )""",
    """CREATE TABLE `sales_2015` (
    `OrderDate` date NOT NULL,
    `StockDate` date NOT NULL,
    `OrderNumber` varchar(100) NOT NULL,
    `ProductKey` int NOT NULL,
    `CustomerKey` int NOT NULL,
    `TerritoryKey` int NOT NULL,
    `OrderLineItem` int NOT NULL,
    `OrderQuantity` int NOT NULL,
    PRIMARY KEY (`OrderNumber`),
    FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
    FOREIGN KEY (`CustomerKey`) REFERENCES `customers` (`CustomerKey`),
    FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`),
    FOREIGN KEY (`OrderDate`) REFERENCES `calendar` (`OrderDate`)
    )""",
    """CREATE TABLE `sales_2016` (
    `OrderDate` date NOT NULL,
    `StockDate` date NOT NULL,
    `OrderNumber` varchar(100) NOT NULL,
    `ProductKey` int NOT NULL,
    `CustomerKey` int NOT NULL,
    `TerritoryKey` int NOT NULL,
    `OrderLineItem` int NOT NULL,
    `OrderQuantity` int NOT NULL,
    PRIMARY KEY (`OrderNumber`),
    FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
    FOREIGN KEY (`CustomerKey`) REFERENCES `customers` (`CustomerKey`),
    FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`),
    FOREIGN KEY (`OrderDate`) REFERENCES `calendar` (`OrderDate`)
    )""",
    """CREATE TABLE `sales_2017` (
    `OrderDate` date NOT NULL,
    `StockDate` date NOT NULL,
    `OrderNumber` varchar(100) NOT NULL,
    `ProductKey` int NOT NULL,
    `CustomerKey` int NOT NULL,
    `TerritoryKey` int NOT NULL,
    `OrderLineItem` int NOT NULL,
    `OrderQuantity` int NOT NULL,
    PRIMARY KEY (`OrderNumber`),
    FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
    FOREIGN KEY (`CustomerKey`) REFERENCES `customers` (`CustomerKey`),
    FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`),
    FOREIGN KEY (`OrderDate`) REFERENCES `calendar` (`OrderDate`)
    )""",
    """CREATE TABLE `territories` (
    `TerritoryKey` int NOT NULL,
    `Region` varchar(100) DEFAULT NULL,
    `Country` varchar(100) DEFAULT NULL,
    `Continent` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`TerritoryKey`)
    )"""
]