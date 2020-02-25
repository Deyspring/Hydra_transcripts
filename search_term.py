# python!
# Description needed

import time


def search_geneid(terms): 
	'''Input a search term and return a geneid'''
	
	geneids =[]
	# Find the keyword field and enter the term 
	keyword_box = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]'
	try:
		keywordElem = browser.find_element_by_xpath(keyword_box)
		print('Found keywordElem with that xpath!')
	except:
		print('Was not able to find keywordElem with that xpath.')

	for term in terms: 
		keywordElem.send_keys(term)
		button = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]'
		try:
			buttonElm = browser.find_element_by_xpath(button).click()
			print ('Found buttonElm with that xpath')
		except:
			print('Was not able to find buttonPress.')

		#If, for some reason, the links can't be found, it could be due to the website loading slowly. Time.sleep()
		#gives the browser time to complete loading. 
		time.sleep(3) 
		
		#Return geneid links produced by search
		row = 3
		should_continue = True

		while should_continue : 
			#row value indicates where geneid is
			row +=1
			try :
				result_link = '/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr['+str(row)+']/td[2]/a'
				print('Found result_link!' + str(row))
				print(str(browser.find_element_by_xpath(result_link).text))
			except:
				print('End of result_links')
				break
			
			time.sleep(2) 
			geneid_elem = str(browser.find_element_by_xpath(result_link).text)
			geneids.append((geneid_elem.split("="))[0]) # Why am i trying to split the geneid? ?? can't remember
		
		print('Found all geneids; put in list') #if no gene ids, give error code 

		#Not sure if it's a good idea to close this window right now, I'll think about it. 
		time.sleep(5) 
		browser.close()
	
		return geneids

#for testing
#Open Hydra web portal
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')
window_first = browser.window_handles[0] # Store the window handle variable before clicking any links

terms = ['ig', 'Ig_2']
geneids = [['badger','badger2','mushroom','mushroom2'], ['monkey','rat','boar','ox','moon']]
transcripts = [[['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']]]

search_geneid(terms)
"""




