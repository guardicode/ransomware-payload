import shutil
from pathlib import Path

import pytest

from monkeytoolbox import get_os
from monkeytypes import OperatingSystem


@pytest.fixture(scope="session")
def data_for_tests_dir(pytestconfig) -> Path:
    return Path(pytestconfig.rootdir) / "tests" / "data_for_tests"


@pytest.fixture(scope="session")
def stable_file(data_for_tests_dir: Path) -> Path:
    return data_for_tests_dir / "stable_file.txt"


@pytest.fixture
def ransomware_test_data(data_for_tests_dir: Path) -> Path:
    return data_for_tests_dir / "ransomware_targets"


@pytest.fixture
def ransomware_target(tmp_path, ransomware_test_data) -> Path:
    ransomware_target = tmp_path / "ransomware_target"
    shutil.copytree(ransomware_test_data, ransomware_target)

    return ransomware_target


@pytest.fixture(params=[".m0nk3y", ".test", ""], ids=["monkeyext", "testext", "noext"])
def ransomware_file_extension(request) -> str:
    return request.param

@pytest.fixture
def home_env_variable():
    if get_os() == OperatingSystem.WINDOWS:
        return "%USERPROFILE%"
    else:
        return "$HOME"

@pytest.fixture
def patched_home_env(monkeypatch, tmp_path, home_env_variable):
    monkeypatch.setenv(home_env_variable.strip("%$"), str(tmp_path))

    return tmp_path
