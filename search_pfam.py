#! python
# search_term enters terms on the Pfam Domain page for Hydra

import time
from selenium import webdriver
import get_link_to_genome_browser 

browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

###Home page: window_first
window_first = browser.window_handles[0] # Store the window handle variable before clicking any links
print("window_first")

input_string = input('Enter "ig" as a test search term: ')

#search term returns a list of gene_ids
gene_ids = search_term('input_string')

###Gene page: window_second

def get_link_to_genome_browser(browser, gene_id): 
	'Takes a gene id and clicks through _View Gene in Genome Browser_ webpage to jbrowser'

   	gene_browser_id = link_to_genome.split('=augustus')
   	jbrowse_url = gene_browser_id[0] +'%2Cscaffold%2CaepLRv2_splign&highlight='

   	return jbrowse_url


def search_term(term): 
	'''input a search term and return a list of gene_ids'''

	if type(term) != str:
		raise not_string_error('the search term is not a string') 

	# Find the keyword field and enter the term 
	keyword_box = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]'
	
	try:
		keyword_elem = browser.find_element_by_xpath(keyword_box)
		print('Found keyword_elem with that xpath!')
		keyword_elem.send_keys(term)
		print(term)
	except:
		print('Was not able to find keyword_elem with that xpath.')

	#Click on the search button  
	button = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]'
	
	try:
		button_elm = browser.find_element_by_xpath(button).click()
		print ('Found button_elm with that xpath')
	except:
		print('Was not able to find button_elm.')


	###### geneID loop
	#result_link = '/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a'
	gene_ids = []
	gene_id = 'test'
	n = 3
	#collect all links into a list, separate link following from link collection. 
	while True: 

		result_link = '/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr['\
						+ str(n) + ']/td[2]/a'
		try: 
			result_elm = browser.find_element_by_xpath(result_link)
			print('Found result_elm with that xpath')
		except: 
			print('Was not able to find the result_elm')
			break 

		gene_id = browser.find_element_by_xpath(result_link).text
		gene_ids.append(gene_id)
		n += 1	

	print (gene_ids)
	return gene_ids

	transcripts_from_Json(gene_ids)

	print (transcripts)



class NotStringError(ValueError): 
	pass   

search_term('ig')
time.sleep(5) 
browser.close()

