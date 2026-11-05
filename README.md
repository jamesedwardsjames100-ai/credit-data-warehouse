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