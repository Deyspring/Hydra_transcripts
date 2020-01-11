#!python3
# A little test script to enter text into the Pfam domain name searchbox, 
# and then identify a resulting link


import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')


#Home page:Tab 1?
try:
	keywordElem = browser.find_element_by_xpath('/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]')
	print('Found keywordElem with that xpath!')
except:
    print('Was not able to find keywordElem.')

#inputString = input('Enter "ig" as a test search term: ')
keywordElem.send_keys('ig')

#Click on the search button  
try:
	buttonPress = browser.find_element_by_xpath('/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]').click()
	print ('Found buttonPress with that xpath')
except:
    print('Was not able to find buttonPress.')

#Click on gene id link returned by search 
try:
	resultElms = browser.find_element_by_xpath('/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a').click()
	window_before = browser.window_handles[0]
	print("window_before")
	print ('Found resultElms with that xpath')	
except:
    print('Was not able to find resultElms.')

#time.sleep(5) # This allows me a good amount of time to look at the results before closing browser. 
#browser.close()
window_after = browser.window_handles[1]
browser.switch_to.window(window_after)
#Gene page: Tab 2? 
# Get gene name from result on sequence page
try:
	geneLink = browser.find_element_by_link_text('View Gene in Genome Browser').click() 
	window_after_that = browser.window_handles[2]
	print('window_after_that')
	print ('Found geneLink with that xpath')
except:
    print('Was not able to find geneLink')


browser.switch_to.window(window_after_that)

# Gene Browser : Tab 3? 
try:
	JulianoCheckbox = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[5]/div[2]/div/div/label[2]/input') 
	print ('Found JulianoCheckbox')	

except:
    print('Was not able to find JulianoCheckbox')
 
#time.sleep(5) 
#browser.close()

#/html/body/div[2]/div[2]/div/div/div[1]/div/div[4]/div[3]/div[2] Juliano track button xpath
#target = "_blank"


