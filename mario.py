import pandas as pd
import numpy as np

# ตารางที่ 1: รายการขาย (df_sales)
df_sales = pd.DataFrame({
    'SaleID': [1, 2, 3, 4, 5],
    'Product': [' iPhone ', 'IPHONE', ' iPad ', 'MacBook', 'UNKNOWN'],
    'Price': ['30000', '30000', '25000', np.nan, '45000'],
    'StoreID': [101, 101, 102, 101, 999]
})

# ตารางที่ 2: สาขา (df_stores)
df_stores = pd.DataFrame({
    'StoreID': [101, 102],
    'StoreName': ['Bangkok', 'Chiangmai']
})

df_sales['Product'] = df_sales['Product'].str.strip().str.upper()
df_sales['Price'] = df_sales['Price'].astype(float)
median_price = df_sales['Price'].median()
df_sales['Price'] = df_sales['Price'].fillna(median_price)
df_merged = pd.merge(df_sales, df_stores, on = 'StoreID', how = 'left' )
df_merged['StoreName'] = df_merged['StoreName'].fillna('Online')
print(df_merged.groupby('StoreName')['Price'].sum()) 









