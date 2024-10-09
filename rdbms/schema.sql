
/* Table structure for the calendar */
DROP TABLE IF EXISTS `calendar`;
CREATE TABLE `calendar` (
  `OrderDate` DATE NOT NULL,
  PRIMARY KEY (`OrderDate`)
);

/* Table structure for the customers */
DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `CustomerKey` INT NOT NULL,
  `Prefix` VARCHAR(100) NOT NULL,
  `FirstName` VARCHAR(100) NOT NULL,
  `LastName` VARCHAR(100) NOT NULL,
  `BirthDate` DATE NOT NULL,
  `MaritalStatus` VARCHAR(100) NOT NULL,
  `Gender` VARCHAR(100) NOT NULL,
  `EmailAddress` VARCHAR(100) NOT NULL,
  `AnnualIncome` INT NOT NULL,
  `TotalChildren` INT NOT NULL,
  `EducationLevel` VARCHAR(100) NOT NULL,
  `Occupation` VARCHAR(100) NOT NULL,
  `HomeOwner` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`CustomerKey`)
);

/* Table structure for product categories */
DROP TABLE IF EXISTS `product_categories`;
CREATE TABLE `product_categories` (
  `ProductCategoryKey` INT NOT NULL,
  `CategoryName` VARCHAR(50) DEFAULT NULL,
  PRIMARY KEY (`ProductCategoryKey`)
);

/* Table structure for product subcategories */
DROP TABLE IF EXISTS `product_subcategories`;
CREATE TABLE `product_subcategories` (
  `ProductSubcategoryKey` INT NOT NULL,
  `SubcategoryName` VARCHAR(100) NOT NULL,
  `ProductCategoryKey` INT NOT NULL,
  PRIMARY KEY (`ProductSubcategoryKey`),
  KEY `ProductCategoryKey` (`ProductCategoryKey`),
  CONSTRAINT `product_subcategories_ibfk_1` FOREIGN KEY (`ProductCategoryKey`) REFERENCES `product_categories` (`ProductCategoryKey`)
); 

/* Table structure for products */
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `ProductKey` INT NOT NULL,
  `ProductSubcategoryKey` INT NOT NULL,
  `ProductSKU` VARCHAR(100) NOT NULL,
  `ProductName` VARCHAR(100) NOT NULL,
  `ModelName` VARCHAR(100) NOT NULL,
  `ProductDescription` VARCHAR(250) NOT NULL,
  `ProductColor` VARCHAR(100) NOT NULL,
  `ProductSize` VARCHAR(100) NOT NULL,
  `ProductStyle` VARCHAR(100) NOT NULL,
  `ProductCost` DECIMAL(10,4) NOT NULL,
  `ProductPrice` DECIMAL(10,4) NOT NULL,
  PRIMARY KEY (`ProductKey`),
  KEY `ProductSubcategoryKey` (`ProductSubcategoryKey`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`ProductSubcategoryKey`) REFERENCES `product_subcategories` (`ProductSubcategoryKey`)
);

/* Table structure for territories */
DROP TABLE IF EXISTS `territories`;
CREATE TABLE `territories` (
  `TerritoryKey` INT NOT NULL,
  `Region` VARCHAR(100) NOT NULL,
  `Country` VARCHAR(100) NOT NULL,
  `Continent` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`TerritoryKey`)
);

/* Table structure for returns */
DROP TABLE IF EXISTS `returns`;
CREATE TABLE `returns` (
  `ReturnDate` DATE NOT NULL,
  `TerritoryKey` INT NOT NULL,
  `ProductKey` INT NOT NULL,
  `ReturnQuantity` INT NOT NULL,
  KEY `ProductKey` (`ProductKey`),
  KEY `TerritoryKey` (`TerritoryKey`),
  CONSTRAINT `returns_ibfk_1` FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
  CONSTRAINT `returns_ibfk_2` FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`)
);

/* Table structure for sales in 2015 */
DROP TABLE IF EXISTS `sales_2015`;
CREATE TABLE `sales_2015` (
  `OrderDate` DATE NOT NULL,
  `StockDate` DATE NOT NULL,
  `OrderNumber` VARCHAR(100) NOT NULL,
  `ProductKey` INT NOT NULL,
  `CustomerKey` INT NOT NULL,
  `TerritoryKey` INT NOT NULL,
  `OrderLineItem` INT NOT NULL,
  `OrderQuantity` INT NOT NULL,
  PRIMARY KEY (`OrderNumber`),
  KEY `ProductKey` (`ProductKey`),
  KEY `CustomerKey` (`CustomerKey`),
  KEY `TerritoryKey` (`TerritoryKey`),
  KEY `OrderDate` (`OrderDate`),
  CONSTRAINT `sales_2015_ibfk_1` FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
  CONSTRAINT `sales_2015_ibfk_2` FOREIGN KEY (`CustomerKey`) REFERENCES `customers` (`CustomerKey`),
  CONSTRAINT `sales_2015_ibfk_3` FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`),
  CONSTRAINT `sales_2015_ibfk_4` FOREIGN KEY (`OrderDate`) REFERENCES `calendar` (`OrderDate`)
);

/* Table structure for sales in 2016 */
DROP TABLE IF EXISTS `sales_2016`;
CREATE TABLE `sales_2016` (
  `OrderDate` DATE NOT NULL,
  `StockDate` DATE NOT NULL,
  `OrderNumber` VARCHAR(100) NOT NULL,
  `ProductKey` INT NOT NULL,
  `CustomerKey` INT NOT NULL,
  `TerritoryKey` INT NOT NULL,
  `OrderLineItem` INT NOT NULL,
  `OrderQuantity` INT NOT NULL,
  PRIMARY KEY (`OrderNumber`),
  KEY `ProductKey` (`ProductKey`),
  KEY `CustomerKey` (`CustomerKey`),
  KEY `TerritoryKey` (`TerritoryKey`),
  KEY `OrderDate` (`OrderDate`),
  CONSTRAINT `sales_2016_ibfk_1` FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
  CONSTRAINT `sales_2016_ibfk_2` FOREIGN KEY (`CustomerKey`) REFERENCES `customers` (`CustomerKey`),
  CONSTRAINT `sales_2016_ibfk_3` FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`),
  CONSTRAINT `sales_2016_ibfk_4` FOREIGN KEY (`OrderDate`) REFERENCES `calendar` (`OrderDate`)
);

/* Table structure for sales in 2017 */
DROP TABLE IF EXISTS `sales_2017`;
CREATE TABLE `sales_2017` (
  `OrderDate` DATE NOT NULL,
  `StockDate` DATE NOT NULL,
  `OrderNumber` VARCHAR(100) NOT NULL,
  `ProductKey` INT NOT NULL,
  `CustomerKey` INT NOT NULL,
  `TerritoryKey` INT NOT NULL,
  `OrderLineItem` INT NOT NULL,
  `OrderQuantity` INT NOT NULL,
  PRIMARY KEY (`OrderNumber`),
  KEY `ProductKey` (`ProductKey`),
  KEY `CustomerKey` (`CustomerKey`),
  KEY `TerritoryKey` (`TerritoryKey`),
  KEY `OrderDate` (`OrderDate`),
  CONSTRAINT `sales_2017_ibfk_1` FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
  CONSTRAINT `sales_2017_ibfk_2` FOREIGN KEY (`CustomerKey`) REFERENCES `customers` (`CustomerKey`),
  CONSTRAINT `sales_2017_ibfk_3` FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`TerritoryKey`),
  CONSTRAINT `sales_2017_ibfk_4` FOREIGN KEY (`OrderDate`) REFERENCES `calendar` (`OrderDate`)
);