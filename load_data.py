import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("clean_orders.csv")

# MySQL connection
username = "root"
password = "root123"
host = "localhost"
database = "ecommerce"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# Load data into MySQL
df.to_sql("orders", con=engine, if_exists="replace", index=False)

print("Data loaded into MySQL successfully")