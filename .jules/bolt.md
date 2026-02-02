## 2026-02-02 - Optimizing String Identifier Comparisons in Pandas

**Learning:** When comparing large sets of string identifiers (like emails or UUIDs), `pd.Series.isin()` is significantly more performant than Python's native `set` subtraction and orders of magnitude faster than `np.isin()`. Specifically, `np.isin()` on large string arrays causes massive performance degradation and timeouts due to inefficient string handling in NumPy's default routines.

**Action:** Prefer `pd.Series.isin()` for membership filtering of string data. Ensure data is de-duplicated using `.unique()` before comparison to further minimize the operation's overhead.
