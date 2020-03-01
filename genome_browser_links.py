#!python
# genome_browser_links
# This module is necessary because a link is generated here with an gene id extenstion I 
# can't figure out. So, the link on this page just has to be clicked. :P 

import time
from selenium import webdriver
import json, requests, sys, pprint

def gb_link(geneids): 

	pass
	"""

	'Takes a gene id and clicks through _View Gene in Genome Browser_ webpage to jbrowser'
	
	gene_sequence_page = browser.window_handles[0]
	browser = webdriver.Firefox()
	url = 'https://research.nhgri.nih.gov/hydra/genewiki/gene_page.cgi?gene=' + gene_id
	browser.get(url)
	time.sleep(2)

	# Click the 'View Gene in Genome Browser link' - it seems to be the only way to get the correct json file
	try:
		link_to_genome = browser.find_element_by_link_text('View Gene in Genome Browser').click()
		print ('Found View_gene_elem with that xpath')
	except:
		print('Was not able to find View_gene_elem')
	browser.close()

	###JBrowser page: window_second
	Jbrowser_page = browser.window_handles[1] # After clicking the result button, store the window handle variable of second page
	browser.switch_to.window(window_second)

	# This is crucial!!! If the browser does not have time to load the second page, 
	# the handle will not be reset to the correct page. Sleep time may need to be lengthened if browser takes too long to load
	# this may be a good thing to put in a try except to retry finding the link if it is not found immediately. 
	time.sleep(8)

	try:
		JulianoCheckbox = browser.find_element_by_xpath(
		'/html/body/div[2]/div[4]/div[5]/div[2]/div/div/label[2]/input').click()
		print ('Found JulianoCheckbox')	
	except:
		print('Was not able to find JulianoCheckbox')
 
	browser.refresh()

	short_gene_id = gene_id.split('.')
	jbrowse_url = 'https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/'\
				  + short_gene_id[0] + '/trackData.json'

	print (jbrowse_url)
	return jbrowse_url
	"""


