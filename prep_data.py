import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv('data.csv', encoding='ISO-8859-1')

# Clean the data
df.dropna(subset=['CustomerID'], inplace=True)
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Add TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Format date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Save to SQLite
conn = sqlite3.connect('ecommerce.db')
df.to_sql('sales', conn, if_exists='replace', index=False)
conn.close()

print("✅ Database created: ecommerce.db with table 'sales'")
