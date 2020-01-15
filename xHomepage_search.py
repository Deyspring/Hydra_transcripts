#!python3
# A little test script to enter text into the Pfam domain name searchbox, 
# and then identify a resulting link


import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

###Home page: window_first
window_first = browser.window_handles[0] # Store the window handle variable before clicking any links
print("window_first")

try:
	keywordElem = browser.find_element_by_xpath('/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]')
	print('Found keywordElem with that xpath!')
except:
    print('Was not able to find keywordElem.')

#inputString = input('Enter "ig" as a test search term: ')
keywordElem.send_keys('ig')

#Click on the search button  
try:
	buttonPress = browser.find_element_by_xpath(
		'/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]').click()
	print ('Found buttonPress with that xpath')
except:
    print('Was not able to find buttonPress.')

#Click on gene id link returned by search 
try:
	resultElms = browser.find_element_by_xpath(
		'/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a').click()
	print ('Found resultElms with that xpath')	
except:
    print('Was not able to find resultElms.')

###Gene page: window_second
time.sleep(5) # This is crucial!!! If the browser does not have time to load the second page, the handle will not be reset to the correct page. 
window_second = browser.window_handles[1] # After clicking the result button, store the window handle variable of second page
browser.switch_to.window(window_second)
print("window_second")

# Get gene name from result on sequence page
try:
	geneLink = browser.find_element_by_link_text('View Gene in Genome Browser').click() 
	print ('Found geneLink with that xpath')
except:
    print('Was not able to find geneLink')

###Gene Browser : window_third
time.sleep(5)
window_third = browser.window_handles[2]
browser.switch_to.window(window_third)
print('window_third') 

time.sleep(5)# This needs to be at least 5 seconds; adjust higher for slower connections to allow browser to load
try:
	JulianoCheckbox = browser.find_element_by_xpath(
		'/html/body/div[2]/div[4]/div[5]/div[2]/div/div/label[2]/input').click()
	print ('Found JulianoCheckbox')	
except:
    print('Was not able to find JulianoCheckbox')

time.sleep(5)
try:
	JulianoDropdownMenu = browser.find_element_by_xpath(
		'/html/body/div[2]/div[2]/div/div/div[1]/div/div[4]/div[3]/div[2]').click()
	print ('Found JulianoDropdownMenu')	
except:
    print('Was not able to find JulianoDropdownMenu')


try: 
	save  
	"https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/Sc4wPfr_1127.1/trackData.json"
except:
    print('Was not able to save aepLRv2_splign data')
 https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/Sc4wPfr_1127.1/Juliano_aepLRv2-Sc4wPfr_1127.1-1..841098.bed


time.sleep(5) 
browser.close()
browser.switch_to.window(window_second)
browser.close()
browser.switch_to.window(window_first)
browser.close()




