import pandas as pd

customers = pd.read_csv("Customers.csv")
products = pd.read_csv("Products.csv")
orders = pd.read_csv("Orders.csv")
order_items = pd.read_csv("Order Items.csv")
#Handle Empty CSV Files
if customers.empty:
    print("Customers dataset is empty.")

if products.empty:
    print("Products dataset is empty.")

if orders.empty:
    print("Orders dataset is empty.")

if order_items.empty:
    print("Order Items dataset is empty.")

#Edge Case 2 - Required columns
required_customer_columns = [
    "customer_id",
    "customer_unique_id",
    "customer_city",
    "customer_state"
]

for col in required_customer_columns:
    if col not in customers.columns:
        raise ValueError(f"Missing column: {col}")
    
customers.to_csv("Clean_Customers.csv", index=False)
products.to_csv("Clean_Products.csv", index=False)
orders.to_csv("Clean_Orders.csv", index=False)
order_items.to_csv("Clean_OrderItems.csv", index=False)

print("Cleaned files saved successfully.")