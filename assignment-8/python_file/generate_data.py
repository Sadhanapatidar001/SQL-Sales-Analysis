import pandas as pd
import random
from faker import Faker
import numpy as np

customers = pd.read_csv("Customers.csv")
products = pd.read_csv("Products.csv")
orders = pd.read_csv("Orders.csv")
order_items = pd.read_csv("Order Items.csv")

customers.info()
customers.head()
customers.shape

products.info()
products.head()
products.shape

orders.info()
orders.head()
orders.shape

order_items.info()
order_items.head()
order_items.shape

customers.isnull().sum()
products.isnull().sum()
orders.isnull().sum()
order_items.isnull().sum()

customers.duplicated().sum()
products.duplicated().sum()
orders.duplicated().sum()
order_items.duplicated().sum()

customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
order_items.drop_duplicates(inplace=True)

customers.dtypes
products.dtypes
orders.dtypes
order_items

customers.dtypes
orders.dtypes

print(customers.columns)
print(orders.columns)

# Remove leading/trailing spaces
customers["customer_city"] = customers["customer_city"].str.strip()
customers["customer_state"] = customers["customer_state"].str.strip()

# Convert city names to proper case
customers["customer_city"] = customers["customer_city"].str.title()

# Check missing values
print(customers.isnull().sum())


date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

print(orders.dtypes)
print(customers.isnull().sum())
print(orders.isnull().sum())
customers.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)

orders = orders[
    orders["customer_id"].isin(customers["customer_id"])
]

print(products.columns.tolist())
print(order_items.columns.tolist())

customers.drop_duplicates(inplace=True)
print(customers.isnull().sum())
customers["customer_city"] = customers["customer_city"].str.strip()
customers["customer_state"] = customers["customer_state"].str.strip()
customers["customer_city"] = customers["customer_city"].str.title()
print(customers["customer_id"].duplicated().sum())
orders.drop_duplicates(inplace=True)
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

orders = orders[
    orders["customer_id"].isin(customers["customer_id"])
]

today = pd.Timestamp.today()

orders = orders[
    orders["order_purchase_timestamp"] <= today
]

products.drop_duplicates(inplace=True)
print(products.isnull().sum())
products["product_category_name"] = products["product_category_name"].fillna("Unknown")

numeric_cols = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]
for col in numeric_cols:
    products[col] = products[col].fillna(products[col].median())

products = products[
    products["product_weight_g"] > 0
]

products = products[
    (products["product_length_cm"] > 0) &
    (products["product_height_cm"] > 0) &
    (products["product_width_cm"] > 0)
]

order_items.drop_duplicates(inplace=True)
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)
print(order_items.isnull().sum())
order_items = order_items[
    order_items["price"] > 0
]
order_items = order_items[
    order_items["freight_value"] >= 0
]
order_items = order_items[
    order_items["product_id"].isin(products["product_id"])
]
order_items = order_items[
    order_items["order_id"].isin(orders["order_id"])
]


print(customers.info())
print(products.info())
print(orders.info())
print(order_items.info())


print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())
print(order_items.isnull().sum())

customers.to_csv("Clean_Customers.csv", index=False)
products.to_csv("Clean_Products.csv", index=False)
orders.to_csv("Clean_Orders.csv", index=False)
order_items.to_csv("Clean_OrderItems.csv", index=False)

print("Customers :", customers.shape)
print("Products :", products.shape)
print("Orders :", orders.shape)
print("Order Items :", order_items.shape)