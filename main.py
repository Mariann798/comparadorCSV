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

parser = parser.parse_args()

def read_csv(path:str, column:str) -> pandas.DataFrame:
    return pandas.read_csv(path, sep=";", usecols=[column])

def compare_files(path1:str, path2:str, column):
    df1 = read_csv(path1, column)
    print("Len File 1: ", len(df1))
    df2 = read_csv(path2, column)
    print("Len File 2: ", len(df2))
    
    data_in_df1_not_in_df2 = set(df1[column]) - set(df2[column])
    return list(data_in_df1_not_in_df2)

if __name__ == '__main__':
    res = compare_files(parser.this, parser.with_that, parser.column)
    
    print("Resultados: ", len(res))
    print("Emails: ", res)