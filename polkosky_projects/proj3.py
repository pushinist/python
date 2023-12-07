import openpyxl

wb = openpyxl.load_workbook('Дипломанты.xlsx')
ws = wb.active

for x in ws.values():
    print(x)


wb.close()
