#!python
#hydra_TS 
#After entering search term(s) into the Pfam domain name searchbox, a spreadsheet
#is returned with the geneIds and lists of transcripts related to that search term. 

import time
from selenium import webdriver
import manage_excel
import get_link_to_genome_browser 
import search_term

# Accept user input and return a list of terms 
terms =[]
term = None

while term != 'done': 
	print('Enter "done" when done entering terms')
	term = input('Enter search term(s): ')
	terms.append(term)

print (terms)

# Open Hydra web portal
browser = webdriver.Firefox()
print("browser")
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')
window_first = browser.window_handles[0] # Store the window handle variable before clicking any links

#Enter search terms and get geneids. 
geneids = search_term.search_geneid(terms)  
	
for geneid in geneids: 
	url = get_link_to_genome_browser(geneid)
	transcripts = json_stripper(url)

manage_excel(terms, geneids, transcripts)

#TODO close browser windows


#Give indication that proram is complete