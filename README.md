# 金融信贷业务离线数仓 (Credit Data Warehouse)

## 项目简介
基于真实的信贷数据集，使用 Python 与 SQLite 从零搭建离线数仓，实现数据的 ETL 清洗与分层建模。

## 🏗️ 架构设计
- **ODS (原始层)**：原封不动接入 CSV 数据。
- **DWD (明细层)**：清洗缺失值，拆分出用户维度表 (`dim_user`) 与借款事实表 (`fact_loan`)。
- **DWS (汇总层)**：按地区 (`Region`) 进行聚合统计。
- **ADS (应用层)**：输出核心风控指标——地区违约率 (`overdue_rate_pct`)。

## 🚀 运行方式
依次执行：
1. `python step1_ods.py`
2. `python step2_dwd.py`
3. `python step3_dws.py`
4. `python step4_ads.py`
# 金融信贷业务离线数仓与指标体系建设

## 📌 项目背景
基于真实的金融信贷数据集（Kaggle Loan Default），使用 Python 与 SQLite 从零搭建企业级离线数据仓库。项目遵循维度建模（星型模型）理论，完成数据 ETL 清洗、分层建模及风控指标输出。

## 🏗️ 数仓分层架构
1. **ODS (原始层)**：接入全量原始 CSV 数据，保留现场痕迹。
2. **DWD (明细层)**：编写 SQL 剔除金额为负等异常记录；处理空值并构建**用户维度表** (`dwd_dim_user`) 与**借款事实表** (`dwd_fact_loan`)。
3. **DWS (汇总层)**：将事实表与维度表 `JOIN` 聚合，按地区 (`Region`) 统计总放款金额、逾期笔数与平均利率。
4. **ADS (应用层)**：面向业务，计算核心风控指标——**地区违约率** (`overdue_rate_pct`)，支撑下游 BI 看板。

## 🚀 运行说明
1. 依次运行 `step1_ods.py` -> `step2_dwd.py` -> `step3_dws.py` -> `step4_ads.py`。
2. 最终在 `credit_warehouse.db` 的 `ads_region_risk` 表中查看业务指标。