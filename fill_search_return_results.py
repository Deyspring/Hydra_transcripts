#!python3
#Script to fill the search box and open each result in a browser page. 

# This program gets the search term from the command line
# It enters the term into the search box and retrieves the resulting pages
# then opens a browser page for each result 

# The program will need to
# X Read the command line arg from sysv.arg
# X Fetch the search results page with requests module
# X Find the links to each search result
# XCall the webbrowser.open(0) function to open each result

#Ok, time to test this puppy. 


import requests, bs4, sys, webbrowser

# Read the command line argument 

print ('Hydra Portal Searching.....') #display text while downloading Hydra portal page
# Put the search request term entered on the command line into the search box (that's sys.argv)
res = requests.get('https://research.nhgri.nih.gov/hydra/pfam/' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser") # creates a text object of the results webpage 

# Attempt to isolate link attributes inside the form they are nested in
#- See README for extensive notes on how I'm 
# trying to isolate the links and grab them with Beautiful Soup
form = soup.find(lambda tag: tag.name =='form' and tag.has_attr('name') and tag['name']=="checkboxform")
print(form)
#links = form.findAll(lambda tag: tag.name=='a') #The links object created by BS is a list


# Open a browser tab for each result.
#for i in links: 
#	webbrowser.open('https://research.nhgri.nih.gov/' + link[i].get('href'))
