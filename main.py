import argparse
import pandas
parser = argparse.ArgumentParser(
    prog="comprare",
    description="Compare CSVs",
    epilog="by Mariann798"
)

parser.add_argument("-t", "--this", help="", required=True)
parser.add_argument("-w", "--with_that", help="", required=True)
parser.add_argument("-c", "--column", help="", required=True)

def read_csv(path:str, column:str) -> pandas.DataFrame:
    # Specifying dtype=str bypasses pandas' automatic type inference,
    # which provides a significant performance boost for large CSV files
    # when the column is known to contain string-like identifiers.
    return pandas.read_csv(path, sep=";", usecols=[column], dtype=str)

def compare_files(path1:str, path2:str, column):
    df1 = read_csv(path1, column)
    print("Len File 1: ", len(df1))
    df2 = read_csv(path2, column)
    print("Len File 2: ", len(df2))
    
    # For finding elements in one collection that are not in another, using
    # pandas' `.isin()` method on a Series is significantly more performant
    # than converting both collections to Python sets and taking the difference.
    # This approach leverages pandas' optimized, vectorized operations and avoids
    # the costly overhead of creating and iterating over large set objects.
    df1_series = df1[column]
    df2_uniques = df2[column].unique()

    # The `~` operator inverts the boolean mask returned by `.isin()`,
    # effectively filtering for elements in `df1_series` that are NOT
    # present in `df2_uniques`. We then get the unique values from the result.
    data_in_df1_not_in_df2 = df1_series[~df1_series.isin(df2_uniques)].unique()

    # .tolist() is the correct and idiomatic method to convert the resulting
    # NumPy array (from .unique()) into a Python list.
    return data_in_df1_not_in_df2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
