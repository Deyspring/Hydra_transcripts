#! python
# Create_excel makes an excel file with a title based on a website and the date. 

import openpyxl
from openpyxl.styles import Font
import time

#if __name__ == '__main__': #not sure what to name instead of _main_ for clarity 
 
# main()

def mng_xl(terms, geneid_lists, transcript_sets): 
	'''Excel file with a title based on a website and the date'''

	#print(terms,"/n", geneid_lists,"/n", transcript_sets)
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
	gen_num = 0
	trn_num = 0

	print("manage_excel\n")

	for term in terms: 
		# Search terms should start at cell A7, row 
		print("term:",term)

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

		for geneids in geneid_lists:
			print("geneids: ", geneids)
			for geneid in geneids:
				print ("geneid:", geneid)
				row_num += 1
				col_num = 1
				sheet.cell(row=row_num, column=col_num).value = geneid
			
				transcript_set = transcript_sets[trn_num]
				print("transcript_set ",trn_num,":", transcript_set)
				for transcripts in transcript_set:

					print("transcripts: ", transcripts)
					for transcript in transcripts: 
						print("transcript:", transcript)
						col_num +=1
						sheet.cell(row=row_num, column=col_num).value = transcript
						trn_num += 1

		gen_num += 1

	#wb.save( title+'_'+ datestamp+'.xlsx' ) # Save the workbook.
	#file_name = (title+'_'+datestamp+'.xlsx')

	print('saved workbook\n')

#Data produced by the other modules, which is correct
#When I use this data as a test case for the module, it does odd things. 
"""
terms = ['Ig_4'] 
geneids = ['Sc4wPfr_172.1.g1567.t1', 'Sc4wPfr_435.1.g6986.t1', 'Sc4wPfr_274.1.g13601.t1', 'Sc4wPfr_172.2.g23178.t1', 'Sc4wPfr_268.g25749.t1', 'Sc4wPfr_268.g25754.t2', 'Sc4wPfr_268.g25749.t2', 'Sc4wPfr_268.g25754.t1'] 
transcripts = [{'t18444aep', 't20351aep', 't1128aep', 't19864aep', 't34681aep', 't27955aep', 't5766aep', 't14414aep', 't22661aep', 't9044aep', 't12064aep', 't11261aep', 't22011aep'}, 
			   {'t36740aep', 't12260aep', 't30006aep', 't37984aep'}, 
			   {'t30122aep', 't297aep'}, 
			   {'t18444aep', 't20351aep', 't1128aep', 't19864aep', 't34681aep', 't27955aep', 't5766aep', 't14414aep', 't22661aep', 't9044aep', 't12064aep', 't11261aep', 't22011aep'}, 
			   {'t24725aep', 't27640aep', 't2308aep', 't31900aep', 't21629aep', 't12602aep', 't14827aep', 't23311aep', 't3984aep', 't27276aep', 't4494aep', 't13463aep', 't18097aep', 't36467aep', 't18096aep', 't23522aep', 't15944aep', 't26172aep', 't24866aep', 't20881aep', 't15548aep', 't439aep', 't14058aep', 't21081aep', 't1197aep'}, 
			   {'t24725aep', 't27640aep', 't2308aep', 't31900aep', 't21629aep', 't12602aep', 't14827aep', 't23311aep', 't3984aep', 't27276aep', 't4494aep', 't13463aep', 't18097aep', 't36467aep', 't18096aep', 't23522aep', 't15944aep', 't26172aep', 't24866aep', 't20881aep', 't15548aep', 't439aep', 't14058aep', 't21081aep', 't1197aep'}, 
			   {'t24725aep', 't27640aep', 't2308aep', 't31900aep', 't21629aep', 't12602aep', 't14827aep', 't23311aep', 't3984aep', 't27276aep', 't4494aep', 't13463aep', 't18097aep', 't36467aep', 't18096aep', 't23522aep', 't15944aep', 't26172aep', 't24866aep', 't20881aep', 't15548aep', 't439aep', 't14058aep', 't21081aep', 't1197aep'}, 
			   {'t24725aep', 't27640aep', 't2308aep', 't31900aep', 't21629aep', 't12602aep', 't14827aep', 't23311aep', 't3984aep', 't27276aep', 't4494aep', 't13463aep', 't18097aep', 't36467aep', 't18096aep', 't23522aep', 't15944aep', 't26172aep', 't24866aep', 't20881aep', 't15548aep', 't439aep', 't14058aep', 't21081aep', 't1197aep'}]


# The data below produces a perfect spreadsheet when the module is run. 
#However, if the structure of the lists changes, the spreadsheet is formatted incorrectly. 
"""
terms = ['term1','term2']
geneids = ['term1_gene1_2','term1_gene1_3','term1_gene1_4','term1_gene1_5'],['gene4term2_1','gene4term2_2','gene4term2_3','gene4term2_4']
transcripts = [{'term1_gene1_tr1','term1_gene1_tr2','term1_gene1_tr3','term1_gene1_tr4'},{'term1_gene2_tr1','term1_gene2_tr2','term1_gene2_tr3','term1_gene2_tr4'},{'term1_gene3_tr1','term1_gene3_tr2','term1_gene3_tr3'},{'term1_gene4_tr1','term1_gene4_tr2','term1_gene4_tr3','term1_gene4_tr4'}],[{'term2_gene1_tr1','term2_gene1_tr2','term2_gene1_tr3','term2_gene1_tr4'},{'term2_gene2_tr1','term2_gene2_tr2','term2_gene2_tr3','term2_gene2_tr4'},{'term2_gene3_tr1','term2_gene3_tr2','term2_gene3_tr3'},{'term2_gene4_tr1','term2_gene4_tr2','term2_gene4_tr3','term2_gene4_tr'}]
mng_xl(terms,geneids,transcripts)