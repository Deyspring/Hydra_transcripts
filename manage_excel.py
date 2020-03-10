#! python
# Create_excel makes an excel file with a title based on a website and the date. 

import openpyxl
from openpyxl.styles import Font
import time

if __name__ == '__main__': #not sure what to name instead of _main_ for clarity 
  main()

def mng_xl(terms, geneids, transcripts): 
	'''Excel file with a title based on a website and the date'''

	#TODO? make these names and link changable in a gui? 
	title = 'Pfam_Domains'   
	subtitle = 'Pfam domains in predicted Hydra proteins'
	web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'
	datestamp = time.strftime("%Y-%m-%d %H:%M")

	title = title.replace(" ","")
	wb = openpyxl.Workbook() # Create a blank workbook
	wb.sheetnames # It starts with one sheet
	sheet = wb.active
	sheet.title
	sheet.title = title 

	#Create fonts
	title_style = Font(size=24, bold=True) 

	#Format spreadsheet
	sheet['A1'] = title
	sheet['A1'].font = title_style
	sheet['A2'] = subtitle
	sheet['A3'] = web_address
	sheet['A5'] = datestamp 
	
	row_num = 6
	col_num = 1

	for term, geneids,transcript_sets in zip(terms,geneids,transcripts): 
		col_num = 1
		# Search terms should start at cell A7
		sheet.cell(row=row_num, column=col_num).value = term 
		for geneid,transcripts in zip(geneids,transcript_sets): 
			row_num += 1
			col_num = 1
			sheet.cell(row=row_num, column=col_num).value = geneid
			for transcript in transcripts:
				col_num +=1
				sheet.cell(row=row_num, column=col_num).value = transcript
	
	wb.save( title+'_'+ datestamp+'.xlsx' ) # Save the workbook.
	file_name = (title+'_'+datestamp+'.xlsx')

	print('saved workbook')

"""
terms = ['ig','pop']
geneids = [['badger','monkey','baboon','mushroom'],['badger2','monkey2','baboon2','mushroom2']]
transcripts = [['bad','bad','bad','bad'],['mon','mon','mon','mon'],['boon','boon','boon'],['mush','room','mush','room']],[['bad2','bad2','bad2','bad2'],['mon2','mon2','mon2','mon2'],['boon2','boon2','boon2'],['mush2','room2','mush2','room2']]

manage_excel(terms,geneids,transcripts) 
"""


