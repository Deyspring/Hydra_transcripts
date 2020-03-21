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
	print("Transcript_sets:", transcript_sets)
	for term, geneid_list, transcript_set in zip(terms,geneid_lists,transcript_sets): 
		col_num = 1
		# Search terms should start at cell A7
		print("term: ",term)
		print("geneids_list: ", geneid_list)
		#print("transcript_set", transcript_set)
		#sheet.cell(row=row_num, column=col_num).value = blank_cell
		row_num += 1
		sheet.cell(row=row_num, column=col_num).value = term 

		for geneid,transcripts in zip(geneid_list, transcript_set):
			print('geneid: ', geneid) 
			print('transcripts :', transcripts)
			row_num += 1
			col_num = 1
			sheet.cell(row=row_num, column=col_num).value = geneid

			for transcript in transcripts:
				print("transcript:", transcript)
				col_num +=1
				sheet.cell(row=row_num, column=col_num).value = transcript
	
	wb.save( title+'_'+ datestamp+'.xlsx' ) # Save the workbook.
	file_name = (title+'_'+datestamp+'.xlsx')

	print('saved workbook')


terms = ['ig','pop']
geneids = [['badger','monkey','baboon','mushroom'],['pidgeon','donkey','hedgehog','duck']]
transcripts = [{'bad','bad3','bad4','bad5'},{'mon1','mon2','mon3','mon4'},{'boon1','boon2','boon3'},{'mush1','mush2','mush3','mush4'}],[{'feed1','feed2','feed3','feed4'},{'cheese1','cheese2','cheese3','cheese4'},{'bread1','bread2','bread3'},{'chard1','chard2','chard3','chard4'}]

mng_xl(terms,geneids,transcripts) 




