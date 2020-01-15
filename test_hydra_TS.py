import unittest


class TestResults(unittest.TestCase):

    def test_homepage_search(self):
    	#Input a list of search terms and get different result pages
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_search_results_loop(self):
    	#Ensure the code loops through all the result GeneIDs
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test_json_format(self):
    	#Ensure that the GeneIDs are incorporated correctly into the Json links
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test_transcript_result(self):
    	#Ensure that all transcripts are returned from the JSon page and 
    	#that they are unique from previous transcript Json link results
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test_transcript_loop(self): 
    	#Ensure that the code loops through all the Json results and gets them all without
    	#errors
    	self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test_spreadsheet_transcript_append(self):
    	#Ensure that the code puts the transcripts in the right places in the spreadsheet
    	# ie. The gene identifier is placed first and then a row of transcripts for that geneId

    def test_spreadsheet_datetime(self):
    	# Ensure that the spreadhseet gets the proper date/time for the day it was run. 	

if __name__ == '__main__':
    unittest.main()