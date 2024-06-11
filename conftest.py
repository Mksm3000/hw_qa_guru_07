import os
import shutil
from zipfile import ZipFile

import pytest

CURRENT_DIR = os.getcwd()
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')


@pytest.fixture(scope='module', autouse=True)
def test_zip_folder():
    with ZipFile('my_archive.zip', "w") as myzip:
        for files in os.walk(TMP_DIR):
            for file in files[2]:
                myzip.write(os.path.join(os.path.relpath(TMP_DIR, CURRENT_DIR), file))

    os.makedirs("resources", exist_ok=True)
    shutil.move("my_archive.zip", "resources/my_archive.zip")
    yield
    shutil.rmtree("resources")
