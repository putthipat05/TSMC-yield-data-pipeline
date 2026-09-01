import pandas as pd
import numpy as np

# ตั้งค่า Seed เพื่อให้สุ่มได้ข้อมูลเหมือนกันทุกครั้งที่รัน
np.random.seed(42)
n_rows = 1000

# 1. จำลองตาราง df_wafers (1,000 รายการ)
wafer_ids = [f" WF-{i:04d} " if i % 3 == 0 else f"WF-{i:04d}" for i in range(1001, 1001 + n_rows)]
lot_codes = np.random.choice(['l-a1', 'L-A1 ', 'L-B2', 'l-b2 ', 'L-C3', 'L-C3 '], size=n_rows)
thickness = np.random.normal(loc=725.0, scale=3.5, size=n_rows)
# ใส่ NaN ใน Thickness 5%
thickness[np.random.choice(n_rows, size=int(n_rows * 0.05), replace=False)] = np.nan

# วันที่แบบ Format ผสมและมี Space
date_formats = ['2026-08-{:02d} ', ' {:02d}/08/2026', '2026/08/{:02d}']
dates = [
    date_formats[i % 3].format(np.random.randint(1, 29))
    for i in range(n_rows)
]

df_wafers = pd.DataFrame({
    'Wafer_ID': wafer_ids,
    'Lot_Code': lot_codes,
    'Thickness_nm': thickness,
    'Inspection_Date': dates
})

# 2. จำลองตาราง df_yield (800 รายการ - ข้อมูลบาง Wafer ยังไม่ได้ตรวจ)
yield_wafer_ids = [f"WF-{i:04d}" for i in range(1001, 1001 + 800)]
defects = np.random.choice(['NONE', 'none', ' edge_scratch ', 'EDGE_SCRATCH', 'RING_DEFECT', 'ring_defect'], size=800, p=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1])
passed_dies = np.random.randint(750, 1000, size=800)

df_yield = pd.DataFrame({
    'Wafer_ID': yield_wafer_ids,
    'Total_Dies': 1000,
    'Passed_Dies': passed_dies,
    'Defect_Category': defects
})

df_wafers['Wafer_Id'] = df_wafers['Wafer_ID'].str.strip() 
df_wafers['Lot_Code'] = df_wafers['Lot_Code'].str.strip().str.upper()
df_wafers['Inspection_Date'] = pd.to_datetime(df_wafers['Inspection_Date'].str.strip(), format= 'mixed')
thickness_mean = df_wafers['Thickness_nm'].mean()
df_wafers['Thickness_nm'] = df_wafers['Thickness_nm'].fillna(thickness_mean)
df_master = pd.merge(df_wafers, df_yield ,on = 'Wafer_ID', how ='left' )
df_master['Defect_Category'] = df_master['Defect_Category'].str.strip().str.upper()
df_master['Total_Dies'] = df_master['Total_Dies'].fillna(1000)
df_master['Passed_Dies'] = df_master['Passed_Dies'].fillna(0)
df_master['Defect_Category'] = df_master['Defect_Category'].fillna('UNINSPECTED')
df_master['Yield_Rate_%'] = (df_master['Passed_Dies'] / df_master['Total_Dies']) * 100
df_pivot = pd.pivot_table(df_master, index='Lot_Code', columns='Defect_Category',values='Yield_Rate_%', aggfunc='mean', fill_value =0 )
print(df_pivot)