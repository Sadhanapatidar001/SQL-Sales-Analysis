import pandas as pd
import sqlite3

conn = sqlite3.connect("ecommerce.db")
print("Database created successfully!")

customers = pd.read_csv("Clean_Customers.csv")
products = pd.read_csv("Clean_Products.csv")
orders = pd.read_csv("Clean_Orders.csv")
order_items = pd.read_csv("Clean_OrderItems.csv")

customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)

query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)
print(tables)

print(pd.read_sql("SELECT COUNT(*) AS Total_Customers FROM customers;", conn))
print(pd.read_sql("SELECT COUNT(*) AS Total_Products FROM products;", conn))
print(pd.read_sql("SELECT COUNT(*) AS Total_Orders FROM orders;", conn))
print(pd.read_sql("SELECT COUNT(*) AS Total_OrderItems FROM order_items;", conn))

print(pd.read_sql("SELECT * FROM customers LIMIT 5;", conn))
print(pd.read_sql("SELECT * FROM products LIMIT 5;", conn))
print(pd.read_sql("SELECT * FROM orders LIMIT 5;", conn))
print(pd.read_sql("SELECT * FROM order_items LIMIT 5;", conn))

conn.close()
print("Database connection closed.")