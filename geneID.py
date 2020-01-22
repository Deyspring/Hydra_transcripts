#!python
# Methods to return the geneID

def geneID_link(row_num):
	'''produce geneId link when given a value'''

	link_pt1 = '/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr['
	link_pt2 = ']/td[2]/a'
	result_link = link_pt1 + row_num + link_pt2
	return result_link


""" Do I need this module? search_pfam returns a geneID
def geneId_result(result_link): 
	''' return a string containing the geneID
	geneIdElem = browser.find_element_by_xpath(result_link).text
	geneId = (geneIdElem.split("="))[0]
	return geneID

	"""



