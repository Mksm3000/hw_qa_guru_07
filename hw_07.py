import openpyxl
import csv
import os
from zipfile import ZipFile

CURRENT_DIR = os.getcwd()
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')

xlsx_file = os.path.join(TMP_DIR, 'file_example_XLSX_50.xlsx')

wb = openpyxl.load_workbook(xlsx_file)
sheet = wb.active

with open(os.path.join(TMP_DIR, 'file_example_CSV.csv'), 'w') as file:
    csv_file = csv.writer(file)
    for row in sheet.rows:
        csv_file.writerow([cell.value for cell in row])

with ZipFile('my_archive.zip', "a") as myzip:
    for files in os.walk(TMP_DIR):
        for file in files[2]:
            myzip.write(os.path.join(os.path.relpath(TMP_DIR, CURRENT_DIR),file))
