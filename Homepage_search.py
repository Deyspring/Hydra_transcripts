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

#After doing some reading I realized that my xpaths are absolute and should be changed to relative. 
#I'm trying to figure out the best way to select the gene id name, which does not have a tag or id attached to it. 
#This may require a chained? xpath. Xpaths are going to be my main way of finding elements on this website. :P 
# First, change absolute links to relative ones. 
#Ok, I tried to change the absolute links to relative ones and that did not work. The relative link would not allow a keyword to be entered into the search bar, for instance. 

#An unsatisfying day of coding, however while cleaning up my project space I realized that I'd entirely forgotten about using 
#an API to get the table data and gene fragments. Tomorrow's quest then. 

import time

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

try:
	keywordElem = browser.find_element_by_xpath('/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]')
	print('Found keywordElem with that xpath!')
except:
    print('Was not able to find keywordElem.')

keywordElem.send_keys('ig')

#Click on the search button  
try:
	buttonPress = browser.find_element_by_xpath('/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]').click()
	print ('Found buttonPress with that xpath')
except:
    print('Was not able to find buttonPress.')

# Click on gene id link returned by search 
try:
	resultElms = browser.find_element_by_xpath('/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a').click()
	print ('Found resultElms with that xpath')	
except:
    print('Was not able to find resultElms.')

# Get gene name from result on sequence page
try:
	geneName = browser.find_element_by_xpath('/html/body/div[3]/h1[1]/i')
	print ('geneName')	
except:
    print('Was not able to find geneName')




#time.sleep(5) # This allows me a good amount of time to look at the results before closing browser. 
browser.close() # If I don't close the browser, they pile up

#target = "_blank"



