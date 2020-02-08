#! python
# Create_excel makes an excel file with a title based on a website and the date. 
###TODO make sure this always saves a worksheet with a different name so they don't get saved over each other.

import openpyxl
from openpyxl.styles import Font
from datetime import datetime


def create_header(): 
	'''Excel file with a title based on a website and the date'''

	#TODO? make these names and link changable in a gui? 
	title = 'Pfam Domains'   
	subtitle = 'Pfam domains in predicted Hydra proteins'
	web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'


	title = title.replace(" ","")
	wb = openpyxl.Workbook() # Create a blank workbook
	wb.sheetnames # It starts with one sheet
	sheet = wb.active
	sheet.title
	sheet.title = title # Change titles

	#Month abbreviation, day and year
	now = datetime.now()
	datestamp = now.strftime("%b_%d_%Y_%H_%M")

	#Create fonts
	title_style = Font(size=24, bold=True) 

	#Format spreadsheet
	sheet['A1'] = title
	sheet['A1'].font = title_style
	sheet['A2'] = subtitle
	sheet['A3'] = web_address
	sheet['A5'] = datestamp 
	wb.save( title+ '_' + datestamp + '.xlsx' ) # Save the workbook.
	file_name = (title+ '_' + datestamp + '.xlsx')

	row = 11
	column = 1

	print('saved workbook')
	return file_name, row, column



def term_subtitle(term, row, column):
	'''Create a subheader title from a term '''
	
	wb = openpyxl.load_workbook(file_name)
	sheet = wb.active
	

def add_data_xl(terms, geneids, transcripts): 
	
	file_name, row, column = create_header()
	row_num = row
	col_num = column
	wb = openpyxl.load_workbook(file_name)
	sheet = wb.active

	testing1 = "term"
	testing2 = "geneid"
	testing3 = "transcripts"
	sheet.cell(row=row_num, column=col_num).value = term

	for term, geneids,transcript_sets in zip(terms,geneids,transcripts): 
		#print ("term, geneids and transcript_sets for this term are: ", term,geneids,transcript_sets)
		sheet.cell(row=row_num, column=col_num).value = term # first one should be A7
		print("")
		print('term row_num, col_num: ', term, row_num,col_num)
		for geneid,transcripts in zip(geneids,transcript_sets): 
			row_num += 1
			col_num = 1
			print( 'geneid row_num, col_num: ', row_num,col_num)
			#print ("geneid, transcripts ", geneid,transcripts)
			sheet.cell(row=row_num, column=col_num).value = geneid
			#print ('')
			for transcript in transcripts:
				col_num +=1
				print('transcripts:row_num, col_num: ', row_num,col_num)
				#print ("transcript: ",transcript)
				sheet.cell(row=row_num, column=col_num).value = transcript
				sheet.cell(row=row_num, column=col_num).value = ' '

	now = datetime.now()
	datestamp = now.strftime("%b_%d_%Y_%H_%M")
	file_name.split('_')
	new_file_name = (file_name[0]+ '_' + datestamp + '.xlsx')
	wb.save(new_file_name)


terms = ['ig','pop']
geneids = [['badger','monkey','baboon','mushroom'],['badger2','monkey2','baboon2','mushroom2']]
transcripts = [['bad','bad','bad','bad'],['mon','mon','mon','mon'],['boon','boon','boon'],['mush','room','mush','room']],[['bad2','bad2','bad2','bad2'],['mon2','mon2','mon2','mon2'],['boon2','boon2','boon2'],['mush2','room2','mush2','room2']]

#row =7
#column =1

add_data_xl(terms,geneids,transcripts) 


