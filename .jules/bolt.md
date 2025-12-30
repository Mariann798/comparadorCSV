## 2024-05-23 - Pandas Set Conversion Optimization

**Learning:** When creating a set from a pandas Series containing string-like data, `set(df['column'])` is measurably faster than `set(df['column'].unique())`. The `.unique()` method first creates an intermediate NumPy array of unique values, which adds unnecessary overhead, especially for large datasets. Direct conversion to a set avoids this step.

**Action:** For future optimizations involving creating sets from pandas Series, I will prefer direct conversion `set(df['column'])` and only use `.unique()` if the intermediate array is needed for other purposes.
