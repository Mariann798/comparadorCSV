## 2026-02-06 - Vectorized 'isin' vs Set operations
**Learning:** For large datasets (1M+ rows), using pandas' vectorized `.isin()` on unique values is significantly more performant than Python's `set()` subtraction for finding elements in one column but not another. In this environment, it reduced execution time by approximately 48%.
**Action:** Always prefer vectorized pandas operations over standard Python collections (set, list) when dealing with large Series, especially for membership and difference operations.
