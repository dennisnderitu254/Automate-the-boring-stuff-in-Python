#! python3

# Chapter 14 Practice Excel to CSV Converter
# Converts all Excel file sheets in the current directory to CSV files

import os
import csv
import openpyxl

for excelFile in os.listdir('.'):
    if excelFile.endswith('.xlsx'):
        wb = openpyxl.load_workbook(excelFile)
        for sheetName in wb.get_sheet_names():
            sheet = wb.get_sheet_by_name(sheetName)
            csvFileName = open(excelFile + sheetName + '.csv', 'w', newline='')
            csvFile = csv.writer(csvFileName)

            for rowNum in range(1, sheet.get_highest_row() + 1):
                rowData = []
                for colNum in range(1, sheet.get_highest_column() + 1):
                    cellData = sheet.cell(row=rowNum, column=colNum).value
                    rowData.append(cellData)

                csvFile.writerow(rowData)

            csvFileName.close()
