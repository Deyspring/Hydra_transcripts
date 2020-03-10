# !python
# json file transcript stripper module
# Transcripts are returned after a Json file is downloaded and assigned to a variable.
# The transcripts are then stripped out of the variable.  

import json, requests, sys, pprint
from selenium import webdriver

def transcripts_data(url): 
	# Download the JSON data from the Hydra Portal's API using a url and get the transcripts from it. 
	browser = webdriver.Firefox()
	
	print ("Json_stripper module")
	transcripts =[]
	response = requests.get(url)
	response.raise_for_status()

	# Load JSON data into a Python variable.
	transcripts_data = json.loads(response.text)
	transcripts_text_file = transcripts_data['intervals']
	#print("transcripts_text_file from transcripts_data")
	#print (transcripts_text_file)

	for nested_list in transcripts_text_file:
		#This complicated selector is necessary because the dictionary is nested. 
		transcript = (transcripts_text_file['nclist'][0][7]).split('|')[0] 
		transcripts.append(transcript) 

	browser.close()
	print (transcripts)
	return transcripts

#This must be a freshly made json url, or the test won't work
#json_url = 'https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/Sc4wPfr_844/trackData.json'
#list_of_transcripts = transcripts_from_Json(json_url)

#Sc4wPfr_844	102021	102494	t12588aep|97511		+		

	

 

