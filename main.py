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
    
    # ⚡ Bolt Optimization: Use vectorized `isin` for faster set differences.
    # This approach is significantly faster than converting to Python sets,
    # as it leverages pandas' optimized, low-level C code for the comparison.
    # 1. Get unique values from the second dataframe for efficient lookup.
    df2_uniques = df2[column].unique()

    # 2. Filter the first dataframe to find values not present in the second.
    # The `~` operator negates the boolean Series returned by `isin`.
    data_in_df1_not_in_df2 = df1[column][~df1[column].isin(df2_uniques)]

    # 3. Return the result as a list of unique values.
    return data_in_df1_not_in_df2.unique().tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
