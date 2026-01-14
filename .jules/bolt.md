## 2024-05-20 - Vectorized vs. Set-Based Filtering

**Learning:** Using `pandas.Series.isin()` for filtering is significantly more performant than converting Series to Python sets and calculating the difference. The vectorized `isin` method leverages pandas' internal C optimizations and avoids the high overhead of creating Python set objects, especially for large datasets.

**Action:** When comparing or filtering pandas Series, always default to using vectorized methods like `.isin()` instead of converting to other data structures like sets, unless a specific algorithm requires set-only features. Measure the performance to confirm the impact.