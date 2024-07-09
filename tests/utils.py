import ctypes
import os
from pathlib import Path

from monkeytoolbox import get_binary_io_sha256_hash


def is_user_admin():
    if os.name == "posix":
        return os.getuid() == 0

    return ctypes.windll.shell32.IsUserAnAdmin()


def raise_(ex):
    raise ex


def get_file_sha256_hash(filepath: Path) -> str:
    """
    Calculates sha256 hash from a file path

    :param filepath: A Path object which defines file on the system
    :return sha256 hash of the file
    """
    with open(filepath, "rb") as f:
        return get_binary_io_sha256_hash(f)
