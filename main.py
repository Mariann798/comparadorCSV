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
    
    # For optimal performance, first find the unique values in the second dataframe.
    # This minimizes the size of the lookup table for the 'isin' check.
    df2_uniques = df2[column].unique()

    # The `isin` method provides a highly optimized, vectorized way to check for
    # membership. Using the `~` operator inverts the result, effectively filtering
    # for elements in `df1` that are NOT in `df2_uniques`. This avoids the costly
    # overhead of converting pandas Series to Python sets.
    # Finally, `.unique()` is called to ensure the output contains only distinct values,
    # matching the logic of the original set-based approach.
    data_in_df1_not_in_df2 = df1[column][~df1[column].isin(df2_uniques)].unique()
    return list(data_in_df1_not_in_df2)

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
