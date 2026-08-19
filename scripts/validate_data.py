from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
raw_path = ROOT / 'data' / 'Walmart.csv'
clean_path = ROOT / 'data' / 'walmart_clean_data.csv'
expected = {'invoice_id', 'Branch', 'City', 'category', 'unit_price', 'quantity', 'date', 'time', 'payment_method', 'rating', 'profit_margin'}

raw = pd.read_csv(raw_path)
clean = pd.read_csv(clean_path)
assert set(raw.columns) == expected, f'Unexpected raw columns: {set(raw.columns) - expected}'
assert set(clean.columns) == expected, f'Unexpected clean columns: {set(clean.columns) - expected}'
assert len(raw) == 10051, f'Unexpected raw row count: {len(raw)}'
assert len(clean) == 9969, f'Unexpected clean row count: {len(clean)}'
assert int(raw.duplicated().sum()) == 51, 'Raw duplicate count changed; review the source extract.'
assert int(clean.duplicated().sum()) == 0, 'Clean data still contains duplicate rows.'
assert int(raw.isna().sum().sum()) == 62, 'Raw missing-cell count changed; review the source extract.'
assert int(clean.isna().sum().sum()) == 0, 'Clean data still contains missing cells.'

price = pd.to_numeric(clean['unit_price'].astype(str).str.replace('$', '', regex=False), errors='coerce')
quantity = pd.to_numeric(clean['quantity'], errors='coerce')
assert price.notna().all(), 'Clean prices contain non-numeric values.'
assert quantity.notna().all(), 'Clean quantities contain non-numeric values.'
revenue = price * quantity
assert (revenue >= 0).all(), 'Derived revenue contains negative values.'
print('Walmart validation passed')
print(f'raw_rows={len(raw)} clean_rows={len(clean)} revenue={revenue.sum():.2f}')
