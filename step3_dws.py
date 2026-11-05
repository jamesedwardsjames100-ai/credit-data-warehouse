import sqlite3

print("开始构建 DWS 层...")
conn = sqlite3.connect('credit_warehouse.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS dws_region_summary")

# 按 Region 维度聚合指标
sql_dws = """
CREATE TABLE dws_region_summary AS
SELECT 
    u.region,
    COUNT(f.user_id) AS total_loan_count, 
    SUM(f.loan_amount) AS total_loan_amount,
    SUM(CASE WHEN f.loan_status = 1 THEN 1 ELSE 0 END) AS overdue_count, 
    AVG(f.rate_of_interest) AS avg_interest_rate
FROM dwd_fact_loan f
JOIN dwd_dim_user u ON f.user_id = u.user_id
GROUP BY u.region;
"""
cursor.execute(sql_dws)
conn.commit()
conn.close()
print("✅ DWS层构建成功！已按地区聚合借款金额及逾期笔数。")