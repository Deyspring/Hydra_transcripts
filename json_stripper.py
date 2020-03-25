# !python
# json file transcript stripper module
# Transcripts are returned after a Json file is downloaded and assigned to a variable.
# The transcripts are then stripped out of the variable.  

import json, requests, sys, pprint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import urllib.request, urllib
import re

def transcripts_data(url): 
	# Download the JSON data from the Hydra Portal's API using a url and get the transcripts from it. 
	options = webdriver.FirefoxOptions()
	options.add_argument('--headless')
	browser = webdriver.Firefox(options= options)
	
	print ('Json_stripper module\n')
	transcripts =[0]
	response = requests.get(url)
	response.raise_for_status()

	# Load JSON data into a Python variable.
	transcripts_data = json.loads(response.text)
	transcripts_text_file = transcripts_data['intervals']
	
	#regex expression
	pattern = re.compile('t\d+aep')
	transcripts = set(pattern.findall(response.text))
	
	#print (transcripts)
	browser.close()

	return transcripts


	
	

 

