# python!
# Create_excel makes an excel file with a title based on a website and the date. 
###TODO make sure this always saves a worksheet with a different name so they don't get saved over each other.

import openpyxl
import time

title = 'Pfam Domains'
subtitle = 'Pfam domains in predicted Hydra proteins'
number = '1'

def create_header(title,subtitle):
#Excel file with a title based on a website and the date
	
	wb = openpyxl.Workbook() # Create a blank workbook
 	wb.sheetnames # It starts with one sheet
  	sheet = wb.active
  	sheet.title
  	sheet.title = title # Change title.
  	wb.save( title + '_'+number +'.xlsx') # Save the workbook.

 	return 

