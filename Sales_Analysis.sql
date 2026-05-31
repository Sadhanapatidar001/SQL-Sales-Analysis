CREATE DATABASE studentdb;
USE studentdb;
#Load dataset into a SQL database

#Explore table (schema, sample data)
SHOW TABLES;
DESCRIBE `sample - superstore`;
RENAME TABLE `sample - superstore`
TO superstore;

SELECT * FROM superstore;
SELECT COUNT(*) AS total_rows
FROM superstore;


#Apply WHERE filters (region, category, date, sales)
SELECT *
FROM superstore
WHERE Region='West';

SELECT *
FROM superstore
WHERE Sales > 1000;

SELECT *
FROM superstore
WHERE Region='West'
AND Sales > 500;


#Use GROUP BY for aggregations (sales, quantity, averages)
SELECT Category, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category;

SELECT Category, AVG(Sales) AS Avg_Sales
FROM superstore
GROUP BY Category;

SELECT Category, SUM(Quantity) AS Total_Quantity
FROM superstore
GROUP BY Category;


#Sort and limit results (top products, top categories)
SELECT `Product Name`,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT Category, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC
LIMIT 5;

#Solve use cases (monthly trends, top customers, duplicates)
SELECT
YEAR(STR_TO_DATE(`Order Date`, '%m/%d/%Y')) AS Year,
MONTH(STR_TO_DATE(`Order Date`, '%m/%d/%Y')) AS Month,
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY
YEAR(STR_TO_DATE(`Order Date`, '%m/%d/%Y')),
MONTH(STR_TO_DATE(`Order Date`, '%m/%d/%Y'))
ORDER BY Year, Month;

SELECT `Customer Name`,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT `Order ID`, COUNT(*) AS Duplicate_Count
FROM superstore
GROUP BY `Order ID`
HAVING COUNT(*) > 1;


#Validate results (row counts, data quality)
SELECT
COUNT(*) AS Total_Rows,
COUNT(`Order ID`) AS Order_ID_Count,
COUNT(`Customer ID`) AS Customer_ID_Count,
COUNT(`Product ID`) AS Product_ID_Count,
COUNT(Sales) AS Sales_Count
FROM superstore;

SELECT `Order ID`, `Product ID`, COUNT(*) AS Duplicate_Count
FROM superstore
GROUP BY `Order ID`, `Product ID`
HAVING COUNT(*) > 1;