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

    # For optimal performance, we first get the unique values from both series.
    # .unique() is a highly optimized numpy-based operation.
    df1_uniques = df1[column].unique()
    df2_uniques = df2[column].unique()

    # We then use the vectorized `.isin()` method, which is significantly faster
    # than converting to Python sets for a difference operation. This check is
    # performed within pandas'/numpy's optimized C-level routines.
    # The `~` operator inverts the resulting boolean mask to find elements
    # in the first dataframe that are NOT present in the second.
    in_df2 = pandas.Series(df1_uniques).isin(df2_uniques)
    data_in_df1_not_in_df2 = df1_uniques[~in_df2]
    
    return data_in_df1_not_in_df2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
