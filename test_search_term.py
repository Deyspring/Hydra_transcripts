import search_pfam
import unittest


class TestResults(unittest.TestCase):

	known_values = ( 
					('ig',  'Sc4wPfr_1127.1.g1468.t2'),
				   )
    
	
	def test_search_known_results(self):
		'''Returns a known geneId value when given a known search term''' 
		for term,value in self.known_values: 
			result = search_pfam.search_term(term)
			self.assertEqual(value,result, "Should be geneID: " +value)

	def test_search_bad_input(self):
		'''Should fail when given a numerical only input'''
		#result = search_pfam.search_term(term)
		self.assertRaises(search_pfam.NotStringError, search_pfam.search_term, 4000)


if __name__ == '__main__':
	unittest.main()