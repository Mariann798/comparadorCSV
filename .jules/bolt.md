## 2025-05-14 - Optimized CSV column comparison
**Learning:** Using `Series[~Series.isin(other_series_uniques)]` is significantly more performant than `set(series1.unique()) - set(series2.unique())` for finding elements in one pandas Series that are not in another. This leverages pandas' optimized, vectorized operations and avoids the overhead of converting to Python sets.
**Action:** Always prefer vectorized pandas operations for data comparison tasks to ensure maximum performance with large datasets.
