#!python
import geneID
import unittest

class TestResults(unittest.TestCase):

	def __init__ (self):#Do i need this line for tests? 


		arguments = ((/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[2]/td[2]/a,
					  Sc4wPfr_1127.1.g1468.t2),
					  /html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a,
					  Sc4wPfr_1127.1.g1468.t1,),
			          /html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[4]/td[2]/a,
			          Sc4wPfr_172.1.g1573.t1,),
					  /html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[5]/td[2]/a,
					  Sc4wPfr_172.1.g1567.t1),
					  /html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[6]/td[2]/a,
					  Sc4wPfr_424.1.g2114.t1),
					  /html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[6]/td[2]/a,
					  Sc4wPfr_708.g2567.t1),
					)

		  known_links= (/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[2]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[4]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[5]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[6]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[7]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[8]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[9]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[10]/td[2]/a,
						/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[11]/td[2]/a,
						)

	       known_geneId=(Sc4wPfr_1127.1.g1468.t2,
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

	def test_geneID_result(self, arguments):
		''' geneID should give known_values with known input'''
		
		for known_links,known_geneIDs in arguments: 

			result = geneID.geneID_result(known_links)

			self.assertEqual(known_geneId,result, "Should be geneID: " + known_geneId)


	def test_geneID_link(self,know_geneId,known_links): 
		''' geneID_link should give known_input values when given row_values'''
		
		row_numbers = list(range(0,9))
		arguments = zip(row_numbers,known_geneId) 
		
		for row_number, known_geneID in arguments: 
			result = geneID.geneID_link(row_number)
			self.assertEqual(known_links, result, "Should be link: " +known_links )


if __name__ == '__main__':
	unittest.main()






