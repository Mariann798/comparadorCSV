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
    
    # Vectorizing the comparison logic using .isin() on unique values is
    # significantly more performant than Python set subtraction for large
    # datasets. It leverages optimized pandas routines for membership testing,
    # which is faster than Python's set-based approach for large-scale string
    # identifier comparisons in this environment.
    s1_unique = df1[column].unique()
    s2_unique = df2[column].unique()
    mask = ~pd.Series(s1_unique).isin(s2_unique)
    data_in_df1_not_in_df2 = s1_unique[mask]

    return data_in_df1_not_in_df2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
