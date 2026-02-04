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
    
    # Pre-calculating unique values for both datasets significantly reduces
    # the number of elements to check during membership filtering.
    unique_df1 = df1[column].unique()
    unique_df2 = df2[column].unique()

    # Using pandas' vectorized .isin() on unique values is significantly faster
    # than Python set subtraction for large datasets. This approach leverages
    # highly optimized C/Cython implementations and avoids the overhead of
    # converting large Series or arrays to Python sets.
    mask = ~pd.Series(unique_df1).isin(unique_df2)
    data_in_df1_not_in_df2 = unique_df1[mask]

    return data_in_df1_not_in_df2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
