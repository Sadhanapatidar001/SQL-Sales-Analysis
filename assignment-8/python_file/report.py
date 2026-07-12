import argparse
import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

#Creating the argument parser
parser = argparse.ArgumentParser(description="E-Commerce Analytics Reports")
parser.add_argument(
    "report",
    nargs="?",
    default="revenue",
    choices=["revenue", "orders", "customers", "products"]
)
args = parser.parse_args()


#Revenue Report
if args.report == "revenue":

    query = """
    SELECT ROUND(SUM(price + freight_value),2) AS Total_Revenue
    FROM order_items;
    """

    print(pd.read_sql(query, conn))

#Orders Report
elif args.report == "orders":

    query = """
    SELECT order_status,
           COUNT(*) AS Total
    FROM orders
    GROUP BY order_status;
    """

    print(pd.read_sql(query, conn))

#Customers Report
elif args.report == "customers":

    query = """
    SELECT
    c.customer_unique_id,
    COUNT(o.order_id) TotalOrders

    FROM customers c

    JOIN orders o

    ON c.customer_id=o.customer_id

    GROUP BY c.customer_unique_id

    ORDER BY TotalOrders DESC

    LIMIT 10;
    """

    print(pd.read_sql(query, conn))

#Products Report
elif args.report == "products":

    query = """
    SELECT
    product_id,
    COUNT(*) Sold

    FROM order_items

    GROUP BY product_id

    ORDER BY Sold DESC

    LIMIT 10;
    """

    print(pd.read_sql(query, conn))

#Closing the connection
conn.close()

