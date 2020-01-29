#!python
#hydra_TS 
#After entering search term(s) into the Pfam domain name searchbox, a spreadsheet
#is returned with the geneIds and lists of transcripts related to that search term. 

import time
from selenium import webdriver
import create_excel
import update_excel
import get_link_to_genome_browser as gl
import search_term
import json_stripper2

#TODO
# create_excel 
# easy way to do this would be to incorporate date/time into filename. Shrug
# make spreadsheet header and make sure it has a different name than previous spreadsheets. 
# Not sure exactly how to do this. # gave this a shot, struggled, moving on. 

#Prompt for list of search terms 
terms = []
terms.append(input('Enter search term(s): '))

# Open Hydra web portal
browser = webdriver.Firefox()
#browser.get('https://research.nhgri.nih.gov/hydra/pfam/')
#window_first = browser.window_handles[0] # Store the window handle variable before clicking any links

#Enter search terms and get geneid lists

geneids = [] # geneid list for all terms
			 # I almost want this to be a dictionary, with term and list of all geneids. 

for term in terms: 
	#TODO Enter the search term on the spreadsheet as a header for all the gene_ids and transcripts to follow. 
	#term_header(term) #TODO module for just adding term header

	#TODO: search search term entered; gene ids returns rm testrm Jreturns list of stripped gene ids 
	geneid = search_term.search_geneid(term)
	geneid = term 
	geneids.append(geneid)

	#TODO : For each geneid, go to Jbrowse to get the transcripts
	n = 0 

print (geneids)

for geneid in geneids: 
	print (geneids)
	print ('monkey')
	url = gl.gb_link(browser, geneid)
	transcripts = json_stripper2.transcripts_from_Json(url)


#TODO put a geneid in the spreadsheet with it's transcripts
#TODO close browser windows


#TODO save and close spreadsheet Give indication that proram is complete