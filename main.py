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
    
    # For optimal performance, we first get the unique values from each DataFrame's column.
    # pandas.Series.unique() is highly optimized for this task.
    series1_uniques = df1[column].unique()
    series2_uniques = df2[column].unique()

    # We then use pandas.Series.isin() for a fast, vectorized lookup to find which values
    # from the first series are also present in the second. The `~` operator inverts this
    # boolean mask, effectively filtering for values in series1 that are NOT in series2.
    # This approach avoids the overhead of converting to Python sets.
    in_series1_not_in_series2 = series1_uniques[~pandas.Series(series1_uniques).isin(series2_uniques)]

    return in_series1_not_in_series2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
