#!python
#hydra_TS 
#After entering search term(s) into the Pfam domain name searchbox, a spreadsheet
#is returned with the geneIds and lists of transcripts related to that search term. 

import time
import manage_excel
import genome_browser_links 
import search_term

#Open Hydra webportal
browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')
# Store homepage window handle variable before clicking any links
hydra_homepage = browser.window_handles[0] 

# Accept user input and return a list of terms 
terms =[]
term = None

while term != 'done': 
	print('Enter "done" when done entering terms')
	term = input('Enter search term(s): ')
	if term != 'done':
		terms.append(term)
	else: 
		pass
print (terms) ### clean up 

#Enter search terms on the Hydra homepage and get the geneids. 
geneids = search_term.search_geneid(terms)  

#Make urls using geneids to click to "View Genome" page
#Click through that page to get transcripts from the JSON browser
for geneid in geneids: 
	url = genome_browser_links.gb_link(geneids) 
	transcripts = json_stripper(url)

#Put all terms, geneids and transcripts into an excel file
manage_excel(terms, geneids, transcripts)

# Close browser windows 
'''
time.sleep(5) 
browser.close()
browser.close()
browser.close()'''

#Give indication that progam is complete while testing
#remove when done
print ("Complete")