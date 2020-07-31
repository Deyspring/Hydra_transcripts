#Close all the browsers

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Open Firefox in headless(invisible), mode
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
browser = webdriver.Firefox(options=options)

while True: 
	try: 
		print("close browser .... ")
		browser.close()
	except: 
		print('no more open browsers')
		break
