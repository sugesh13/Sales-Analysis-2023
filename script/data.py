import pandas as pd
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv("data/sales_dataset.csv")

# Data cleaning
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)
df['Product Name'] = df['Product Name'].str.strip().str.title()
df.fillna({"Profit": 0}, inplace=True)
df['Avg_Price'] = (df['Sales'] / df['Quantity']).round(2)

# Save cleaned data
df.to_csv("data/sales_cleaned.csv", index=False)

# Load into SQLite
engine = create_engine('sqlite:///data/sales.db')
df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("✅ Data cleaned and loaded into SQLite database.")