# python!
# Description needed


def search_geneid(term): 
	'''input a search term and return a geneID'''
	pass # stub for testing 

'''
	# Find the keyword field and enter the term 
	keyword_box = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]'
	try:
		keywordElem = browser.find_element_by_xpath(keyword_box)
		print('Found keywordElem with that xpath!')
	except:
		print('Was not able to find keywordElem with that xpath.')

	keywordElem.send_keys(term)

	button = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]'
	try:
		buttonElm = browser.find_element_by_xpath(button).click()
		print ('Found buttonElm with that xpath')
	except:
		print('Was not able to find buttonPress.')

	#Return geneid links produced by search
	row = 3

	while True: 
		result_link = '/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[row]/td[2]/a'
		geneIdElem = browser.find_element_by_xpath(result_link).text
		gene_ids = gene_ids.append((geneIdElem.split("="))[0])
		row +=1
	else: 
		print('geneids in list')
	
	return gene_ids
'''



