# python!
# Json file stripper module
# A module to download a Json file, transform it to Python data and strip out the relevant transcripts

import json, requests, sys, pprint


# Download the JSON data from Hydra Portal's API

#TODO: put relvant GeneId name into this url ad forget about grabbing it each time
url = "https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/Sc4wPfr_1127.1/trackData.json"

response = requests.get(url)
response.raise_for_status()

 # Load JSON data into a Python variable.
transcriptData = json.loads(response.text)
#pprint.pprint(response.text)

t = transcriptData['intervals']

print(t['nclist'][0][6])
'''
"intervals":
	{"nclist":[
		[0,40868,47718,0,"AEP_SPLIGN","Sc4wPfr_1127.1","t1160aep|7384","t1160aep|7384","gene.t1160aep|7384","mRNA",
		  [
		    [1,47689,47718,0,"AEP_SPLIGN","Sc4wPfr_1127.1","exon","t1160aep|7384"],
		    [1,40868,41041,0,"AEP_SPLIGN","Sc4wPfr_1127.1","CDS","t1160aep|7384"],
		    [1,40868,41041,0,"AEP_SPLIGN","Sc4wPfr_1127.1","exon","t1160aep|7384"],
		    [1,47689,47718,0,"AEP_SPLIGN","Sc4wPfr_1127.1","CDS","t1160aep|7384"]
		  ]
		]

 #Print transcript variables
t =transcriptData['list']
print(t[6])
'''

		