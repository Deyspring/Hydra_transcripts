# !python
# Json file stripper module
# Transcripts are returned after a Json file is downloaded, transformed to python code and the transcripts are stripped out.   

import json, requests, sys, pprint

gene_ids = ['Sc4wPfr_1127.1.g1468.t2', 'Sc4wPfr_1127.1.g1468.t1', 'Sc4wPfr_172.1.g1573.t1', 'Sc4wPfr_172.1.g1567.t1', 'Sc4wPfr_424.1.g2114.t1', 'Sc4wPfr_708.g2567.t1', 'Sc4wPfr_708.g2561.t1', 'Sc4wPfr_1357.1.g3221.t1', 'Sc4wPfr_758.g3713.t1', 'Sc4wPfr_758.g3713.t2', 'Sc4wPfr_435.1.g6986.t1', 'Sc4wPfr_307.g9631.t1', 'Sc4wPfr_1300.g9811.t1', 'Sc4wPfr_1300.g9811.t2', 'Sc4wPfr_178.g10676.t1', 'Sc4wPfr_309.g10789.t1', 'Sc4wPfr_309.g10788.t1', 'Sc4wPfr_197.g11018.t1', 'Sc4wPfr_96.g11969.t1', 'Sc4wPfr_96.g11963.t1', 'Sc4wPfr_96.g11965.t1', 'Sc4wPfr_720.g12291.t1', 'Sc4wPfr_124.g12319.t1', 'Sc4wPfr_304.2.g12749.t1', 'Sc4wPfr_729.g12871.t2', 'Sc4wPfr_729.g12871.t1', 'Sc4wPfr_274.1.g13601.t1', 'Sc4wPfr_138.g13918.t1', 'Sc4wPfr_250.g16094.t1', 'Sc4wPfr_875.1.g17139.t1', 'Sc4wPfr_811.1.g17337.t1', 'Sc4wPfr_854.g18494.t1', 'Sc4wPfr_66.g19053.t1', 'Sc4wPfr_66.g19052.t1', 'Sc4wPfr_347.g19288.t3', 'Sc4wPfr_347.g19288.t1', 'Sc4wPfr_347.g19288.t2', 'Sc4wPfr_95.2.g19499.t1', 'Sc4wPfr_95.2.g19498.t1', 'Sc4wPfr_132.g22649.t1', 'Sc4wPfr_132.g22677.t1', 'Sc4wPfr_132.g22677.t2', 'Sc4wPfr_378.g22720.t1', 'Sc4wPfr_378.g22717.t2', 'Sc4wPfr_378.g22717.t1', 'Sc4wPfr_172.2.g23178.t1', 'Sc4wPfr_106.g23594.t1', 'Sc4wPfr_293.g24406.t1', 'Sc4wPfr_384.g24768.t1', 'Sc4wPfr_384.g24766.t1', 'Sc4wPfr_268.g25749.t1', 'Sc4wPfr_268.g25749.t2', 'Sc4wPfr_268.g25756.t1', 'Sc4wPfr_268.g25754.t1', 'Sc4wPfr_268.g25754.t2', 'Sc4wPfr_338.g25873.t1', 'Sc4wPfr_705.g26924.t1', 'Sc4wPfr_599.g27237.t1', 'Sc4wPfr_599.g27237.t2', 'Sc4wPfr_599.g27237.t3', 'Sc4wPfr_287.2.g28208.t1', 'Sc4wPfr_199.g28577.t2', 'Sc4wPfr_199.g28594.t1', 'Sc4wPfr_199.g28577.t1', 'Sc4wPfr_199.g28578.t1', 'Sc4wPfr_1301.g29099.t1', 'Sc4wPfr_624.g29791.t1', 'Sc4wPfr_463.g30865.t1', 'Sc4wPfr_1077.g31033.t1', 'Sc4wPfr_7.g33202.t1', 'Sc4wPfr_844.g33356.t1']

def transcripts_from_Json(gene_ids): 
	# Download the JSON data from Hydra Portal's API using a url
	transcripts = []

	for gene_id in gene_ids: 

		url = 'https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/'\
			  + gene_id + '/trackData.json'

		response = requests.get(url)
		response.raise_for_status()

 		# Load JSON data into a Python variable.
		transcript_data = json.loads(response.text)
		t = transcript_data['intervals']

		#print(t['nclist'][0][6]) #This complicated selector is necessary because the dictionary is nested. 
		
		transcripts.append(t['nclist'][0][6])

	return transcripts

transcripts = transcripts_from_Json(gene_ids)
print (transcripts)


		