import sqlite3
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("开始构建 DWD 层...")
conn = sqlite3.connect('credit_warehouse.db')
cursor = conn.cursor()

# 删掉旧表，防止报错
cursor.execute("DROP TABLE IF EXISTS dwd_dim_user")
cursor.execute("DROP TABLE IF EXISTS dwd_fact_loan")

# 1. 建用户维度表 (dim_user)：处理空值，按 ID 去重
sql_dim_user = """
CREATE TABLE dwd_dim_user AS
SELECT 
    ID AS user_id,
    COALESCE(Gender, 'Unknown') AS gender, 
    COALESCE(age, 0) AS age, 
    COALESCE(Region, 'Unknown') AS region, 
    Credit_Score, 
    COALESCE(income, 0) AS income
FROM ods_loan
WHERE ID IS NOT NULL
GROUP BY ID;
"""
cursor.execute(sql_dim_user)

# 2. 建借款事实表 (fact_loan)：过滤金额异常，提取核心行为
sql_fact_loan = """
CREATE TABLE dwd_fact_loan AS
SELECT 
    ID AS user_id, 
    loan_amount, 
    rate_of_interest, 
    Status AS loan_status, 
    COALESCE(dtir1, 0) AS dti_ratio, 
    COALESCE(LTV, 0) AS ltv_ratio
FROM ods_loan
WHERE loan_amount > 0 AND ID IS NOT NULL AND Status IS NOT NULL;
"""
cursor.execute(sql_fact_loan)

conn.commit()
conn.close()
print("✅ DWD层构建成功！已清洗脏数据，并拆分出维度表与事实表。")