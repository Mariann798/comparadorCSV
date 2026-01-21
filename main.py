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
    
    # Using pandas' `isin` is a highly vectorized operation that is
    # significantly faster than converting to Python sets for finding the
    # difference between two series, especially for large datasets.
    # 1. Get unique values from the second dataframe.
    # 2. Create a boolean mask for values in the first dataframe that are NOT in the second.
    # 3. Apply the mask and get the unique values from the result to match original behavior.
    df2_uniques = df2[column].unique()
    data_in_df1_not_in_df2 = df1[column][~df1[column].isin(df2_uniques)].unique()
    return data_in_df1_not_in_df2.tolist()

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
