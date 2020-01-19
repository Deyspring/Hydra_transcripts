# !python
# Json file stripper module
# A module to download a Json file, transform it to Python data and strip out the relevant transcripts

import json, requests, sys, pprint

# Download the JSON data from Hydra Portal's API

#TODO: put relvant GeneId name into this url ad forget about grabbing it each time
url = "https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/Sc4wPfr_178/trackData.json"

response = requests.get(url)
response.raise_for_status()

 # Load JSON data into a Python variable.
transcriptData = json.loads(response.text)
#pprint.pprint(response.text)

t = transcriptData['intervals']

# Whoohoo! I have the code to select one transcript. 

print(t['nclist'][0][6]) #This complicated selector is necessary because the dictionary is nested. 

		