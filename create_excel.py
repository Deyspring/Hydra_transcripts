#! python
# Create_excel makes an excel file with a title based on a website and the date. 
###TODO make sure this always saves a worksheet with a different name so they don't get saved over each other.

import openpyxl
from datetime import date
import os

title = 'Pfam Domains'
subtitle = 'Pfam domains in predicted Hydra proteins'
web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'
number = '1'

def new_filename(): #eventally have it take create_header return 
	'''Make sure the new excel file created does not have the same name as one that exists'''

	xl_names = [x for x in os.listdir() if x.endswith(".xlsx")]
	print(xl_names)

	new_filename = input('Enter new spreadsheet name: ')

	for filename in xl_names: 
		print (filename)
		if filename == 'new_filename':
			print ('A file with that name exists.') 
		
	print(new_filename + "new_filename")
	return 

while True:
    value = raw_input('Enter new spreadsheet name: ')
    try:
       value == old_value)
    except ValueError:
       print 'Valid number, please'
       continue
    if 0 <= value <= 100:
       break
    else:
       print 'Valid range, please: 0-100'





def create_header(title,subtitle,web_adress,number): 
	'''Excel file with a title based on a website and the date'''
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

	return wb.save( title + '_'+ number +'.xlsx' ) # Save the workbook.


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

#create_header(title, subtitle, web_address, number)
new_filename()

