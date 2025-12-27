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

def compare_files(path1:str, path2:str, column):
    # Process CSVs in chunks to reduce memory usage for very large files.
    # This approach is significantly more memory-efficient as it avoids
    # loading the entire file into memory at once.
    chunk_size = 10000  # The number of rows to read at a time.

    # Read the first CSV in chunks and collect unique values from the specified column.
    unique_values_1 = set()
    for chunk in pandas.read_csv(path1, sep=";", usecols=[column], dtype=str, chunksize=chunk_size):
        unique_values_1.update(chunk[column].unique())
    print("Unique values in File 1: ", len(unique_values_1))

    # Read the second CSV in chunks and collect unique values.
    unique_values_2 = set()
    for chunk in pandas.read_csv(path2, sep=";", usecols=[column], dtype=str, chunksize=chunk_size):
        unique_values_2.update(chunk[column].unique())
    print("Unique values in File 2: ", len(unique_values_2))

    # Find the values that are in the first set but not in the second.
    data_in_df1_not_in_df2 = unique_values_1 - unique_values_2
    return list(data_in_df1_not_in_df2)

if __name__ == '__main__':
    args = parser.parse_args()
    res = compare_files(args.this, args.with_that, args.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)
