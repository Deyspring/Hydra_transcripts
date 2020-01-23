# !python
# Json file stripper module
# Transcripts are returned after a Json file is downloaded, transformed to python code and the transcripts are stripped out.   

import json, requests, sys, pprint

def transcripts_from_Json(json_url): 
	# Download the JSON data from Hydra Portal's API using a url

	response = requests.get(json_url)
	response.raise_for_status()

 	# Load JSON data into a Python variable.
	transcripts_data = json.loads(response.text)
	t = transcripts_data['intervals']

	transcripts= t['nclist'][0][6] #This complicated selector is necessary because the dictionary is nested. 
	
	return transcripts

#This must be a freshly made json url, or the test won't work
json_url = 'https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/scaffold/Sc4wPfr_1127/trackData.json'

list_of_transcripts = transcripts_from_Json(json_url)

print (transcripts)


		