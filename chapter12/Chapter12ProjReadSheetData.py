#! /usr/bin/env python3

# Chapter 12 Project Reading Spreadsheet Data
# Tabulates population and number of census tracts for each county from
# censuspopdata.xlsx.

import openpyxl
import pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # Make sure key for state exists
    countyData.setdefault(state, {})
    # Make sure the key for this county exists
    countyData[state].setdefault(county, {'tracts':0, 'pop':0})
    # Each row represents one census tract so increment by one
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

