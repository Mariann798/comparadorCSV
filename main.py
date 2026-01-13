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
    
    # This approach is significantly faster than converting to sets. By using
    # pandas' vectorized `isin` method, we avoid the overhead of converting
    # numpy arrays to python sets and operate within the highly optimized
    # pandas/numpy ecosystem.
    df1_uniques = df1[column].unique()
    df2_uniques = df2[column].unique()

    # Create a boolean mask where True indicates a value in df1_uniques is NOT in df2_uniques
    mask = ~pd.Series(df1_uniques).isin(df2_uniques)

    # Apply the mask to get the final values and convert to a list
    data_in_df1_not_in_df2 = df1_uniques[mask]
    return data_in_df1_not_in_df2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
