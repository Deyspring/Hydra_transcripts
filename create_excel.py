
# Test code to create an excel file and import website data into it.

import openpyxl


#Create an excel file
wb = openpyxl.load_workbook('hydra.xlsx')

#Create a top sheet
sheet = wb.get_sheet_by_name('Sheet1')

#Make a gene identifier as a test case 
gene_Ident = sheet.cell( row = 11, column = 1 ).value

#and the transcripts associated with each gene
transcripts = ['a','b','c']

# Todo: loop through all the rows and add the gene identifiers and transcripts 

for rowNum in range(11, sheet.max_row):  # skip the first rows
	gene_Ident = sheet.cell(row=rowNum, column=1).value
	
	colNum = 2

	for i in transcripts: 
		sheet.cell(row=rowNum, column=colNum).value = i
		colNum += 1

print (sheet.cell(row=11, column=2).value)

wb.save('UpdateHydra.xlsx')
