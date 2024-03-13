from .file_reader_sample import FileReaderSample
from .file_reader_sample_header import FileReaderSampleHeader
from .file_reader_sample_exl_header import FileReaderSampleExlHeader


def get_file_reader(name: str, path: str):
    if name == "sample":
        return FileReaderSample(path)
    elif name == "sample_header":
        return FileReaderSampleHeader(path)
    elif name == "sample_header_excel":
        return FileReaderSampleExlHeader(path)
    else:
        raise NameError()
