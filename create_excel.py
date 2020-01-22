#! python
# Create_excel makes an excel file with a title based on a website and the date. 
###TODO make sure this always saves a worksheet with a different name so they don't get saved over each other.

import openpyxl
from datetime import date

title = 'Pfam Domains'
subtitle = 'Pfam domains in predicted Hydra proteins'
web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'
number = '1'

def create_header(title,subtitle,web_adress,number): # change name back to create_header after testing
#Excel file with a title based on a website and the date
	title = title.replace(" ","")
	wb = openpyxl.Workbook() # Create a blank workbook
	wb.sheetnames # It starts with one sheet
	sheet = wb.active
	sheet.title
	sheet.title = title # Change title.

	# Month abbreviation, day and year	
	datestamp = (date.today()).strftime("%b/%d/%Y")

	#Format spreadsheet
	sheet['A1'] = title
	sheet['A2'] = subtitle
	sheet['A3'] = web_address
	sheet['A5'] = datestamp 

	return wb.save( title + '_'+number +'.xlsx' ) # Save the workbook.


def update_xl(): 
	'''Update excel file with geneIDs and their transcripts'''

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

create_header(title, subtitle, web_address, number)

