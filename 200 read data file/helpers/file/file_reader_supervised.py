from abc import ABC, abstractmethod
from .file import check_file_exists


class FileReaderSupervised(ABC):
    def __init__(self, path: str):
        check_file_exists(path)
        self.path = path
        self.x = None
        self.y = None

    @abstractmethod
    def read_data(self):
        pass
