from pathlib import Path


def check_file_exists(path: str):
    """Checks if file exists. Returns True or False."""
    if Path(path).exists():
        return True
    return False


def ex_file_not_exists(path: str):
    """Checks if file exists. Throws an exception if it does not exist."""
    if not Path(path).exists():
        raise FileExistsError("File " + path + " does not exist!!!")
