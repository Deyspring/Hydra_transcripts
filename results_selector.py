# python3!
# This is a small script to select all links that are results of a search
# The gene id will be inserted into a spreadsheet
# The link will be clicked to lead to the gene id's transcripts? maybe
#I can't even start this, this page won't even show up until the search is run. 


from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

try:
    keywordElems = browser.find_elements_by_id('keyword')
    print('Found element with that class name!' )
except:
    print('Was not able to find element with that name.')

https://research.nhgri.nih.gov/hydra/genewiki/gene_page.cgi?