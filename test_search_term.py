import hydra_ts
import unittest


class TestResults(unittest.TestCase):

	search_term = ( 
					('ig',  'Sc4wPfr_1127.1.g1468.t2'),
				   )
	
	def test_search_known_results(self):
		#Inputs a search term and gets a geneId
		for term,value in self.search_term: 
			result = hydra_ts.search_term(term)
			self.assertEqual(value,result, "Should be geneID: " +value)


if __name__ == '__main__':
	unittest.main()