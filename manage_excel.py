#! python
# Create_excel makes an excel file with a title based on a website and the date. 

import openpyxl
from openpyxl.styles import Font
import time

#if __name__ == '__main__': #not sure what to name instead of _main_ for clarity 
 
# main()

def mng_xl(terms, geneid_lists, transcript_sets): 
	'''Excel file with a title based on a website and the date'''

	#TODO? make these names and link changable in a gui? 
	title = 'Pfam_Domains'   
	subtitle = 'Pfam domains in predicted Hydra proteins'
	web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'
	datestamp = time.strftime("%Y-%m-%d %H:%M")

	title = title.replace(' ','')
	wb = openpyxl.Workbook() # Create a blank workbook
	wb.sheetnames # It starts with one sheet
	sheet = wb.active
	sheet.title
	sheet.title = title 

	#Create fonts
	title_style = Font(size=24, bold=True) 
	term_style = Font(size =16, bold = True)
	term_sub_style = Font(size =16)
	geneid_style = Font(size=14, bold = True)
	transcript_style = Font(size=12, bold = True)

	#Format spreadsheet
	sheet['A1'] = title
	sheet['A1'].font = title_style
	sheet['A2'] = subtitle
	sheet['A3'] = web_address
	sheet['A5'] = datestamp 
	blank_cell= " "
	
	row_num = 6
	col_num = 1

	print("manage_excel\n")

	for term, geneid_list, transcript_set in zip(terms,geneid_lists,transcript_sets): 
		# Search terms should start at cell A7, row 1
		col_num = 1
		row_num += 2
		sheet.cell(row=row_num, column=col_num).font = term_style
		sheet.cell(row=row_num, column=col_num).value = "TERM"
		row_num += 1
		sheet.cell(row=row_num, column=col_num).font = term_sub_style
		sheet.cell(row=row_num, column=col_num).value = term

		row_num += 1
		sheet.cell(row=row_num, column=col_num).font = geneid_style
		sheet.cell(row=row_num, column=col_num).value = "Geneids"
		col_num +=1
		sheet.cell(row=row_num, column=col_num).font = transcript_style
		sheet.cell(row=row_num, column=col_num).value = "transcripts"
		col_num -=1 


		for geneid,transcripts in zip(geneid_list, transcript_set):
			row_num += 1
			col_num = 1
			sheet.cell(row=row_num, column=col_num).value = geneid
	
			for transcript in transcripts:
				col_num +=1
				sheet.cell(row=row_num, column=col_num).value = transcript
	
	wb.save( title+'_'+ datestamp+'.xlsx' ) # Save the workbook.
	file_name = (title+'_'+datestamp+'.xlsx')

	print('saved workbook\n')


'''
terms = ['ig','pop']
geneids = [['badger','monkey','baboon','mushroom'],['pidgeon','donkey','hedgehog','duck']]
transcripts = [{'bad','bad3','bad4','bad5'},{'mon1','mon2','mon3','mon4'},{'boon1','boon2','boon3'},{'mush1','mush2','mush3','mush4'}],[{'feed1','feed2','feed3','feed4'},{'cheese1','cheese2','cheese3','cheese4'},{'bread1','bread2','bread3'},{'chard1','chard2','chard3','chard4'}]

mng_xl(terms,geneids,transcripts) 
'''