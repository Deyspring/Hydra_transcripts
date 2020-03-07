# python!
# Takes a list of terms, enters them into the search box, clicks the button and then finds all the resulting
# links and returns them a list, ** with the browser ** I'm not sure this module should do that, we'll see. 

import time
from selenium import webdriver

def search_geneid(terms): 
	'''Input a search term and return a geneid'''
	# use Ig_4 to test 

	#Open Hydra webportal
	browser = webdriver.Firefox()
	browser.get('https://research.nhgri.nih.gov/hydra/pfam/')
	hydra_homepage = browser.window_handles[0] # Store the window handle variable before clicking any links

	# Find the keyword field and enter the term 
	keyword_box = '//div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]'
	try:
		keywordElem = browser.find_element_by_xpath(keyword_box)
		print('Found keywordElem with that xpath!')
	except:
		print('Was not able to find keywordElem with that xpath.')

	for term in terms: 
		keywordElem.send_keys(term)
		button = '//div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]'
		try:
			buttonElm = browser.find_element_by_xpath(button).click()
			print ('Found buttonElm with that xpath')
		except:
			print('Was not able to find buttonPress.')

		#If, for some reason, the links can't be found, it could be due to the website loading slowly. Time.sleep()
		#gives the browser time to complete loading. 
		time.sleep(3) 
		
		#Return geneid links produced by search
		geneids =[]
		row = 3
		link = None
		
		result_link = '//div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[*]/td[2]/a'

		for link in browser.find_elements_by_xpath(result_link): 
			geneid = link.text
			geneids.append((geneid.split("="))[0]) # split the geneid to provide id to make gene sequence page url 
			print(".", end ="")

		print(".")
		print(geneids)
		print('Found all geneids; put in list') #if no gene ids, give error code 
	
	#Uncomment for module testing
	#	time.sleep(5) 
	#	browser.close()
	
		return geneids, hydra_homepage

#for testing
"""

terms = ['ig', 'Ig_2']
geneids = [['badger','badger2','mushroom','mushroom2'], ['monkey','rat','boar','ox','moon']]
transcripts = [[['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']]]

search_geneid(terms)
"""




