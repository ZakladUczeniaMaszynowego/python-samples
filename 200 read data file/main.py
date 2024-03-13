from helpers.file import get_file_reader

if __name__ == "__main__":
    print(">>>> START")

    # Ex. 1. File without header

    path_data = "./data/sample_data_01.csv"
    type_data = "sample"

    x, y = get_file_reader(type_data, path_data).read_data()

    print(">>>> x:")
    print(x)
    print(x.shape)
    print(">>>> y:")
    print(y)
    print(y.shape)

    # Ex. 2. File with header

    path_data = "./data/sample_data_header_01.csv"
    type_data = "sample_header"

    x, y = get_file_reader(type_data, path_data).read_data()

    print(">>>> x:")
    print(x)
    print(x.shape)
    print(">>>> y:")
    print(y)
    print(y.shape)

    # Ex. 3. Excel file with header

    path_data = "./data/sample_data_02.xlsx"
    type_data = "sample_header_excel"

    x, y = get_file_reader(type_data, path_data).read_data()

    print(">>>> x:")
    print(x)
    print(x.shape)
    print(">>>> y:")
    print(y)
    print(y.shape)

    print(">>>> END")
