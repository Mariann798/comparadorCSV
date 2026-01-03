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
    
    # Cache the unique values from the second dataframe's column for faster lookups.
    df2_uniques = df2[column].unique()

    # Use the vectorized `isin()` method, which is significantly faster than
    # converting to sets for finding elements in one Series that are not
    # present in another. The `~` operator negates the boolean mask,
    # selecting only the rows where the condition is False.
    data_in_df1_not_in_df2 = df1[column][~df1[column].isin(df2_uniques)]

    # Using .unique() here is more memory-efficient and faster than converting the
    # entire Series to a set, especially when there are many duplicate values.
    # It de-duplicates the data first in a highly optimized way before converting to a list.
    return data_in_df1_not_in_df2.unique().tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
