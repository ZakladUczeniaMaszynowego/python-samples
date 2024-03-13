from .file_reader_supervised import FileReaderSupervised
import pandas as pd


class FileReaderSampleHeader(FileReaderSupervised):
    def __init__(self, path):
        super().__init__(path)

    def read_data(self) -> tuple:
        data = pd.read_csv(self.path, header=0)

        return data.values[:, :-1], data.values[:, -1]
