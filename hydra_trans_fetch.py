#!python
#hydra_TS 
#After entering search term(s) into the Pfam domain name searchbox, a spreadsheet
#is returned with the geneIds and lists of transcripts related to that search term. 

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import manage_excel
import genome_browser_links 
import search_term 
import json_stripper


# Accept user input and return a list of terms 
# use Ig_4 to bug test this program; it returns a short list of results

terms =[]
term = None

print('After entering all terms, type "done"')
print('='*20)

while term != 'done': 
	term = str(input('Enter search term(s): '))
	if (' ' not in term and len(term) != 0 and term != 'q'):
			terms.append(term)
	else : 
		print('Please enter a term or \'done\' to finish adding terms.')
	

print('Finished adding terms')	


# Open Firefox in headless(invisible), mode
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
browser = webdriver.Firefox(options=options)
print ('open browser')
print('.'* 10 )

# Enter search terms on the Hydra homepage and get the geneids. 
pfam_webportal = 'https://research.nhgri.nih.gov/hydra/pfam/'
browser.get(pfam_webportal)
geneids = search_term.search_geneid(terms,browser)  
print('.'* 10 )

# Make urls using geneids. 
# Selenium clicks through the "View Genome" page to get transcripts from the JSON browser.
transcripts =[]
for geneid in geneids: 
	url = genome_browser_links.gb_link(geneid, browser) 
	transcript_set = json_stripper.transcripts_data(url, browser)
	transcripts.append(transcript_set)

# Temporary output for testing purposes. 
print("hydra_ts terms: \n", terms)
print("hydra_ts genids:\n", geneids)
print("hydra_ts transripts:\n", transcripts)
print("close browser .... ")
browser.close()

#Put all terms and their matching geneids and transcripts into an excel file.
manage_excel.mng_xl(terms, geneids, transcripts)
