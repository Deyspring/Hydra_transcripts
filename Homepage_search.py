#!python3
# A little test script to enter text into the Pfam domain name searchbox, 
# and then identify a resulting link

#This code is pretty simple right now, but after the text is entered and submitted, no search items return 
# Something happens, the browser refreshes, but nothing else. 
# Now I'm wondering about how the text is entered and the autocomplete java stuff. 
# And also if the search is being blocked by some sort of automatic script sensor

#I'm going to try the Firefox driver and see if that makes any difference - nope!
# After a bit more careful peering at the html, I noticed the onkeyup option and did 
# research I wish I'd done sooner. It was triggering the execution of some javascript. 
# Solution below. 
#Fuck yeah! sucess!!! I used the click() method and pinpointed the elements using xpath
#The element's xpaths can be copied in the developer window after selecting them. 

#next, sectecting one gene id link and putting that link name in a spreadsheet. make this a separate method

import time

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

try:
	searchElem = browser.find_element_by_xpath('/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]')
    #print('Found element with that class name!')
   
except:
    print('Was not able to find element with that name.')

searchElem.send_keys('ig')
#Click on the search button to activate search. 
buttonPress = browser.find_element_by_xpath('/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]').click()

resultElms = browser.find_element_by_xpath("/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a").click()  

# Search result
# Select a link and click it. - seems like it will be easier to clean up the resulting link
#browser.find_element_by_tag_name('a')

try:
	resultElms = browser.find_element_by_xpath("/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a").click()
	print ('Found elements')
	
except:
    print('Was not able to find element with that name.')

#https://research.nhgri.nih.gov/hydra/jbrowse/display_jbrowse.cgi?loc=Sc4wPfr_1127.1%3A428978..461136&tracks=augustus%2Cscaffold&highlight=
time.sleep(5) # This allows me a good amount of time to look at the results before closing browser. 
browser.close() # If I don't close the browser, they pile up

target = "_blank"



