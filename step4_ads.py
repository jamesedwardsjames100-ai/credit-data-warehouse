import sqlite3
import pandas as pd

print("开始构建 ADS 层...")
conn = sqlite3.connect('credit_warehouse.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS ads_region_risk")

# 计算违约率，并保留两位小数
sql_ads = """
CREATE TABLE ads_region_risk AS
SELECT 
    region,
    total_loan_count,
    total_loan_amount,
    overdue_count,
    avg_interest_rate,
    ROUND(overdue_count * 100.0 / total_loan_count, 2) AS overdue_rate_pct
FROM dws_region_summary
ORDER BY overdue_rate_pct DESC;
"""
cursor.execute(sql_ads)
conn.commit()

# 打印最终结果
print("\n🎉 ADS层构建成功！各地区的风控指标如下：")
result = pd.read_sql("SELECT * FROM ads_region_risk", conn)
print(result.to_string(index=False))
conn.close()