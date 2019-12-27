#!python3
#Script to fill the search box and open each result in a browser page. 

# This program gets the search term from the command line
# It enters the term into the search box and retrieves the resulting pages
# then opens a browser page for each result 

# The program will need to
# Read the command line arg from sysv.arg
# Fetch the search results page with requests module
# Find the links to each search result
# Call the webbrowser.open(0) function to open each result


import requests, bs4, sys, webbrowser

# Read the command line argument 

print ('Hydra Portal 2.0 .....') #display text while downloading Hydra portal page
# Put the search request term entered on the command line into the search box
res = requests.get('https://research.nhgri.nih.gov/hydra/genewiki/gene_page.cgi?gene='+' '.join(sys.argv[ 1:]))
res.raise_for_status()

# TODO: Retrieve search result links.

soup = bs4.BeautifulSoup(res.text) # create a text object of the result webpage 

table = soup.find_all('table')[0] # Select the first table on the website, which has the Gene Identity links desired. 

row_marker = 0
for row in table.find_all('tr'):
	column_marker = 0 
	columns = row.find_all('td')
	for column in columns: 
		linkGeneID = column.select('a')
		webbrowser.open('https://research.nhgri.nih.gov/' + linkGeneID.get('href'))
		column_marker += 1 
	row_marker += 1

# TODO: Open a browser tab for each result.

 	#webbrowser.open('https://research.nhgri.nih.gov/' + linkGeneID[i].get('href'))
