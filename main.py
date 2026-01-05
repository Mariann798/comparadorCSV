import argparse
import pandas as pd
parser = argparse.ArgumentParser(
    prog="comprare",
    description="Compare CSVs",
    epilog="by Mariann798"
)

parser.add_argument("-t", "--this", help="", required=True)
parser.add_argument("-w", "--with_that", help="", required=True)
parser.add_argument("-c", "--column", help="", required=True)

def read_csv(path:str, column:str) -> pd.DataFrame:
    # Specifying dtype=str bypasses pandas' automatic type inference,
    # which provides a significant performance boost for large CSV files
    # when the column is known to contain string-like identifiers.
    return pd.read_csv(path, sep=";", usecols=[column], dtype=str)

def compare_files(path1:str, path2:str, column):
    df1 = read_csv(path1, column)
    print("Len File 1: ", len(df1))
    df2 = read_csv(path2, column)
    print("Len File 2: ", len(df2))
    
    # --- Start of Bolt's optimization ---
    # The original implementation converted pandas Series to Python sets to find
    # the difference. This is inefficient as it doesn't leverage pandas'
    # high-performance, C-optimized internal routines.
    #
    # The optimized approach below uses pandas' vectorized `isin` method.
    # We get the unique values from both series first, which is a fast hash-based
    # operation, and then perform the `isin` check on the smaller, unique datasets.
    # This avoids Python-level loops and minimizes the amount of data processed.
    #
    # 📊 Impact: For large CSVs (e.g., 1M rows), this is significantly faster
    # than the set-based approach.
    df1_uniques = df1[column].unique()
    df2_uniques = df2[column].unique()

    # To use the fast .isin() method, we work with a pandas Series.
    s1_uniques_series = pd.Series(df1_uniques)

    # Filter the unique values from the first series for those NOT in the second.
    result_series = s1_uniques_series[~s1_uniques_series.isin(df2_uniques)]

    # Convert to a list as expected by the function's return type.
    return result_series.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
