# 🛒 Walmart Sales Analysis — End-to-End SQL + Python Project

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()

> An end-to-end data analytics pipeline on Walmart sales data — cleaned and processed with Python (Pandas), loaded into both MySQL and PostgreSQL, and analyzed using advanced SQL (window functions, CTEs, ranking) to solve 9 real business problems.

![Project Pipeline](images/project_pipeline.png)

## 📌 Project Overview

This project simulates a full analytics workflow a Data Analyst would run at a retail company: sourcing raw sales data, cleaning and transforming it in Python, loading it into relational databases, and writing SQL to answer business-critical questions — around revenue, ratings, payment behavior, and branch performance.

| | |
|---|---|
| **Data** | Walmart 10K sales transactions dataset |
| **Languages/Tools** | Python (Pandas), MySQL, PostgreSQL |
| **Business Questions Solved** | 9 |
| **Techniques** | Data cleaning, feature engineering, window functions, CTEs, ranking, date functions |

## 🗂️ Repository Structure
```
walmart-sales-analysis/
├── README.md
├── requirements.txt
├── Walmart_Business_Problems.pdf     # Business questions this project answers
├── data/
│   ├── Walmart.csv                    # Raw dataset
│   └── walmart_clean_data.csv          # Cleaned dataset (post feature engineering)
├── notebooks/
│   └── walmart_analysis.ipynb          # Data cleaning, EDA, feature engineering
├── sql_queries/
│   ├── mysql_queries.sql               # Business problem queries — MySQL
│   └── postgresql_queries.sql          # Business problem queries — PostgreSQL
└── images/
    ├── project_pipeline.png
    └── walmart_project.png
```

## ❓ Business Problems Solved
1. Payment methods used, number of transactions, and quantity sold per method
2. Highest-rated category in each branch
3. Busiest day of the week for each branch, by transaction volume
4. Total quantity of items sold per payment method
5. Average, minimum, and maximum rating per category, by city
6. Total profit per category, ranked highest to lowest
7. Most common (preferred) payment method per branch
8. Sales split into Morning / Afternoon / Evening shifts, per branch
9. Top 5 branches with the highest revenue decline year-over-year (2022 → 2023)

## 🔑 Key Techniques Used
- **Data cleaning & feature engineering** in Pandas — deduplication, missing values, data-type fixes, currency formatting, and a calculated `total` (unit_price × quantity) field
- **Window functions** (`RANK() OVER (PARTITION BY ...)`) to find top category/day/payment-method per branch
- **CTEs** for multi-step logic (e.g., year-over-year revenue comparison)
- **Date functions** (`STR_TO_DATE`/`TO_DATE`, `DAYNAME`) to derive weekday and shift-based insights
- Dialect-aware SQL — same business logic written for **both MySQL and PostgreSQL**

## 🛠️ Tech Stack
`Python` · `Pandas` · `SQLAlchemy` · `MySQL` · `PostgreSQL` · `Jupyter Notebook`

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Load `data/walmart_clean_data.csv` into MySQL/PostgreSQL (or explore it directly via `notebooks/walmart_analysis.ipynb`)
4. Run the queries in `sql_queries/mysql_queries.sql` or `sql_queries/postgresql_queries.sql` against your database

## 📁 Dataset
Walmart 10K sales transactions dataset, with fields including branch, city, category, unit price, quantity, payment method, rating, date, and time.

---
*Part of a Data Analyst project portfolio.*
