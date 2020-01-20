#!python
import geneID
import unittest
from search_pfam import search_term 

class TestResults(unittest.TestCase):

	def __init__ (self):

	self.known_values = (Sc4wPfr_1127.1.g1468.t2,
					Sc4wPfr_1127.1.g1468.t1,
					Sc4wPfr_172.1.g1573.t1,
					Sc4wPfr_172.1.g1567.t1,
					Sc4wPfr_424.1.g2114.t1,
					Sc4wPfr_708.g2567.t1,
					Sc4wPfr_708.g2561.t1,
					Sc4wPfr_1357.1.g3221.t1,
					Sc4wPfr_758.g3713.t1,
					Sc4wPfr_758.g3713.t2,
					)

	def test_geneID_link(self, term):
		''' geneID should give known_values with known input'''
		
		search_term('term')

		for value in known_values: 

			result = geneID.geneID_aquire()