import csv
import os
import shutil
from zipfile import ZipFile

import openpyxl
import pytest

CURRENT_DIR = os.getcwd()
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')


@pytest.fixture(scope='module', autouse=True)
def test_zip_folder():
    with ZipFile('my_archive.zip', "w") as myzip:
        for files in os.walk(TMP_DIR):
            for file in files[2]:
                myzip.write(os.path.join(os.path.relpath(TMP_DIR, CURRENT_DIR), file))

    xlsx_file = os.path.join(TMP_DIR, 'file_example_XLSX_50.xlsx')
    wb = openpyxl.load_workbook(xlsx_file)
    sheet = wb.active

    with open('file_example_CSV.csv', 'w') as file:
        csv_file = csv.writer(file)
        for row in sheet.rows:
            csv_file.writerow([cell.value for cell in row])

    with ZipFile('my_archive.zip', "a") as myzip:
        myzip.write('file_example_CSV.csv')

    os.makedirs("resources", exist_ok=True)
    shutil.move("my_archive.zip", "resources/my_archive.zip")
    shutil.move("file_example_CSV.csv", "resources/file_example_CSV.csv")
    yield
    shutil.rmtree("resources")
