import sqlite3
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
import pandas as pd

print("开始构建 ODS 层...")
# 连接数据库（如果没有会自动创建 credit_warehouse.db）
conn = sqlite3.connect('credit_warehouse.db')

# 读取原始 CSV 数据
df_raw = pd.read_csv('Loan_Default.csv')

# 写入数据库表 ods_loan，if_exists='replace' 表示每次跑都覆盖旧表，方便调试
df_raw.to_sql('ods_loan', conn, if_exists='replace', index=False)

print(f"✅ ODS层构建成功！共导入了 {len(df_raw)} 条原始数据。")
conn.close()