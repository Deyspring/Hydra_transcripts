# !python
# Json file stripper module
# Transcripts are returned after a Json file is downloaded, transformed to python code and the transcripts are stripped out.   

import json, requests, sys, pprint

def transcripts_from_Json(geneID): 
	# Download the JSON data from Hydra Portal's API using a url
	url = "https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/" 
		  + geneID + "/trackData.json"

	response = requests.get(url)
	response.raise_for_status()

 	# Load JSON data into a Python variable.
	transcriptData = json.loads(response.text)

	t = transcriptData['intervals']

	# Whoohoo! I have the code to select one transcript. 
	print(t['nclist'][0][6]) #This complicated selector is necessary because the dictionary is nested. 

	return t['nclist'][0][6]

		