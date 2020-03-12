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

	"""for nested_list in transcripts_text_file:
		print ("nested list:", nested_list, "\n")
		#This complicated selector is necessary because the dictionary is nested. 
		transcript = (transcripts_text_file['nclist'][0][7]).split('|')[0] # I think I'm selecting the same thing again and again
		print ("transcript:", transcript,"\n") 
		transcripts.append(transcript) 
	"""
	transcripts = [[['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']]]


	browser.close()
	return transcripts

	

 

