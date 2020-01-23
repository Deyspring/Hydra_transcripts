# !python
# json file stripper module
# Transcripts are returned after a Json file is downloaded, 
# transformed to python code and the transcripts are stripped out of the file.   

import json, requests, sys, pprint

def transcripts_from_Json(json_url): 
	# Download the JSON data from Hydra Portal's API using a url

	response = requests.get(json_url)
	response.raise_for_status()
	print ('raisedforstatus')
 	# Load JSON data into a Python variable.
	transcripts_data = json.loads(response.text)
	t = transcripts_data['intervals']
	print ('ttttttttttttttt')
	print ("")
	print ("")
	print ("")
	print ("")
	print (t)

	transcripts = t['nclist'][0][6] #This complicated selector is necessary because the dictionary is nested. 
	
	print ("transcripts")
	print(transcripts)

	return transcripts

#This must be a freshly made json url, or the test won't work
json_url = 'https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/scaffold/Sc4wPfr_1127/trackData.json'

list_of_transcripts = transcripts_from_Json(json_url)

linkTemplate = /hydra/jbrowse/data.cgi?type=aepLRv2&gene={load_id}

"key": "Juliano_aepLRv2",
  "feature": [
    "mRNA:AEP_SPLIGN"

"storeClass": "JBrowse/Store/SeqFeature/NCList",
  "urlTemplate": "tracks/aepLRv2_splign/{refseq}/trackData.json",

  "baseUrl": "https://research.nhgri.nih.gov/hydra/jbrowse/data/",

  track name="aepLRv2_splign" useScore=0
Sc4wPfr_844	102021	102494	t12588aep|97511		+					

 


#Juliano_aepLRv2-Sc4wPfr_844-1..1035958.bed


		