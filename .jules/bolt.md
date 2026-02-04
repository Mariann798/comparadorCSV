## 2025-05-15 - Vectorized isin vs Sets and Index difference
**Learning:** For finding differences between large collections of string identifiers, pandas vectorized `.isin()` on unique values is significantly faster (~2x) than Python set subtraction and faster than `pd.Index.difference()`. Additionally, `numpy.isin` is known to perform poorly for large-scale string comparisons in this environment.
**Action:** Prefer `unique_array[~pd.Series(unique_array).isin(other_unique_array)]` for set-like difference operations in pandas-centric codebases.
