import pandas as pd
import numpy as np

# สร้างข้อมูลจำลองสำหรับร้านค้าปลีก (Retail Store)
data = {
    'Transaction_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Clothing', 'Furniture', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics'],
    'Price_Per_Unit': [500, 1200, 150, 45, 800, np.nan, 1200, 950, 35, 150],
    'Quantity': [1, 2, 4, 3, 1, 2, np.nan, 1, 10, 2],
    'Member': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)
mean_price = df['Price_Per_Unit'].mean()
df[ 'Price_Per_Unit'] = df['Price_Per_Unit'].fillna(mean_price)
df['Quantity'] = df['Quantity'].fillna(1)
df['total_revenue'] = df['Price_Per_Unit'] * df['Quantity']

eletronics_df = df[(df['Category'] == 'Electronics') & (df['Member'] == 'Yes')]

print(eletronics_df)
