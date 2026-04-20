import pandas as pd

# Load raw data
df = pd.read_csv("orders.csv")

# Basic cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Convert data types
df['order_date'] = pd.to_datetime(df['order_date'])

# Create new column
df['total_price'] = df['quantity'] * df['price']

# Save cleaned data
df.to_csv("clean_orders.csv", index=False)

print("Data cleaned and saved as clean_orders.csv")