#!python3
# A little test script to enter text into the Pfam domain name searchbox, 
# and then identify a resulting link

#This code is pretty simple right now, but after the text is entered and submitted, no search items return 
# Something happens, the browser refreshes, but nothing else. 
# Now I'm wondering about how the text is entered and the autocomplete java stuff. 
# And also if the search is being blocked by some sort of automatic script sensor

#I'm going to try the Firefox driver and see if that makes any difference

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

try:
    keywordElem = browser.find_elements_by_id('keyword')
    print('Found element with that class name!' )
    print(keywordElem[0].text + "keywordElem") #keyword Elem is apparently blank

except:
    print('Was not able to find element with that name.')

searchBoxElem = keywordElem[1]
searchBoxElem.send_keys('ig')


searchBoxElem.send_keys(Keys.RIGHT)
searchBoxElem.send_keys(Keys.RIGHT)
searchBoxElem.send_keys(Keys.ENTER)
print('pressed return')
#searchBoxElem.submit()

time.sleep(10) # This allows me a good amount of time to look at the results before closing browser. 
browser.close() # If I don't close the browser, they pile up
quit()
