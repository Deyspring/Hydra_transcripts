# hydra_ts.py

import time
from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

#inputString = input('Enter "ig" as a test search term: ')
#inputList = ['ig','Ig_2',''Ig_5']
#for i in inputList: 
# 	search_term = i 
	#return genetranscripts 

def search_term(term): 
	#insert search terms and return geneID names

	window_first = browser.window_handles[0] # Store window handle variable before next window
	keyword_box = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]'
	try:
		keywordElem = browser.find_element_by_xpath(keyword_box)
		print('Found keywordElem with that xpath!')
		#keywordElem.send_keys(search_term)
		keywordElem.send_keys('ig')
	except:
		print('Was not able to find keywordElem with that xpath.')

	#Click on the search button  
	buttonElm = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]'
	try:
		buttonPress = browser.find_element_by_xpath(buttonElm).click()
		print ('Found buttonPress with that xpath')
	except:
		print('Was not able to find buttonPress.')

	#return first gene id link produced by search
	resultElem = '/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a'
	geneIdElem = browser.find_element_by_xpath(resultElem).text

	gene_id = (geneIdElem.split("="))[0]
	
	return gene_id
