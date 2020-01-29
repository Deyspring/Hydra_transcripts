#!python
# get_link_to_genome_browser 
# This module is necessary because a link is generated here with an gene id extenstion I 
# can't figure out. So, the link on this page just has to be clicked. :P 

pass #stub for testing 

import time
from selenium import webdriver
import json, requests, sys, pprint

#browser = webdriver.Firefox()

def gb_link(browser, gene_id): 
	'Takes a gene id and clicks through _View Gene in Genome Browser_ webpage to jbrowser'
	pass
	"""
	#Gene page: window_one
	window_first = browser.window_handles[0] # Store the window handle variable before clicking any links
	print("window_first")

	url = 'https://research.nhgri.nih.gov/hydra/genewiki/gene_page.cgi?gene=' + gene_id
	browser.get(url)
	time.sleep(1)
	print ('window 1 sleeping .... ')

	# Click the 'View Gene in Genome Browser link' - it seems to be the only way to get the correct json file
	try:
		link_to_genome = browser.find_element_by_link_text('View Gene in Genome Browser').click()
		print ('Found link_to_genome with that xpath')
	except:
		print('Was not able to find link_to_genome')
	browser.close()

	###JBrowser page: window_second
	window_second = browser.window_handles[0] # After clicking the result button, store the window handle variable of second page
	browser.switch_to.window(window_second)

	# This is crucial!!! If the browser does not have time to load the second page, 
	# the handle will not be reset to the correct page. Sleep time may need to be lengthened if browser takes too long to load
	# this may be a good thing to put in a try except to retry finding the link if it is not found immediately. 
	time.sleep(8)
	print("window_second sleeping... ")

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


get_link_to_genome_browser(browser,'Sc4wPfr_1127.1.g1468.t2')

time.sleep(5) 
browser.close()

gene_ids = ['Sc4wPfr_1127.1.g1468.t2', 'Sc4wPfr_1127.1.g1468.t1', 'Sc4wPfr_172.1.g1573.t1', 'Sc4wPfr_172.1.g1567.t1', 'Sc4wPfr_424.1.g2114.t1', 'Sc4wPfr_708.g2567.t1', 'Sc4wPfr_708.g2561.t1', 'Sc4wPfr_1357.1.g3221.t1', 'Sc4wPfr_758.g3713.t1', 'Sc4wPfr_758.g3713.t2', 'Sc4wPfr_435.1.g6986.t1', 'Sc4wPfr_307.g9631.t1', 'Sc4wPfr_1300.g9811.t1', 'Sc4wPfr_1300.g9811.t2', 'Sc4wPfr_178.g10676.t1', 'Sc4wPfr_309.g10789.t1', 'Sc4wPfr_309.g10788.t1', 'Sc4wPfr_197.g11018.t1', 'Sc4wPfr_96.g11969.t1', 'Sc4wPfr_96.g11963.t1', 'Sc4wPfr_96.g11965.t1', 'Sc4wPfr_720.g12291.t1', 'Sc4wPfr_124.g12319.t1', 'Sc4wPfr_304.2.g12749.t1', 'Sc4wPfr_729.g12871.t2', 'Sc4wPfr_729.g12871.t1', 'Sc4wPfr_274.1.g13601.t1', 'Sc4wPfr_138.g13918.t1', 'Sc4wPfr_250.g16094.t1', 'Sc4wPfr_875.1.g17139.t1', 'Sc4wPfr_811.1.g17337.t1', 'Sc4wPfr_854.g18494.t1', 'Sc4wPfr_66.g19053.t1', 'Sc4wPfr_66.g19052.t1', 'Sc4wPfr_347.g19288.t3', 'Sc4wPfr_347.g19288.t1', 'Sc4wPfr_347.g19288.t2', 'Sc4wPfr_95.2.g19499.t1', 'Sc4wPfr_95.2.g19498.t1', 'Sc4wPfr_132.g22649.t1', 'Sc4wPfr_132.g22677.t1', 'Sc4wPfr_132.g22677.t2', 'Sc4wPfr_378.g22720.t1', 'Sc4wPfr_378.g22717.t2', 'Sc4wPfr_378.g22717.t1', 'Sc4wPfr_172.2.g23178.t1', 'Sc4wPfr_106.g23594.t1', 'Sc4wPfr_293.g24406.t1', 'Sc4wPfr_384.g24768.t1', 'Sc4wPfr_384.g24766.t1', 'Sc4wPfr_268.g25749.t1', 'Sc4wPfr_268.g25749.t2', 'Sc4wPfr_268.g25756.t1', 'Sc4wPfr_268.g25754.t1', 'Sc4wPfr_268.g25754.t2', 'Sc4wPfr_338.g25873.t1', 'Sc4wPfr_705.g26924.t1', 'Sc4wPfr_599.g27237.t1', 'Sc4wPfr_599.g27237.t2', 'Sc4wPfr_599.g27237.t3', 'Sc4wPfr_287.2.g28208.t1', 'Sc4wPfr_199.g28577.t2', 'Sc4wPfr_199.g28594.t1', 'Sc4wPfr_199.g28577.t1', 'Sc4wPfr_199.g28578.t1', 'Sc4wPfr_1301.g29099.t1', 'Sc4wPfr_624.g29791.t1', 'Sc4wPfr_463.g30865.t1', 'Sc4wPfr_1077.g31033.t1', 'Sc4wPfr_7.g33202.t1', 'Sc4wPfr_844.g33356.t1']
"""