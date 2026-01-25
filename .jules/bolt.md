## 2024-05-22 - Pandas `isin` vs Set Conversion

**Learning:** For finding elements in one pandas Series that are not in another, `Series[~Series.isin(other_series_uniques)]` is significantly more performant than the common `set(series1.unique()) - set(series2.unique())` pattern. The conversion to Python sets is a major overhead that pandas' optimized, vectorized `.isin()` method avoids entirely.

**Action:** In this codebase, when comparing columns between CSVs, always prefer using the `.isin()` method for finding differences. Avoid converting pandas Series to sets for comparison operations.