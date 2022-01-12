from openpyxl import load_workbook

path = './excel/Lista-de-Municipios.xlsx';
e_file = load_workbook(path);

sheet = e_file.active;