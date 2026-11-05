import pandas as pd

# 读取你刚才下载的数据
df = pd.read_csv('Loan_Default.csv', nrows=5) # 只读前5行，速度快
print("=== 数据集包含的所有列名 ===")
print(df.columns.tolist())
print("\n=== 前5行数据预览 ===")
print(df.head())