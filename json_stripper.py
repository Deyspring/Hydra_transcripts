# !python
# json file stripper module
# Transcripts are returned after a Json file is downloaded, 
# transformed to python code and the transcripts are stripped out of the file.  

#Right now it's just stripping out the gene_id!!!! arrrgh  

import json, requests, sys, pprint

def transcripts_data(url): 
	# Download the JSON data from Hydra Portal's API using a url and get the transcripts from it. 
	
	transcripts =[]
	response = requests.get(url)
	response.raise_for_status()
	# Load JSON data into a Python variable.
	transcripts_data = json.loads(response.text)
	t = transcripts_data['intervals']

	n = 1

	while True: 
		try: 
			transcript = t['nclist'][0][7] #This complicated selector is necessary because the dictionary is nested. 
			transcripts.append(transcript)
		except: 
			print('Was not able to find a transcript')
			break

	print (transcripts)
	return transcripts

#This must be a freshly made json url, or the test won't work
#json_url = 'https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/Sc4wPfr_844/trackData.json'
#list_of_transcripts = transcripts_from_Json(json_url)

#Sc4wPfr_844	102021	102494	t12588aep|97511		+		

	

 

