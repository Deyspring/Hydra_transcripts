#!python3
# A little test script to enter text into the Pfam domain name searchbox, 
# and then identify a resulting link

#This code is pretty simple right now, but after the text is entered and submitted, no search items return 
#It's pretty clear the search did happen, but I'm wondering if it was too quick. 
# It does not appear to be a quickness thing
# Now I'm wondering about how the text is entered and the autocomplete java stuff. 
#And also if the search is being blocked by some sort of automatic script sensor

import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

try:
    keywordElem = browser.find_elements_by_id('keyword')
    print('Found element with that class name!' )
except:
    print('Was not able to find element with that name.')

searchBoxElem = keywordElem[1]
searchBoxElem.send_keys('ig')

time.sleep(3)

searchBoxElem.submit()
searchBoxElem.submit()


"""
try:
    submitElem = browser.find_elements_by_name('search')
    print('Found element search with that class name!' )
except:
    print('Was not able to find element with that name.')

submitElem.submit()"""

