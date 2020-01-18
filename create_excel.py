# python!
# Create_excel makes an excel file with a title based on a website and the date. 
###TODO make sure this always saves a worksheet with a different name so they don't get saved over each other.

import openpyxl
from datetime import date

title = 'Pfam Domains'
subtitle = 'Pfam domains in predicted Hydra proteins'
web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'
number = '1'

def create_header(title,subtitle,web_adress,number):
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

create_header(title, subtitle, web_address, number)

