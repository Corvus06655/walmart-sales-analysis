# Walmart Sales Analysis — End-to-End SQL + Python Project

An end-to-end retail analytics case study that cleans transaction data with Python, loads the resulting table into relational databases, and answers business questions with MySQL and PostgreSQL. The project is designed to demonstrate the workflow a Data Analyst would use from raw data validation through KPI-oriented SQL analysis.

> **Portfolio focus:** data cleaning, revenue calculation, payment behavior, branch performance, SQL portability, window functions, CTEs, and business storytelling.

## Business objective

Retail teams need a reliable view of sales value, product categories, branch performance, payment methods, and customer ratings. This project turns a messy transaction extract into a clean analysis-ready dataset and documents the assumptions used in the transformation.

## Verified dataset facts

The raw file contains **10,051 transactions**, 11 columns, 51 duplicate rows, and 62 empty cells [1]. The cleaned file contains **9,969 transactions**, zero duplicate rows, and zero empty cells [2]. Revenue in this project is calculated as `unit_price × quantity` after removing the dollar symbol from the price field.

| Metric | Verified result |
|---|---:|
| Raw transactions | 10,051 |
| Clean transactions | 9,969 |
| Duplicate raw rows | 51 |
| Empty raw cells | 62 |
| Derived clean revenue | $1,209,726.38 |
| Top category by derived revenue | Fashion accessories |
| Top branch by derived revenue | WALM009 |
| Most common payment method | Credit card |

## Key business insights

The cleaned dataset produces **$1,209,726.38** in derived revenue. Fashion accessories is the leading category by derived revenue, while branch `WALM009` is the leading branch in the cleaned extract. Credit card is the most frequently observed payment method. These are descriptive findings from the project dataset, not claims about Walmart’s current commercial performance.

The most important analytical improvement is the transition from the raw file to the clean file: duplicate rows and missing cells are addressed before aggregation, making downstream SQL results more defensible. A production implementation should additionally reconcile row-level revenue against a source-system sales total and document the treatment of refunds, discounts, and taxes if those fields become available.

## Analytical workflow

1. Profile the raw CSV for duplicates, missing cells, data types, and field validity.
2. Clean the transaction extract and preserve a separate analysis-ready CSV.
3. Derive revenue from unit price and quantity.
4. Load the cleaned data into MySQL or PostgreSQL.
5. Use dialect-specific SQL to answer nine retail business questions.
6. Compare results across database engines and review the notebook outputs.

## SQL questions covered

The query files cover revenue and quantity summaries, category performance, payment-method behavior, branch-level comparisons, rating analysis, time and shift analysis, and ranking-based questions. The MySQL and PostgreSQL versions use the same business logic while respecting each dialect’s date and string functions [3] [4].

## Data-quality checks

The repository includes a validation script at `scripts/validate_data.py`. It checks the expected columns, compares raw and clean row counts, verifies that the cleaned file has no duplicate rows or missing cells, validates numeric conversion for price and quantity, and confirms that derived revenue is non-negative.

## Repository structure

```text
├── data/
│   ├── Walmart.csv
│   └── walmart_clean_data.csv
├── images/
│   └── walmart_project.png
├── notebooks/
│   └── walmart_analysis.ipynb
├── scripts/
│   └── validate_data.py
├── sql_queries/
│   ├── mysql_queries.sql
│   └── postgresql_queries.sql
├── requirements.txt
└── Walmart_Business_Problems.pdf
```

## How to reproduce

```bash
git clone https://github.com/Corvus06655/walmart-sales-analysis.git
cd walmart-sales-analysis
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_data.py
```

To run the SQL analysis, load `data/walmart_clean_data.csv` into a database table and execute the matching query file in `sql_queries/`. The notebook provides the Python-side cleaning and exploratory workflow.

## Data provenance and limitations

The repository contains the working raw and cleaned CSV extracts used for this educational case study. The project is not affiliated with Walmart and should not be interpreted as analysis of Walmart’s current internal systems. Because the dataset does not expose a full commercial data dictionary, assumptions about revenue, discounts, refunds, and profitability should be validated before operational use.

## References

[1]: data/Walmart.csv — raw transaction extract.
[2]: data/walmart_clean_data.csv — cleaned transaction extract.
[3]: sql_queries/mysql_queries.sql — MySQL business queries.
[4]: sql_queries/postgresql_queries.sql — PostgreSQL business queries.
[5]: notebooks/walmart_analysis.ipynb — Python cleaning and analysis workflow.

## Author

**Mayank Srivastava** · [GitHub](https://github.com/Corvus06655) · [LinkedIn](https://linkedin.com/in/mayank-srivastava-076020215)
