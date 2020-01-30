#! python
# Create_excel makes an excel file with a title based on a website and the date. 
###TODO make sure this always saves a worksheet with a different name so they don't get saved over each other.

import openpyxl
from datetime import date
import os
from openpyxl.styles import Font
import pdb # debugging module
#pdb.set_trace()


title = 'Pfam Domains'
subtitle = 'Pfam domains in predicted Hydra proteins'
web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'

#pass #stub for testing

def create_header(title,subtitle,web_adress): 
	'''Excel file with a title based on a website and the date'''

	title = title.replace(" ","")
	wb = openpyxl.Workbook() # Create a blank workbook
	wb.sheetnames # It starts with one sheet
	sheet = wb.active
	sheet.title
	sheet.title = title # Change titles

	#Month abbreviation, day and year	
	datestamp = (date.today()).strftime("%b_%d_%Y")

	#Create fonts
	title_style = Font(size=24, bold=True) 

	#Format spreadsheet
	sheet['A1'] = title
	sheet['A1'].font = title_style
	sheet['A2'] = subtitle
	sheet['A3'] = web_address
	sheet['A5'] = datestamp 
	wb.save( title+ '_' + datestamp + '.xlsx' ) # Save the workbook.
	print('saved workbook')
	return 

def update_xl(search_term, geneids, transcripts): 
	'''Update excel file with a search term and it's resulting geneids and transcripts'''
	# Search term 
	search_term_header = sheet.cell(row = 11, column =1).value
	#Make a gene identifier as a test case 
	geneid_cell = sheet.cell( row = 12, column = 1 ).value

	#and the transcripts associated with each gene
	transcript_cell = ['a','b','c']

	# Todo: loop through all the rows and add the gene identifiers and transcripts 

	for rowNum in range(11, sheet.max_row):  # skip the first rows
		gene_Ident = sheet.cell(row=rowNum, column=1).value
	
		colNum = 2

	for i in transcripts: 
		sheet.cell(row=rowNum, column=colNum).value = i
		colNum += 1

	print (sheet.cell(row=11, column=2).value)

	wb.save('UpdateHydra.xlsx')

create_header(title, subtitle, web_address)
#new_filename()

