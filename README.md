# 金融信贷业务离线数仓与指标体系建设 (Credit Data Warehouse)

## 📌 项目简介
本项目基于真实的金融信贷数据集（Kaggle Loan Default），使用 Python 与 SQLite 从零搭建企业级离线数据仓库。项目遵循维度建模（星型模型）理论，完成了从数据接入 (ODS) 到明细清洗 (DWD)、汇总聚合 (DWS) 以及业务指标输出 (ADS) 的全链路 ETL 调度，并包含数据质量监控模块。

## 🏗️ 数仓分层架构
1. **ODS (原始层)**：接入全量原始 CSV 数据，保留现场痕迹。
2. **DWD (明细层)**：编写 SQL 剔除金额为负等异常记录；处理空值并构建**用户维度表** (`dwd_dim_user`) 与**借款事实表** (`dwd_fact_loan`)。
3. **DWS (汇总层)**：将事实表与维度表 `JOIN` 聚合，按地区 (`Region`) 统计总放款金额、逾期笔数与平均利率。
4. **ADS (应用层)**：面向业务，计算核心风控指标——**地区违约率** (`overdue_rate_pct`)，支撑下游 BI 看板。

## 📊 业务指标产出示例 (ADS层)
执行全链路后，成功计算得出各地区的信贷违约率，结果如下：

| region | total_loan_count | total_loan_amount | overdue_count | avg_interest_rate | overdue_rate_pct |
| :--- | :--- | :--- | :--- | :--- | :--- |
| North-East | 1235 | 381687500 | 376 | 4.062154 | 30.45% |
| central | 8697 | 2809970500 | 2395 | 4.065262 | 27.54% |
| south | 64016 | 21337884000 | 17047 | 4.035249 | 26.63% |
| North | 74722 | 24697733000 | 16821 | 4.051406 | 22.51% |

## 🚀 运行说明
本项目已实现全链路自动化调度，依赖 `pandas` 和 `sqlite3`。
依次执行以下脚本：
1. `python step1_ods.py`
2. `python step2_dwd.py`
3. `python step3_dws.py`
4. `python step4_ads.py`

**或直接运行主控 ETL 调度脚本（推荐）：**
`python etl_pipeline.py`