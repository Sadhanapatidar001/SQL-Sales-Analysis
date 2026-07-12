import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

#Total Revenue
query = """
SELECT
    ROUND(SUM(price + freight_value), 2) AS Total_Revenue
FROM order_items;
"""
print(pd.read_sql(query, conn))

#Total Orders
query = """
SELECT COUNT(*) AS Total_Orders
FROM orders;
"""
print(pd.read_sql(query, conn))

#Orders by Status
query = """
SELECT
    order_status,
    COUNT(*) AS Total_Orders
FROM orders
GROUP BY order_status
ORDER BY Total_Orders DESC;
"""
print(pd.read_sql(query, conn))

#Top 10 Selling Products
query = """
SELECT
    oi.product_id,
    COUNT(*) AS Total_Sold
FROM order_items oi
GROUP BY oi.product_id
ORDER BY Total_Sold DESC
LIMIT 10;
"""
print(pd.read_sql(query, conn))

#Top 10 Customers by Number of Orders
query = """
SELECT
    c.customer_unique_id,
    COUNT(o.order_id) AS Total_Orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
ORDER BY Total_Orders DESC
LIMIT 10;
"""
print(pd.read_sql(query, conn))

#Monthly Revenue Trend
query = """
SELECT
    strftime('%Y-%m', shipping_limit_date) AS Month,
    ROUND(SUM(price + freight_value),2) AS Revenue
FROM order_items
GROUP BY Month
ORDER BY Month;
"""
print(pd.read_sql(query, conn))

#Revenue by Product Category
query = """
SELECT
    p.product_category_name,
    ROUND(SUM(oi.price),2) AS Revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_category_name
ORDER BY Revenue DESC
LIMIT 15;
"""
print(pd.read_sql(query, conn))

#Average Order Value
query = """
SELECT
ROUND(AVG(price),2) AS Average_Order_Value
FROM order_items;
"""
print(pd.read_sql(query, conn))

#Window Function (Customer Ranking)
query = """
SELECT
customer_unique_id,
TotalSpent,
RANK() OVER (ORDER BY TotalSpent DESC) AS CustomerRank
FROM
(
SELECT
c.customer_unique_id,
SUM(oi.price) AS TotalSpent
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_unique_id
);
"""
print(pd.read_sql(query, conn))

#CTE (Top 10 Customers)
query = """
WITH CustomerRevenue AS
(
SELECT
c.customer_unique_id,
SUM(oi.price) Revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_unique_id
)

SELECT *
FROM CustomerRevenue
ORDER BY Revenue DESC
LIMIT 10;
"""
print(pd.read_sql(query, conn))

#Customer Segmentation
query = """
SELECT
customer_unique_id,
TotalSpent,
CASE
WHEN TotalSpent > 5000 THEN 'VIP'
WHEN TotalSpent > 2000 THEN 'Regular'
ELSE 'Normal'
END AS Customer_Type
FROM
(
SELECT
c.customer_unique_id,
SUM(oi.price) AS TotalSpent
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_unique_id
);
"""
print(pd.read_sql(query, conn))

#Top Freight Charges
query = """
SELECT
order_id,
freight_value
FROM order_items
ORDER BY freight_value DESC
LIMIT 10;
"""
print(pd.read_sql(query, conn))

#Cohort Analysis
query = """
WITH first_purchase AS (
    SELECT
        customer_id,
        MIN(date(order_purchase_timestamp)) AS first_purchase_date
    FROM orders
    GROUP BY customer_id
)

SELECT
    strftime('%Y-%m', fp.first_purchase_date) AS Cohort_Month,
    COUNT(DISTINCT o.customer_id) AS Customers
FROM first_purchase fp
JOIN orders o
ON fp.customer_id = o.customer_id
GROUP BY Cohort_Month
ORDER BY Cohort_Month;
"""
print(pd.read_sql(query, conn))

#Retention Metrics
query = """
SELECT
COUNT(*) AS Repeat_Customers
FROM
(
SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1
);
"""
print(pd.read_sql(query, conn))

#Closing the Connection
conn.close()