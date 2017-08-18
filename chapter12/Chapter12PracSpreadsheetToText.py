#! usr/bin/env python3

# Chapter 12 Practice
# Spreadsheet to Text - Takes each column of data and creates a text file
#                       with that data.

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.get_active_sheet()

for columnNum in range(1, sheet.get_highest_column()):
    spreadText = open('Column ' + str(columnNum) +'.txt', 'a')
    for rowNum in range(2, sheet.get_highest_row()):
        rowData = sheet.cell(row=rowNum, column=columnNum).value
        spreadText.write(str(rowData) + '\n')
    spreadText.close()

        
