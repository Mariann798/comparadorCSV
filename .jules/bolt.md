## 2024-07-25 - Pandas Set Difference Optimization
**Learning:** Using vectorized pandas operations like `isin` is significantly more performant for finding differences between series than converting them to Python sets. The conversion process adds unnecessary overhead that pandas' optimized, underlying C implementations avoid.
**Action:** When comparing pandas Series, always use `isin` for set-like operations instead of converting to `set()`. This is a critical performance pattern for this codebase.
