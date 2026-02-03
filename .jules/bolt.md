# Bolt's Journal - Critical Learnings

## 2025-05-14 - Vectorized Membership Testing
**Learning:** For large-scale identifier comparisons, `pandas.Series.isin()` on pre-deduplicated arrays is significantly faster (~2.5x) than Python's `set` difference. This leverages pandas' optimized C routines and avoids the overhead of converting to/from Python sets.
**Action:** Prefer `u1[~pd.Series(u1).isin(u2)]` for finding elements in one set but not another when working with pandas data.
