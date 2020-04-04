#! python


def mng_xl(terms,geneid_sets,transcript_sets):

	if len(terms) >= 2: 

		for term,geneid_set,transcript_set in zip(terms,geneid_sets,transcript_sets):

			print (term,"\n")

			for geneid,transcripts in zip(geneid_set,transcript_set):
				print (geneid,'/n')
				for transcript in transcripts: 
					print(transcript) 

	else: 

		print ("already combined ")
		print (terms)
		for geneid,transcripts in zip(geneid_sets,transcript_sets):
				print (geneid,'/n')
				for transcript in transcripts: 
					print(transcript) 


"""
terms = ['term1','term2']
geneids = [['g1','g1'],['g2','g2']]
transcripts = [[{'trn1','trn1a'},{'trn1b','trn1c'}],[{'trn2','trn2a'},{'trn2b','trn2c'}]]

"""
terms = ['Ig_4'] 
geneids = ['S', 'C' ] 
transcripts = [{'2','2','2','2','2','2','2'}, 
			   {'3', '3', '3', '3'}, ]

mng_xl(terms,geneids,transcripts)


