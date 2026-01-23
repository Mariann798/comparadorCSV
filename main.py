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
    
    # For finding elements in one Series that are not in another, the `isin`
    # method is highly optimized. By passing the unique values of the second
    # DataFrame to `isin` and negating the result with `~`, we create a boolean
    # mask to filter the first DataFrame. This vectorized approach is
    # significantly faster than converting both Series to sets and performing
    # a set difference, as it avoids the overhead of Python-level iteration.
    df1_series = df1[column]
    df2_uniques = df2[column].unique()

    data_in_df1_not_in_df2 = df1_series[~df1_series.isin(df2_uniques)].unique()

    return data_in_df1_not_in_df2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
