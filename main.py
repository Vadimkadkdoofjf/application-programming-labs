import argparse
from data import *

def parser_()->str:
    """
    Parses the name of annotation
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of your file')
    args = parser.parse_args().filename
    return args


def main():
    annotation = parser_()

    dataframe = create_dataframe(annotation)
    add_columns(dataframe)
    print(dataframe,"\n\n")

    stat(dataframe)
    print("\n\n")

    new_df = sort(dataframe,1200,1200)
    print(new_df,"\n\n")

    create_s_column(dataframe)
    print(dataframe,"\n\n")

    new_df = sort_s(dataframe)
    print(new_df,"\n\n")

    hist(new_df)


if __name__ == '__main__':
    main()

