#!python
#hydra_TS 
#After entering search term(s) into the Pfam domain name searchbox, a spreadsheet
#is returned with the geneIds and lists of transcripts related to that search term. 

import time
from selenium import webdriver
import manage_excel
import get_link_to_genome_browser 
import search_term


#Prompt for list of search terms 
terms = input('Enter search term(s): ') #Change this so list of search terms are accepted. 
# enter a search term, or enter "Done"
# try except loop to make terms list


# Open Hydra web portal
browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')
window_first = browser.window_handles[0] # Store the window handle variable before clicking any links

#Enter search terms and get geneids. 
for term in terms: 
	#Search term entered; returns list of geneids 
	geneids = search_term.search_geneid(term)
	
	for geneid in geneids: 
		url = get_link_to_genome_browser(geneid)
		transcripts = json_stripper(url)

manage_excel(terms, geneids, transcripts)

#TODO close browser windows


#Give indication that proram is complete