#Create Database
CREATE DATABASE superstore_db;
USE superstore_db;

DESCRIBE superstore;

#Create Customers Table
CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    segment VARCHAR(50)
);
show tables;

INSERT INTO customers
SELECT
    `Customer ID`,
    MAX(`Customer Name`),
    MAX(Segment)
FROM superstore
GROUP BY `Customer ID`;

#Create Products Table
CREATE TABLE products (
    product_id VARCHAR(30) PRIMARY KEY,
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255)
);

INSERT INTO products
SELECT
    `Product ID`,
    MAX(Category),
    MAX(`Sub-Category`),
    MAX(`Product Name`)
FROM superstore
GROUP BY `Product ID`;


#Create Orders Table
CREATE TABLE orders (
    row_id INT,
    order_id VARCHAR(30),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(20),
    product_id VARCHAR(30),
    sales DECIMAL(15,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(15,2)
);


INSERT INTO orders
SELECT
    `Row ID`,
    `Order ID`,
    STR_TO_DATE(`Order Date`, '%m/%d/%Y'),
    STR_TO_DATE(`Ship Date`, '%m/%d/%Y'),
    `Ship Mode`,
    `Customer ID`,
    `Product ID`,
    Sales,
    Quantity,
    Discount,
    Profit
FROM superstore;


# Subqueries (Orders Above Average Sales)
SELECT *
FROM orders
WHERE sales >
(
    SELECT AVG(sales)
    FROM orders
);


# CTE (Total Sales Per Customer)
WITH customer_sales AS
(
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_sales;


# Window Functions (ROW_NUMBER())
SELECT
    customer_id,
    order_id,
    sales,
    ROW_NUMBER() OVER(
        PARTITION BY customer_id
        ORDER BY sales DESC
    ) AS row_num
FROM orders;


# Window Functions (RANK())
SELECT
    customer_id,
    SUM(sales) AS total_sales,

    RANK() OVER(
        ORDER BY SUM(sales) DESC
    ) AS sales_rank

FROM orders
GROUP BY customer_id;


# JOIN + CTE + Window Function
WITH customer_sales AS
(SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id)

SELECT
    c.customer_name,
    c.segment,
    cs.total_sales,

    RANK() OVER(
        ORDER BY cs.total_sales DESC
    ) AS customer_rank

FROM customer_sales cs
JOIN customers c
ON cs.customer_id = c.customer_id;


# Business Query 1: Top 10 Customers
WITH customer_sales AS
(
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM customer_sales
ORDER BY total_sales DESC
LIMIT 10;

# Business Query 2: Bottom 10 Customers
WITH customer_sales AS
(
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM customer_sales
ORDER BY total_sales ASC
LIMIT 10;

# Business Query 3: Single-Order Customers
SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(DISTINCT order_id) = 1;


# Business Query 4: Customers Above Average Sales
WITH customer_sales AS
(
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM customer_sales
WHERE total_sales >
(
    SELECT AVG(total_sales)
    FROM customer_sales
);


# Business Query 5: Most Profitable Customers
SELECT
    customer_id,
    SUM(profit) AS total_profit
FROM orders
GROUP BY customer_id
ORDER BY total_profit DESC
LIMIT 10;


