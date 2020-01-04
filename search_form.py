#!python3
# Second try to get links after entering in a search term on the Hydra 2.0 portal site
#List of drivers for different webpages to import
#Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
#Firefox: https://github.com/mozilla/geckodriver/releases
#Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
#If you are using IE, just install one of the above and don't go back. 
#Info on how to install selenium on windows machine
#https://www.seleniumeasy.com/python/getting-started-selenium-webdriver-using-python

from selenium import webdriver
driver = webdriver.Chrome(r'C:\Python\chromedriver.exe') # Just because I like chrome, there are other webdrivers
type(browser)

browser.get('http://inventwithpython.com')